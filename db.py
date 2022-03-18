# import re
import sqlite3
import csv
import time
import os
# import subprocess
import glob
import hashlib

files = "./csv/*.csv"
csv_list = glob.glob(files)
db_path = "./whereabouts.db"
md5_hash = hashlib.md5()

if not os.path.exists(db_path):
    print(f'DB not found. Creating {db_path} ...')
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    create_table = '''
    CREATE TABLE "Joined" (
    "Field1"	TEXT,
    "Field2"	TEXT,
    "Field3"	TEXT,
    "Field4"	TEXT,
    "Field5"	TEXT,
    "Field6"	TEXT,
    "Field7"	TEXT,
    "Field8"	TEXT,
    "Field9"	TEXT
    ); '''
    create_index = '''
    CREATE INDEX "MAC" ON "Joined" (
    "Field1"); '''
    cur.execute(create_table)
    cur.execute(create_index)
    con.commit()
    con.close()

w = open('./csv/db_csvs.txt', 'r+')
added_csvs = w.read().splitlines()


for csv_file in csv_list:
    fname = os.path.split(csv_file)[1]
    with open(csv_file, 'r') as c:
        content = c.read()
        rows = content.splitlines()
        md5_hash.update(content[:10000].encode())
        digest = md5_hash.hexdigest()
        reader_rows = csv.reader(rows, delimiter='\t')

    if digest in added_csvs:
        print('{} is already added to the database. Skipped.'.format(fname))
        continue

    print('adding {} to database...'.format(fname))
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    row_counter = 0
    not_added = 0
    success = True
    for row in reader_rows:
        row_counter += 1
        # Ignored headers & empty rows
        if 'First seen' in row or not len(row):
            not_added += 1
            continue
        # Insure a
        if len(row) <= 9:
            row.extend([None] * (9 - len(row)))
            to_db = row
        else:
            print(f'failed to add {fname} to db. The number of cells on row {row_counter} exceeds the table columns 9.')
            success = False
            break
        try:
            cur.execute("INSERT INTO Joined VALUES(?,?,?,?,?,?,?,?,?)", to_db)
        except:
            print(f'failed to add {fname} to db.')
            con.close()
            success = False
            break

    # commit when done with file
    if success:
        con.commit()
        print(f'added {row_counter - not_added} rows to db')
        w.write(digest + '\n')

w.close()
