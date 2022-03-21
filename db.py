import sqlite3
import csv
import os
import glob
import hashlib


def csv_digest(content):
    md5_hash = hashlib.md5()
    md5_hash.update(content[:10000].encode())
    digest = md5_hash.hexdigest()
    return digest


def db_create(db_path):
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
    create_csvs = '''
        CREATE TABLE "CSVs" (
        "digest"    TEXT
    ); '''
    create_csvs_index = '''
        CREATE INDEX "digest" ON "CSVs" (
        "digest"); '''
    cur.execute(create_table)
    cur.execute(create_index)
    cur.execute(create_csvs)
    cur.execute(create_csvs_index)
    con.commit()
    con.close()


def db_add():
    files = "./csv/*.csv"
    csv_list = glob.glob(files)
    db_path = "./whereabouts.db"

    if not os.path.exists(db_path):
        print(f'DB not found. Creating {db_path} ...')
        db_create(db_path)

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    for csv_file in csv_list:
        fname = os.path.split(csv_file)[1]
        with open(csv_file, 'r', encoding='utf-8') as c:
            content = c.read()
            rows = content.splitlines()
            digest = csv_digest(content)
            cur.execute(f"SELECT digest from CSVs WHERE digest = '{digest}'")
            db_digest = cur.fetchone()
            if db_digest:
                print('{} is already added to the database. Skipped.'.format(fname))
                continue
            reader_rows = csv.reader(rows, delimiter='\t')

        print('adding {} to database...'.format(fname))

        row_counter = 0
        not_added = 0
        success = True
        for row in reader_rows:
            row_counter += 1
            # Ignore counting headers & empty rows
            if 'First seen' in row or not len(row):
                not_added += 1
                continue
            # Ensure a row has 9 cells
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
            cur.execute(f"INSERT INTO CSVs (digest) VALUES('{digest}');")
            con.commit()
            print(f'added {row_counter - not_added} rows to db')

    con.close()

if __name__=='__main__':
    db_add()
