import csv
import os
import time
import sys
import pyperclip
from tkinter import messagebox
import tkinter
import datetime
from textbox import textbox


def get_macs(MACS):
    result = str()
    with open('./create_ouis.csv', 'r', encoding='utf-8') as f:
        dd = f.readlines()
        ouis = dict()
        for line in dd:
            entry = line.split('\t')
            ouis[entry[0]] = entry[1]
            # ouis[line[:8]] = line[9:].strip().upper()
    for mac in MACS:
        if mac[:8] in ouis:
            result += ouis[mac[:8]] + '\n'
        else:
            result += '\n'
    return result

#print(time.time() - before)
#messagebox.showinfo("MACresolver", time.time() - before)
#root.clipboard_clear()
#root.clipboard_append('ass')



if __name__ == '__main__':
    before = time.time()
    root = tkinter.Tk()
    root.withdraw()

    MACS = pyperclip.paste().upper().splitlines()

    if not os.path.isfile('./create_ouis.csv'):
        print('oui file does not exist')
        quit()

    mtime = os.path.getmtime('./create_ouis.csv')
    mtime = datetime.datetime.fromtimestamp(mtime)

    result = get_macs(MACS)
    result = result.replace('\r', '')
    
    if len(sys.argv) == 1:
        print(result)
        print('{} ouis in {} seconds'.format(result.count('\n'), time.time() - before))
        pyperclip.copy(result)
        pyperclip.paste()
        delta = datetime.datetime.today() - mtime
        messagebox.showinfo("MACresolver", '{}\n\nOUI file is {} days old'.format('ouis have been copied to Clipboard', delta.days))
        #print(datetime.datetime.now() - mtime)
        textbox(result)
    elif sys.argv[1] == 'call':
        textbox(result)
