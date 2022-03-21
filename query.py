from sqlite3 import connect
from tkinter import Tk
from textbox import textbox
import time
import argparse
import os
before = time.time()

db_path = './whereabouts.db'
if not os.path.exists(db_path):
    print(f'Database does not exist in "{db_path}"')
    quit(1)
conn = connect(db_path)
conn.text_factory = bytes
cur = conn.cursor()

with open('create_ouis.csv', 'r', encoding='utf-8') as o:
    ouis = {}
    # fetch OUIs from db into a dict {ABCDEF:COMPANY}
    for line in o:
        s = line.strip().split('\t')
        if len(s) > 2:
            ouis[s[0].replace(':', '')] = s[2]
        else:
            ouis[s[0]] = ''


def get_db_entries(mac) -> str:
    entries = ''
    cur.execute("SELECT * FROM Joined WHERE field1 = '" + mac + "'")
    c = cur.fetchall()
    for row in c:
        for i in row:
            if i:
                entries += i.decode("utf-8") + '\t'
            else:
                entries += '\t'
        entries += '\n'
    entries += '\n'
    return entries


def get_oui(oui) -> str:
    if oui in ouis:
        return f'\nMAC address was added to IEEE list of OUIs at: {ouis[oui]}'
    else:
        return '\nDate not found in OUIs list. either this MAC is randomized or the OUIs list is outdated'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Query MAC address(es) from database')
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument('-m', '--mac', help='MAC address')
    g.add_argument('-f', '--file', help='File with list of MAC addresses')
    g.add_argument('-c', '--clipboard', help='MAC addresses from clipboard', action='store_true')
    parser.add_argument('-b', '--text-box', help='Show results in a text box', action='store_true')
    args = parser.parse_args()
    if args.mac:
        MACS = args.mac.upper()
    elif args.file:
        if not os.path.exists(args.file):
            print(f'File "{args.file}" does not exist!')
            conn.close()
            quit(1)
        with open(args.file, 'r') as f:
            MACS = f.read()
    else:
        root = Tk()
        root.withdraw()
        MACS = root.clipboard_get().upper()
    output = ''
    fetched = 0
    for row in MACS.splitlines():
        mac = row[0:17]
        oui = row[0:8].replace(':', '')
        if not oui:
            continue
        # check for valid hex MAC address
        try:
            int(oui, 16)
        except ValueError:
            output += f'"{row}" is not a valid MAC address\n'
        else:
            mac_row = f'MAC: {row}\n\n'
            db_entries = get_db_entries(mac)
            oui_res = get_oui(oui)
            output += mac_row + db_entries + oui_res + '\n'
            print(mac_row + db_entries + oui_res)
            fetched += 1
        finally:
            separator = '-----------------------------------------------------------------------'
            print(separator)
            output += separator + '\n'

    print(f'Fetched {fetched} results from database in {int((time.time() - before)*1000)}ms')
    if args.text_box:
        textbox(output)
    conn.close()
