import time
import csv
import subprocess
import io
import os
import glob
from multiprocessing import Pool

cap_dir = r'./cap/'
csv_dir = r'./csv/'
tshark_location = 'C:/Program Files/Wireshark/tshark.exe'
threads = 4
fileList = glob.glob(cap_dir + '*.cap')

def Index(fullpath):
    start_timer = time.time()
    filename = os.path.splitext(os.path.basename(fullpath))[0]
    if os.path.isfile(csv_dir + filename + '.csv'):
        print(fullpath + ' is already indexed')
        return
    print('Indexing {} ...'.format(filename))

    process = subprocess.Popen(tshark_location + r' -r %s -T fields -e "frame.time_epoch" -e "wlan.sa" -e "wlan.da" '
                                                 r'-e "wlan.ta" -e "wlan.ra" -e "wlan.bssid" '
                                                 r'-e "wlan.fixed.capabilities.ess" -e "wlan.rsn.pcs.type" '
                                                 r'-e "wlan.rsn.akms.type" -e "wlan.ds.current_channel" -e "ip.src" '
                                                 r'-e "wlan_radio.signal_dbm" -e "wlan.fixed.capabilities.privacy" '
                                                 r'-e "wlan.ssid"' %fullpath, stdout=subprocess.PIPE)
    out = process.communicate()[0]

    reader = io.BufferedReader(io.BytesIO(out))
    d = io.TextIOWrapper(reader)

    APs = dict()
    stations = dict()
    unknown_yet = set()
    undefined = dict()

    broadcast = 'ff:ff:ff:ff:ff:ff'
    ARP = '00:00:00:00:00:00'

    sh = csv.reader(d, delimiter='\t', quoting=csv.QUOTE_NONE)
    shark = [item for item in sh if len(item) == 14]

    #make APs and stations and unknown lists
    for TIME,SA,DA,TA,RA,BSSID,isAP,pcs,akms,ch,src,dBm,isEnc,SSID in shark:
        if BSSID and BSSID == SA:
            if isEnc == '0':
                Cipher = 'OPN'
            elif pcs == '4,2' or pcs == '2,4':
                Cipher = 'CCMP TKIP'
            elif pcs == '4':
                Cipher = 'CCMP'
            elif pcs == '2':
                Cipher = 'TKIP'
            else:
                Cipher = ''
            if akms == '1':
                auth = 'MGT'
            elif '2' in akms:
                auth = 'PSK'
            else:
                auth = ''
            if SA not in APs or APs[SA] == ['','','','','',0,'',0,'']:
                APs[SA] = ['','',Cipher,auth,ch,0,isEnc,0,SSID]
            if not APs[SA][2] and pcs:
                APs[SA][2] = Cipher
            if not APs[SA][3] and akms:
                APs[SA][3] = auth
            if not APs[SA][4] and ch:
                APs[SA][4] = ch

            if (DA not in stations or stations[DA][4] == 'N/A') and DA != 'ff:ff:ff:ff:ff:ff':
                stations[DA] = ['','',0,0,'N/A',set()]

        elif BSSID and BSSID == DA:
            if DA not in APs and DA != broadcast and DA != ARP:
                APs[DA] = ['','','','','',0,'',0,'']
            if SA not in stations or stations[SA][4] == 'N/A':
                bssid = BSSID
                if BSSID == ARP or BSSID == broadcast:
                    bssid = 'N/A'
                stations[SA] = ['','',0,0,bssid,set()]
        elif BSSID:
            if BSSID not in APs and BSSID != broadcast:
                APs[BSSID] = ['','','','','',0,'',0,'']

            if SA and (SA not in stations or stations[SA][4] == 'N/A'):
                bssid = BSSID
                if BSSID == ARP or BSSID == broadcast:
                    bssid = 'N/A'
                stations[SA] = ['','',0,0,bssid,set()]

            if (DA not in stations or stations[DA][4] == 'N/A') and DA and DA != broadcast and BSSID != broadcast:
                bssid = BSSID
                if BSSID == ARP or BSSID == broadcast:
                    bssid = 'N/A'
                stations[DA] = ['','',0,0,bssid,set()]

        if RA and RA != broadcast and RA != ARP:
            unknown_yet.add(RA)
        if TA and TA != ARP:
            unknown_yet.add(TA)

    if ARP in APs:
        APs.pop(ARP)
    for mac in unknown_yet:
        if mac not in APs and mac not in stations:
            undefined[mac] = ['','',0,0]

    #packet counter and leastDb calculator
    for line in shark:
        if line[3] in stations:
            stations[line[3]][3] += 1
            if line[11] and (stations[line[3]][2] < int(line[11]) or stations[line[3]][2] == 0):
                stations[line[3]][2] = int(line[11])
        if line[3] in APs:
            APs[line[3]][5] += 1
            if line[11] and (APs[line[3]][7] < int(line[11]) or APs[line[3]][7] == 0):
                APs[line[3]][7] = int(line[11])
        if line[3] in undefined:
            undefined[line[3]][3] += 1
            if line[11] and (undefined[line[3]][2] < int(line[11]) or undefined[line[3]][2] == 0):
                undefined[line[3]][2] = int(line[11])

    #get first seen for all lists
    set_errors = 0
    for frame in shark:
        for i in range(1,6):
            if frame[i] in APs and not APs[frame[i]][0] and '-' not in frame[0]:
                APs[frame[i]][0] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(round(float(frame[0]))))
            if frame[i] in stations and not stations[frame[i]][0] and '-' not in frame[0]:
                stations[frame[i]][0] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(round(float(frame[0]))))
            if frame[i] in undefined and not undefined[frame[i]][0] and '-' not in frame[0]:
                undefined[frame[i]][0] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(round(float(frame[0]))))
        if frame[5] and frame[13] and frame[5] == frame[3] and frame[3] != ARP:
            APs[frame[3]][-1] = frame[13]
        if frame[-1] and frame[3] and frame[5] != frame[3] and len(frame[-1]) <= 32:
            try:
                stations[frame[3]][-1].add(frame[-1])
            except:
                set_errors += 1
    if set_errors:
        print('{} set errors occurred!'.format(set_errors))

    # get last seen for all lists
    for frame in reversed(shark):
        for i in range(1, 6):
            if frame[i] in APs and not APs[frame[i]][1] and '-' not in frame[0]:
                APs[frame[i]][1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(round(float(frame[0]))))
            if frame[i] in stations and not stations[frame[i]][1] and '-' not in frame[0]:
                stations[frame[i]][1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(round(float(frame[0]))))
            if frame[i] in undefined and not undefined[frame[i]][1] and '-' not in frame[0]:
                undefined[frame[i]][1] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(round(float(frame[0]))))

    print(len(APs), 'APs')
    print(len(stations), 'stations')
    print(len(undefined), 'undefined')

    with open(csv_dir + filename + '.csv', 'w', newline='') as d:
        writer = csv.writer(d, delimiter='\t')
        writer.writerow(['BSSID', 'First seen', 'Last seen', 'Cipher', 'Authentication', 'Channel', 'Packets', 'Least dBm', 'SSID'])
        for key, value in sorted(APs.items(),key=lambda x: (x[1][0], x[1][1], x[0])):
            writer.writerow([key.upper()] + value[:6] + value[7:])

        d.write('\r\n')
        writer.writerow(['Station','First seen','Last seen','Least dBm','Packets','BSSID','Probed SSIDs'])
        for key, value in sorted(stations.items(),key=lambda x: (x[1][0], x[1][1], x[0])):
            if value[5]:
                writer.writerow([key.upper()] + value[0:4] + [value[4].upper()] + [", ".join(sorted(value[5]))])
            else:
                writer.writerow([key.upper()] + value[0:4] + [value[4].upper()])
        d.write('\r\n')
        writer.writerow(['Undefined', 'First seen', 'Last seen', 'Least dBm', 'Packets'])
        for key, value in sorted(undefined.items(), key=lambda x: (x[1][0], x[1][1], x[0])):
            writer.writerow([key.upper()] + value)

    print('Processed {} in {} seconds'.format(filename, time.time() - start_timer))

if __name__ == '__main__':
    print('started indexing {} cap file(s):\n{}\n'.format(len(fileList), fileList))
    p = Pool(threads)
    result = p.map(Index, fileList)
    p.close()
    p.join()
