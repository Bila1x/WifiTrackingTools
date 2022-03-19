import csv
import time
import datetime
from MACresolver import get_macs
import subprocess
import re
from sqlite3 import connect
from seen import Seen
import mostLines
import os

before = time.time()

file = r'1dec'
devices = set()
print(file)

# csvdir = r'C:\Users\Bilal\Desktop\whereabouts\\'
# dbdir = 'C:\\Users\\Bilal\\Desktop\\whereabouts\\db.db'
csv_dir = r'./csv/'
db_dir = './whereabouts.db'
if os.name == 'nt':
    windump_path = './WinDump.exe'
else:
    windump_path = 'tcpdump'

# Get prone OUI list
with open('./proneOUIs.txt', 'r') as pr:
    prone = pr.read().splitlines()

# CONNECT TO DB
conn = connect(db_dir)
conn.text_factory = bytes
cur = conn.cursor()

# GET LIST OF ALL DEVICES:
with open(csv_dir + f'{file}.csv', 'r') as d:
    reader = csv.reader(d, delimiter='\t')
    z = list(reader)
    STA = False
    for device in z:
        if len(device) and 'Station' in device[0]:
            STA = True
        if len(device) and device[0] == 'Undefined':
            break
        if STA and len(device):# and device[4].isdigit() and int(device[4]) > 0:# and int(device[3]) > -80:
            devices.add(device[0].upper())

print('total devices: {}'.format(len(devices)))
# FILTER OUT NON-RANDOM DEVICES:
res = get_macs(devices).splitlines()
count = 0
pronecount = 0
for line in res:
    if line:
        count +=1
        if line in prone:
            pronecount += 1
print('actual devices: {}'.format(count))

def count_seen():
    new = 0
    with open('./pyoui-27-02-2019.txt', 'r') as f:
        dd = f.readlines()
        ouis = dict()
        for line in dd:
            ouis[line[:8]] = line[9:].strip().upper()

    for device in devices:
        if device[:8] in ouis:
            cur.execute(f"SELECT field1 FROM Joined WHERE field1 = '{device}'")
            try: c = cur.fetchall()
            except: print('ERROR COUNTING SEEN DEVICES'); break
            if len(c) != 1:
                new += 1
    conn.close()
    print('Unique devices: {} ({}% from actual devices)'.format(new, round(new/count*100)))
count_seen()

# GET DERANDED DEVICES FROM CAP:
try:
    p = subprocess.check_output(windump_path + f' -ten -r ./cap/{file}.cap (wlan addr1 22:22:22:22:22:22) or (wlan src 22:22:22:22:22:22)', stderr=subprocess.STDOUT).decode('utf-8')
except FileNotFoundError:
    print(f'ERROR: {windump_path} not found')
    quit(1)

responses = int(p.count('SA:22:22:22:22:22:22')/2)

p = p.splitlines()
unique = set()
SSIDs = {}
ack = 0
deranded = []
for line in p:
    if 'st ' in line:
        a = re.search('SA:(..:..:..:..:..:..)', line)
        b = re.search('st \((.*)\)', line)
        c = re.search('DA:22:22:22:22:22:22', line)
        add = a.group(1) + '-' + b.group(1)
        if add not in unique and c:
            deranded.append(a.group(1).upper())
        if a.group(1) and add not in unique:
            unique.add(add)
            if b.group(1) in SSIDs:
                SSIDs[b.group(1)] += 1
            else:
                SSIDs[b.group(1)] = 1
    elif 'Acknowledgment' in line:
        ack += 1


# print('Responses sent: {}'.format(responses))
if responses:
    print('Acks/Responses received: {}/{} ({}%)'.format(ack, responses, round(ack/responses*100)))
else:
    print('no Responses sent!')
if count and responses:
    print('deranded devices: {} ({}% from total devices) ({}% from actual devices) ({}% from total responses) ({}% prone OUIs to derand)'
      .format(len(unique), round(len(unique) / len(devices) * 100, 2), round(len(unique) / count * 100, 2), round(len(unique) / responses * 100, 3), round(len(unique) / pronecount * 100, 2)))

for item in reversed(sorted(SSIDs.items(), key= lambda x: x[1])):
    print([item[1], item[0], '{}%'.format(round(item[1]/len(unique)*100, 1))])

print('\nDeranded devices:')
ll = get_macs(deranded)
for line in reversed(sorted(mostLines.rows(ll.splitlines(), 1))):
    print('{} ({}% of this OUI)'.format(line, round(line[0]/res.count(line[1])*100, 3)))

print('time to run: {}'.format(time.time() - before))