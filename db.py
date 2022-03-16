import re
import sqlite3

import csv
import time
import os
import subprocess
import glob
import hashlib

files = "./csv/*.csv"
csv_list = glob.glob(files)
sq_dir = './sqlite-tools-win32-x86-3380000/sqlite3.exe'
db_path = "./whereabouts.db"

md5_hash = hashlib.md5()

with open('./csv/added_csvs.txt', 'r') as a:
    added_csvs = a.read().splitlines()
w = open('./csv/added_csvs.txt', 'a')


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
    for row in reader_rows:
        row_counter += 1
        if len(row) == 9:
            to_db = row
        elif not row:
            to_db = [None] * 9
        elif len(row) < 9:
            row.extend([None] * (9 - len(row) - 1))
            to_db = row
        else:
            print(f'failed to add {fname} to db. The number of cells on row {row_counter} exceeds the table columns 9.')
            break
        try:
            cur.execute("INSERT INTO Joined VALUES(?,?,?,?,?,?,?,?,?)", to_db)
        except:
            print(f'failed to add {fname} to db.')
            con.close()
            break

    # commit when done with file
    con.commit()

    # try:
        # dbimport = subprocess.check_output(sq_dir + ' ' + db_path + """ ".mode csv" ".separator '\t'" ".importn """ + fname + ' Joined"', stderr=subprocess.STDOUT, cwd='./')

    # except subprocess.CalledProcessError as e:
    #     print('Failed to add {} to database!\n{}'.format(fname, e))
    #     continue

    w.write(digest + '\n')


w.close()
    # dbimport = subprocess.check_call('{} {} ".mode csv" ".import {} Joined"'.format(sq_dir, db_path, fname), stderr=subprocess.STDOUT)
    # newrows = subprocess.check_output(sq_dir + ' ' + db_path + """ "SELECT max(rowid) FROM Joined;" """)

    # rowsadded = int(newrows) - int(oldrows)
    # print(rowsadded, "rows out of", len(airolist), "has been added to db")
    # print(newrows)

    # p = str(dbimport).count('extras ignored')
    # if p > 0:
    #     errlog = open('db.py.log','w')
    #     errlog.write(str(dbimport))
    #     errlog.close()
    #     print(p, "lines could not be completely added due to excessive column count!. Read the log file: db.py.log")
    # if len(airolist) - rowsadded != 0:
    #     print(len(airolist) - rowsadded, "lines could not be added, reason: UNKNOWN")