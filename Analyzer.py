import csv
import time
from MACresolver import get_macs
import subprocess
import re
from sqlite3 import connect
import mostLines
import os
from db import csv_digest
import argparse
import configparser

before = time.time()

fake_ap_mac = '22:22:22:22:22:22'

parser = argparse.ArgumentParser(description='Analyze a capture file')
parser.add_argument('cap_file', help='capture file path')
args = parser.parse_args()

cap_file = args.cap_file
csv_file = os.path.splitext(os.path.basename(cap_file))[0] + '.csv'

if not os.path.exists(cap_file):
    print(f'Capture file "{cap_file}" does not exist!')
    quit(1)
if not os.path.exists(csv_file):
    print(f'CSV file of "{cap_file}" does not exist in "./csv/". Run indexer.py on the capture file first.')
    quit(1)

csv_dir = './csv/'
devices = set()
db_dir = './whereabouts.db'
if os.name == 'nt':
    windump_path = './WinDump.exe'
else:
    windump_path = 'tcpdump'

# Get prone OUI list
with open('./proneOUIs.txt', 'r', encoding='utf-8') as pr:
    prone = pr.read().splitlines()

# CONNECT TO DB
conn = connect(db_dir)
conn.text_factory = bytes
cur = conn.cursor()

# Get CSVs added to db
with open(csv_dir + 'db_csvs.txt', 'r') as a:
    added_csvs = a.read().splitlines()

# GET LIST OF ALL DEVICES:
with open(csv_dir + csv_file, 'r', encoding='utf-8') as d:
    reader = csv.reader(d, delimiter='\t')
    z = list(reader)
    d.seek(0)
    content = d.read()
    if csv_digest(content) in added_csvs:
        print(f'{csv_file} is added to database')
        in_db = True
    else:
        print(f'{csv_file}.csv is not added to database')
        in_db = False
    del content

STA = False
for device in z:
    if len(device) and 'Station' in device[0]:
        STA = True
    if len(device) and device[0] == 'Undefined':
        break
    if STA and len(device):# and device[4].isdigit() and int(device[4]) > 0:# and int(device[3]) > -80:
        devices.add(device[0].upper())

print('\n# of devices (incl. randomized MACs): {}'.format(len(devices)))

# FILTER OUT DEVICES WITH NON-RANDOM MACS:
res = get_macs(devices).splitlines()
actual = 0
pronecount = 0
for line in res:
    if line:
        actual +=1
        if line in prone:
            pronecount += 1
print('# of actual devices: {}'.format(actual))

def count_seen():
    unique = 0
    with open('./create_ouis.csv', 'r', encoding='utf-8') as f:
        dd = f.readlines()
        ouis = dict()
        for line in dd:
            entry = line.split('\t')
            ouis[entry[0]] = entry[1]

    for device in devices:
        if device[:8] in ouis:
            cur.execute(f"SELECT field1 FROM Joined WHERE field1 = '{device}'")
            try: db_hits = cur.fetchall()
            except: print('ERROR COUNTING SEEN DEVICES'); break
            if len(db_hits) <= in_db:
                unique += 1
    conn.close()
    print(f'Unique devices to database: {unique} ({round(unique / actual * 100)}% first seen devices)')
count_seen()

# GET DERANDED DEVICES FROM CAP:
try:
    p = subprocess.check_output(windump_path + f' -ten -r {cap_file} (wlan addr1 {fake_ap_mac}) or (wlan src {fake_ap_mac})', stderr=subprocess.STDOUT).decode('utf-8')
except FileNotFoundError:
    print(f'ERROR: "{windump_path}" not found')
    quit(1)
except:
    print(f'ERROR: "{windump_path}" failed to run. Did you install the dependencies?')

responses = int(p.count('SA:22:22:22:22:22:22')/2)

p = p.splitlines()
unique = set()
SSIDs = {}
ack = 0
deranded = []
for line in p:
    if 'Request ' in line:
        a = re.search('SA:(..:..:..:..:..:..)', line)
        b = re.search('Request \((.*)\)', line)
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

if responses:
    print('\nAcknowledgements received / Probe Responses sent: {}/{} ({}%)'
          .format(ack, responses, round(ack/responses*100)))
else:
    print('\nAcknowledgements received / Probe Responses sent: 0/0 (0%)')
    print('No responses found. Either no devices probed for your SSID(s),'
          ' or deanonymize.py did not run during the capture.')

if actual and responses:
    print(f'De-anomymized devices: {len(unique)}\n\t'
          f'{round(len(unique) / actual * 100, 2)}% from actual devices\n\t'
          f'{round(len(unique) / responses * 100, 3)}% from total responses\n\t'
          f'{round(len(unique) / pronecount * 100, 2)}% devices prone to de-anonymization')

print('\nResponses to fake AP:')
if SSIDs.items():
    print('┌─' + '─' * 10 + '┬─' + '─' * 30 + '┬─' + '─' * 5 + '─┐')
    print(f'│ {"Responses": <10}│ {"SSID": <30}│ {"%": <5} │')
    for x in reversed(sorted(SSIDs.items(), key= lambda x: x[1])):
        line = f'│ {x[1]: <10}│ {x[0]: <30}│ {round(int(x[1])/len(unique)*100, 1): <5} │'
        print('├─' + '─' * 10 + '┼─' + '─' * 30 + '┼─' + '─' * 5 + '─┤')
        print(line)
    print('└─' + '─' * 10 + '┴─' + '─' * 30 + '┴─' + '─' * 5 + '─┘')
else:
    print('No responses found. Either no devices probed for your SSID(s),'
          ' or deanonymize.py did not run during the capture.')

print('\nDe-anomymized devices stats:')
ll = get_macs(deranded)
if ll:
    print('┌─' + '─' * 10 + '┬─' + '─' * 35 + '┬─' + '─' * 5 + '─┬─' + '─' * 9 + '┐')
    print(f'│ {"Devices": <10}│ {"OUI": <35}│ {"%": <5} │ {"% of OUI": <9}│')
    for x in reversed(sorted(mostLines.rows(ll.splitlines(), 1))):
        line = f'│ {x[0]: <10}│ {x[1]: <35}│ {x[2]: <5} │ {round(x[0] / res.count(x[1]) * 100, 2): <9}│'
        print('├─' + '─' * 10 + '┼─' + '─' * 35 + '┼─' + '─' * 5 + '─┼─' + '─' * 9 + '┤')
        print(line)
    print('└─' + '─' * 10 + '┴─' + '─' * 35 + '┴─' + '─' * 5 + '─┴─' + '─' * 9 + '┘')
else:
    print('No responses found. Either no devices probed for your SSID(s),'
          ' or deanonymize.py did not run during the capture.')

print('\nDone in: {}s'.format(round(time.time() - before, 2)))
