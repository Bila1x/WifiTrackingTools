import os
import re
import time
import requests
import json
import glob
import sys
from subprocess import Popen, PIPE

import requests

token = 'aw5uyqzgeezbmqjf65g27h7saviyxx'
user = 'up81pubzck6vdog6zwsew4obx2x7rz'
cap_location = './cap/'
tmp_location = './'
tmp_cap = 'temp.cap'
notify = False

co = None
filename = ''

if len(sys.argv) > 1:
    filename = sys.argv[1]

if not filename:
    fileList = glob.glob(cap_location + '*.cap')
    try:
        filename = max(fileList, key=os.path.getctime)
    except:
        print("couldn't find a cap file, try adding it as an argument")
        quit()
    print(filename)
    del fileList

with open('allouis-no-filters.txt', 'r') as o:
    ouis = o.read()
    ouis = ouis.upper()

with open('MACS', 'r') as m:
    MACS = []
    for line in m.read().splitlines():
        cells = line.split(',')
        MACS.append([cells[0].upper(), cells[1], 0, 0])
    del cells

probes = 0
pcount = 1
lastpcount = 0
totalcount = 0
diff = 10
devices = set()
before = time.time()
FNULL = open(os.devnull, 'w')

# with open(filename, 'rb') as header:
#     head = header.read(24)

f = open(filename, 'rb')
head = f.read(24)
first = False


def sender(mac, name, sa, da, db):
    requests.post('https://api.pushover.net/1/messages.json',
                  headers={'content-type': 'application/json'},
                  data=json.dumps({
                      "token": token,
                      "user": user,
                      "title": mac,
                      "message": '{} - {}/{}/{}'.format(name, sa, da, db)}))


def tshark_fail():
    for i in range(3):
        try:
            requests.post('https://api.pushover.net/1/messages.json',
                          headers={'content-type': 'application/json'},
                          data=json.dumps({
                              "token": token,
                              "user": user,
                              "title": 'Tshark stopped the capture!',
                              "message": '!!!',
                              "sound": 'falling'}))
            break
        except:
            print('failed to warn about Tshark');
            time.sleep(1)


while True:
    # if int(pcount) != 0:
    content = f.read()
    offset = len(content) - content.rfind(b'\x00\x00\x24\x00\x2F\x40\x00\xa0')
    if offset > 0 and content.rfind(b'\x00\x00\x24\x00\x2F\x40\x00\xa0') > 0:
        content = content[:-offset - 16]
        f.seek(f.tell() - offset - 16)
    tcpdump = Popen("tcpdump -qetNn -r - 2>/dev/null", stdin=PIPE, stdout=PIPE, shell=True)
    p = tcpdump.communicate(head + content)[0].decode('ascii').upper()
    pos = f.tell()

    if diff == 0:
        print('no more packets!')
        tshark_fail()
        time.sleep(10)

    pcount = p.count('\n') + pcount
    print(pcount)
    diff = pcount - lastpcount
    timediff = time.time() - before
    before = time.time()

    # packet and probe stats
    file = open(tmp_location + 'index.html', 'w')
    probe = p.count('PROBE')
    probes += probe
    file.write('In {} seconds:\npackets: {} to {}\n{} packets/s. {} probes/s.\n'.format(round(timediff, 2), lastpcount, pcount, int(diff / timediff), int(probe / timediff)))
    lastpcount = pcount
    file.write('\nIn session:\n{}% probes in all packets\n'.format(round(probes * 100 / pcount)))

    # devices stats
    dcount = len(devices)
    dmentions = set(re.findall('A:(..:..:..:..:..:..)', p))
    if dmentions:
        for dmention in dmentions:
            if dmention[:8] in ouis:
                devices.add(dmention)
    file.write('{} devices detected:\n'.format(len(devices)))

    p = p.replace(' TA:', ' SA:')
    p = p.replace(' RA:', ' DA:')

    for mac in MACS:
        DA = p.count("DA:" + mac[0])
        SA = p.count("SA:" + mac[0])
        db = ''
        if SA == 0 and DA == 0:
            continue
        if SA != 0:
            co = re.search('(-..)DBM.*SA:' + mac[0], p)
            if co is not None:
                db = co.group(1) + "dBm"

        mac[2] += SA
        mac[3] += DA

        if notify:
            bsend = time.time()
            try:
                sender(mac[1], mac[0], str(SA), str(DA), db)
                print('sent a match to "{}" in {} seconds'.format(mac[1], round(time.time(), 2) - bsend))
            except:
                print('failed to send notification')
                continue

    for line in MACS:
        if line[2] > 0 or line[3] > 0:
            file.write('{}, {}, Sent:{}, Received:{}'.format(line[0], line[1], line[2], line[3]))
    file.close()
    time.sleep(5)
    print()

