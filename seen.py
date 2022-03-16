#import sqlite3 as lite
from sqlite3 import connect
#import sys
#MAC = 'A8:B8:6E:37:EE:A3'
#MAC = sys.argv[1].upper()
from tkinter import Tk
from textbox import textbox
import time
before = time.time()


class Seen:
    pass


way = ['oui-2017-12-17-wayback', 'oui-2015-01-23-wayback', 'oui-2015-01-28-wayback', 'oui-2015-02-07-wayback', 'oui-2015-02-11-wayback', 'oui-2015-02-19-wayback', 'oui-2015-03-03-wayback', 'oui-2015-03-07-wayback', 'oui-2015-03-09-wayback', 'oui-2015-03-10-wayback', 'oui-2015-03-13-wayback', 'oui-2015-04-04-wayback', 'oui-2015-04-05-wayback', 'oui-2015-04-07-wayback', 'oui-2015-04-11-wayback', 'oui-2015-04-13-wayback', 'oui-2015-04-18-wayback', 'oui-2015-04-23-wayback', 'oui-2015-04-25-wayback', 'oui-2015-05-03-wayback', 'oui-2015-05-12-wayback', 'oui-2015-05-23-wayback', 'oui-2015-05-24-wayback', 'oui-2015-05-31-wayback', 'oui-2015-06-13-wayback', 'oui-2015-07-23-wayback', 'oui-2015-07-31-wayback', 'oui-2015-08-11-wayback', 'oui-2015-08-12-wayback', 'oui-2015-08-16-wayback', 'oui-2015-08-18-wayback', 'oui-2015-09-27-wayback', 'oui-2015-10-07-wayback', 'oui-2015-10-12-wayback', 'oui-2015-10-25-wayback', 'oui-2015-10-31-wayback', 'oui-2015-11-15-wayback', 'oui-2015-12-22-wayback', 'oui-2016-01-16-wayback', 'oui-2016-03-02-wayback', 'oui-2016-03-15-wayback', 'oui-2016-04-03-wayback', 'oui-2016-04-12-wayback', 'oui-2016-05-02-wayback', 'oui-2016-05-19-wayback', 'oui-2016-05-31-wayback', 'oui-2016-06-17-wayback', 'oui-2016-06-28-wayback', 'oui-2016-07-18-wayback', 'oui-2016-07-22-wayback', 'oui-2016-07-27-wayback', 'oui-2016-08-05-wayback', 'oui-2016-08-06-wayback', 'oui-2016-08-26-wayback', 'oui-2016-09-28-wayback', 'oui-2016-11-16-wayback', 'oui-2016-11-26-wayback', 'oui-2017-03-26-wayback', 'oui-2017-05-23-wayback', 'oui-2017-06-02-wayback', 'oui-2017-06-17-wayback', 'oui-2017-07-14-wayback', 'oui-2017-08-13-wayback', 'oui-2017-08-21-wayback', 'oui-2017-09-10-wayback', 'oui-2017-09-16-wayback']
way.sort(); way.reverse()
conn = connect('C:\\Users\\Bilal\\Desktop\\whereabouts\\db.db')
conn = connect(r'O:\whereabouts\hopecsv\whereabouts.db')
conn.text_factory = bytes
cur = conn.cursor()
conn2 = connect('C:\\Users\\Bilal\\Desktop\\whereabouts\\wayback - Copy.db')
cur2 = conn2.cursor()

def err():
    print('!!---ERROR---!!'); textbox('!!---ERROR---!!'); quit()

def get_posts():
    result = ''
    cur.execute("SELECT * FROM Joined WHERE field1 = '" + MAC + "'")
    try: c = cur.fetchall()
    except: err()
    i = 0
    count = len(c)
    for row in c:
        for cell in row:
            i+=1
            if i == 3:
                #cell = row[2][10:]
                try: result += '{}{} '.format('-', cell.decode("utf-8")[10:])
                except: err()
            #if cell == row[3]:
                #break
            #if cell is not None:
                #cell = cell.encode('UTF-8') activate if you wanna show probed SSIDs
            elif cell:
                try: result += '{} '.format(cell.decode("utf-8", errors='ignore'))
                except: err()
        result += '\n'
        i = 0
    #print(MAC)
    #if err == True: print('!!---ERROR---!!'); textbox('!!---ERROR---!!'); quit()
    return [result, count]

def get_oui():
    result = ''
    i = 0
    for table in way:
        cur2.execute("SELECT field3 FROM '" + table + "' WHERE field1 = '" + oui + "' LIMIT 1")
        o = cur2.fetchall()
        if i < len(way) - 1: i+=1
        if not o:
            if result: result += ' - {} wayback'.format(table[4:14])
            break
        else:
            result = '{}\n{}'.format(o[0][0], way[i-1][4:14])

    return '{}\n'.format(result)

if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    MACS = root.clipboard_get().upper()
    result = ''
    for row in MACS.splitlines():
        row = row[0:17]
        oui = row[0:8].replace(':','')
        MAC = row
        entry = get_posts()[0]
        result += entry
        result += get_oui()
        if entry:
            result += '-----------------------------------------------------------------------\n'

    result = 'in {}ms\n{}'.format(int((time.time() - before)*1000), result)

    try: print(result)
    except: pass
    textbox(result)
    conn.close()
    conn2.close()


#print(MAC)
#sqdir = """C:\\Users\\Bilal\\Desktop\\whereabouts\\sqlite-tools-win32-x86-3240000\\sqlite3.exe"""
#dbdir = """C:\\Users\\Bilal\\Desktop\\whereabouts\\db.db"""

#dbimport = subprocess.check_output(sqdir + ' ' + dbdir + """ ".mode csv" "SELECT * FROM Joined WHERE field1 = '""" + MAC + """'" """,stderr=subprocess.STDOUT)
#dbimport = str(dbimport)
#f = re.match('A', dbimport)
#dbimport = re.sub("""\r\n""", '\r\n', dbimport)

#print(f)