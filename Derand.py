import csv
import time as timer
from math import log10
import os
import subprocess
import datetime
import pandas as pd
from MACresolver import get_macs
#import GUI

capsDir = './cap/'
MaxAV = -99
showAppl = False
flags = ''
MaxDb = "-99"
cap = "1dec"
dname = "derand"
eq1, eq2, eq3 = 60, 60, 60
capSize = 0

# OLD TSHARK COMMAND
# wlan.sa_resolved contains "Apple" || (not wlan.sa_resolved contains "_" && wlan.fc.type_subtype == 4)
#f'-Y "wlan.sa_resolved contains "Apple" || (not wlan.sa_resolved contains "_" && wlan.fc.type_subtype == 4)" -T fields '
#                             f'-e wlan.sa_resolved -e wlan.seq -e frame.time_epoch -e wlan_radio.signal_dbm -e wlan.tag.length

def makeDlist():
    global p
    # global capSize
    p = 1
    if not os.path.isfile(f'./Derand/{cap}.xls'):
        #41s per 100MB
        p = subprocess.Popen(f'"C:/Program Files/Wireshark/tshark.exe" -r {capsDir}{cap}.cap ' +
                             f'-Y "wlan.fc.type_subtype == 4 and wlan.tag.oui == 0x0017f2" -T fields '
                             f'-e wlan.sa -e wlan.seq -e frame.time_epoch -e wlan_radio.signal_dbm -e wlan.ds.current_channel '
                             f'-e wlan.extcap -e wlan.ht.capabilities -e wlan.ht.ampduparam -e wlan.tag.vendor.data -e wlan.ht.mcsset.rxbitmask.8to15 '
                             f'-e wlan.tag.vendor.oui.type > ./Derand/{cap}.xls', shell=True)
        #openShark()
    try:
        return os.path.getsize(capsDir + '%s.cap' % cap) >> 20
    except FileNotFoundError:
        return


def openShark():
    if os.path.exists(f'./Derand/{cap}.xls'):
        with open(f'./Derand/{cap}.xls', 'r') as d:
            reader = csv.reader(d, delimiter='\t')
            dlist = list(reader)
        return dlist


class RequestPacket(object):
    frames = []

    with open('./create_ouis.csv', 'r', encoding='utf-8') as f:
        dd = f.readlines()
        ouis = dict()
        for line in dd:
            entry = line.split('\t')
            ouis[entry[0]] = entry[1]

    frame_count = {}
    frame_num = 1
    start_frame = None

    def __init__(self, mac, seq, epoch, dbm, ch, ext_cap, ht_cap, ampduparam, vendor_data, rbitmask_8to15, vendor_oui_type):
        self.frames.append(self)
        self.mac = mac.lower()
        self.seq = int(seq)
        self.epoch = float(epoch)
        self.dbm = int(dbm)
        self.ch = ch
        self.ext_cap = ext_cap
        self.ht_cap = ht_cap
        self.ampduparam = ampduparam
        self.vendor_data = vendor_data
        self.rbitmask_8to15 = rbitmask_8to15
        self.vendor_oui_type = vendor_oui_type
        self.resolve = self.resolve_mac(self.mac)
        if self.mac[1] in [2, 6, 'a', 'e']:
            self.isRandom = True
        else:
            self.isRandom = True
        if self.mac in RequestPacket.frame_count:
            RequestPacket.frame_count[self.mac] += 1
        else:
            RequestPacket.frame_count[self.mac] = 1
        self.frame_num = self.frame_num
        RequestPacket.frame_num += 1
        # set the first frame of MAC
        # if mac == MAC and not RequestPacket.start_frame:
        #     RequestPacket.start_frame = self
    @staticmethod
    def boundaries(mac, reverse=False) -> object:
        # mac = self.mac
        if reverse:
            frames = reversed(RequestPacket.frames)
        else:
            frames = RequestPacket.frames

        for frame in frames:
            if frame.mac == mac:
                return frame

    def __repr__(self):
        return [self.mac, self.seq, self.epoch, self.dbm, self.ch]

    def __str__(self):
        return f'{self.mac}\t{self.seq}\t{self.epoch}\t{self.dbm}\t{self.ch}'

    @staticmethod
    def get_av_dbm():
        avlist = [['', 1]]
        packet_count = 2
        over100 = 0
        for dline in sorted(dlist):
            # if not flags:
            #     dline[4] = ''
            if not dline[3]:
                continue
            if 99 + int(dline[3]) <= 0:  # if dbm <= 99
                over100 += 1
            if dline[0] != avlist[-1][0] and 100 + int(dline[3]) > 0:  # if not same mac as previous and <= 99
                avlist[-1][1] = -round(100 - 10 ** (avlist[-1][1] / packet_count))  # get average
                avlist.append([dline[0], log10(100 + int(dline[3]))])
                packet_count = 1

            elif 100 + int(dline[3]) > 0:  # if dbm <= 99
                avlist[-1][1] += float(log10(100 + int(dline[3])))
                packet_count += 1

                if showAppl is True and MAC in avlist[-1][0]:
                    toGUI += toGUI + str(dline) + '\r\n'
                    print(dline)
        avlist[-1][1] = -round(100 - 10 ** (avlist[-1][1] / packet_count))  # get average of last line
        print(avlist)
        return avlist

    def resolve_mac(self, mac):
        if mac[:8] in self.ouis:
            return self.ouis[mac[:8]]


def magic(target_frame):
    exectime = timer.time()
    if not os.path.exists(f'./Derand/{cap}.xls'):
        return 1
    with open(f'./Derand/{cap}.xls', 'r', encoding='utf-8') as d:
        reader = csv.reader(d, delimiter='\t')
        dlist = list(reader)

    Irrlist = set()

    prev_mac = target_frame.mac
    global toGUI
    toGUI = ''; over100 = 0

    # Get average DBm for each MAC
    avdict = {'':1}
    packet_count = 2
    prev = ''
    for dline in sorted(dlist):
        # if not flags:
        #     dline[4] = ''
        if not dline[3]:
            continue
        if 99 + int(dline[3]) <= 0: # if dbm <= 99
            over100 += 1
        if dline[0] != prev and 100 + int(dline[3]) > 0: # if not same mac as previous and <= 99
            avdict[prev] = -round(100 - 10**(avdict[prev] / packet_count)) # get average
            avdict[dline[0]] = log10(100+int(dline[3]))
            prev = dline[0]
            packet_count = 1

        elif 100 + int(dline[3]) > 0: # if dbm <= 99
            avdict[prev] += float(log10(100+int(dline[3])))
            packet_count += 1

            if showAppl is True and target_mac in prev:
                toGUI = toGUI + str(dline) + '\r\n'
                print(dline)
    avdict[prev] = -round(100 - 10 ** (avdict[prev] / packet_count))  # get average of last line
    print(avdict)
    #-------------------------#

    if target_mac in avdict.keys():
        ApplAV = avdict[target_mac]
        print('Target MAC average db', ApplAV)
        if ApplAV < MaxAV:
            return
    for x in dlist: x += [0,0]

    prev_mac = target_frame.mac
    first_seen = RequestPacket.boundaries(target_frame.mac)
    if not first_seen:
        print(f'MAC {target_frame.mac} DOES NOT EXIST')
        return True
    prev_seq, time = first_seen.seq, first_seen.epoch
    fcount = 0
    LastAVdb = ApplAV
    before = list()
    firstMACtime, lastMACtime = 0, 0
    skip = True
    new_mac = False

    for frame in reversed(RequestPacket.frames): #before start
        if frame != first_seen and skip: # jump to start or LastRandMac's first occurrence
            if before and frame.mac != prev_mac:
                Irrlist.add(frame.mac)
            continue
        elif frame == first_seen:
            skip = False

        if frame.mac in Irrlist or (frame.resolve and frame.mac != target_frame.mac):
            continue

        if not (frame.ext_cap == first_seen.ext_cap and frame.ht_cap == first_seen.ht_cap and frame.ampduparam == first_seen.ampduparam
                and frame.vendor_data == first_seen.vendor_data and frame.rbitmask_8to15 == first_seen.rbitmask_8to15):
            Irrlist.add(frame.mac)
            continue

        if frame.mac in avdict.keys():
            macfcount = RequestPacket.frame_count[frame.mac]
        t_delta = time - frame.epoch

        if prev_mac != frame.mac and t_delta < 0.05:
            Irrlist.add(frame.mac)
            continue
        elif t_delta < 560:
            if LastAVdb - avdict[frame.mac] > 5:
                max_sn_delta = eq1
            else:
                max_sn_delta = eq1
        else:
            break

        if frame.seq <= prev_seq:
            sn_delta = prev_seq - frame.seq
        else:
            sn_delta = 4096 - prev_seq + frame.seq

        if prev_mac != frame.mac and t_delta < 0.05:
            Irrlist.add(frame.mac)
            continue

        # if seq within range, or it's the same as last or target MAC
        if sn_delta <= max_sn_delta or (prev_mac == frame.mac) or (frame.mac == target_frame.mac):

            human_time = datetime.datetime.fromtimestamp(frame.epoch).strftime("%H:%M:%S.%f")
            before.append([frame.mac, frame.seq, human_time, frame.dbm, round(t_delta, 3), max_sn_delta, sn_delta])

            prev_mac = frame.mac
            LastAVdb = RequestPacket.frame_count[frame.mac]
            prev_seq, time = frame.seq, frame.epoch
            fcount += macfcount
            if len(before) == 1:
                lastMACtime = frame.epoch
            firstMACtime = frame.epoch

            # Find first seen of this MAC
            first_seen = RequestPacket.boundaries(frame.mac)

        else: Irrlist.add(frame.mac)

    before = before[::-1]

    pd.set_option('expand_frame_repr', False)
    before = pd.DataFrame(before)
    pd.set_option('display.max_rows', len(before))
    before.rename(
        columns={0: 'MAC', 1: 'SN', 2: 'Time', 3: 'dBm', 4: 'Time-Delta', 5: 'Max Delta', 6: 'SN-Delta', 7: 'Max'}, inplace=True)
    print(before)
    toGUI += '\r\n' + str(before)

    out = '\r\n'
    out += '{}{}{}'.format('ignored over -99 frames: ', str(over100), '\r\n')
    out += '{}{}{}'.format('number of frames: ', str(fcount), '\r\n')
    out += '{}{}{}'.format('irrelevant MACs: ', str(len(Irrlist)), '\r\n')
    #out += '{}{}{}'.format('output lines: ', str(len(before)), '\r\n')

    #out = out.join(['output lines: ', str(len(before)), '\r\n'])
    if len(before):
        out += '{}{}{}{}'.format(timer.strftime('%H:%M:%S', timer.localtime(firstMACtime)), ' - ', timer.strftime('%H:%M:%S', timer.localtime(lastMACtime)), '\r\n')

    if target_mac in Irrlist:
        print('<<<DESIGNATED IS IN IRRLIST>>>')
        for line in Irrlist:
            print(line)
    out += "-------------------------------------------------------------------" + '\r\n'
    out += timer.strftime('%H:%M:%S', timer.localtime(first_seen.epoch)) + '\r\n'
    out += str(target_frame) + '\r\n'
    out += "-------------------------------------------------------------------" + '\r\n'
    print(out)
    toGUI += out

    last_seen = RequestPacket.boundaries(target_frame.mac, reverse=True)
    prev_mac = last_seen.mac
    prev_seq, time = last_seen.seq, last_seen.epoch
    after = list()
    firstMACtime = 0; lastMACtime = 0
    i = 0; f = 0; fcount = 0; LastAVdb = ApplAV
    skip = True

    for frame in RequestPacket.frames: #after start
        if frame != last_seen and skip: # jump to start or prev_mac's first occurrence
            if after and frame.mac != prev_mac:
                Irrlist.add(frame.mac)
            continue
        else:
            skip = False

        if frame.mac in Irrlist or (frame.resolve and frame.mac != target_frame.mac):
            continue

        if not (frame.ext_cap == first_seen.ext_cap and frame.ht_cap == first_seen.ht_cap and frame.ampduparam == first_seen.ampduparam
                and frame.vendor_data == first_seen.vendor_data and frame.rbitmask_8to15 == first_seen.rbitmask_8to15):
            Irrlist.add(frame.mac)
            continue

        if frame.mac in avdict.keys():
            macfcount = RequestPacket.frame_count[frame.mac]
        t_delta = frame.epoch - time

        if prev_mac != frame.mac and t_delta < 0.05:
            Irrlist.add(frame.mac)
            continue
        elif t_delta < 560:
            if LastAVdb - RequestPacket.frame_count[frame.mac] > 4:
                max_sn_delta = eq1
            else:
                max_sn_delta = eq1
        else:
            break

        if frame.seq >= prev_seq:
            sn_delta = frame.seq - prev_seq
        else:
            sn_delta = 4096 - prev_seq + frame.seq

        # if seq within range, or it's the same as last or target MAC
        if sn_delta <= max_sn_delta or (prev_mac == frame.mac) or (frame.mac == target_frame.mac):

            human_time = datetime.datetime.fromtimestamp(frame.epoch).strftime("%H:%M:%S.%f")
            after.append([frame.mac, frame.seq, human_time, frame.dbm, round(t_delta, 3), max_sn_delta, sn_delta])

            prev_mac = frame.mac
            # LastDb = int(dline[3])
            prev_seq = frame.seq
            time = float(frame.epoch)

            fcount += macfcount
            if len(after) == 1:
                firstMACtime = frame.epoch
            lastMACtime = frame.epoch

            last_seen = RequestPacket.boundaries(frame.mac, reverse=True)
            # SN = last_seen.seq
            # time = last_seen.epoch
            # count = RequestPacket.frame_count[frame.mac]
            # firstMACtime = last_seen.epoch
            # if str(f) not in after[-1]:
            #     after.append(str(f))# + ['-', '-', '-', '-'])  # avoid double printing
            # break

        else: Irrlist.add(frame.mac)

    out = ''
    if len(after):
        aftertime = timer.strftime('%H:%M:%S', timer.localtime(firstMACtime)) + ' - ' + timer.strftime('%H:%M:%S', timer.localtime(lastMACtime))
        toGUI += aftertime
        print(aftertime)
    # for line in after:
        #line[2] = timer.strftime('%H:%M:%S.%f', timer.localtime(float(line[2])))
        # line[2] = datetime.datetime.fromtimestamp(frame.epoch).strftime("%H:%M:%S.%f")
        #print(line)
        #toGUI += '\r\n' + str(line)

    pd.set_option('expand_frame_repr', False)
    after = pd.DataFrame(after)
    pd.set_option('display.max_rows', len(after))
    after.rename(
        columns={0: 'MAC', 1: 'SN', 2: 'Time', 3: 'dBm', 4: 'Time-Delta', 5: 'Max-Delta', 6: 'SN-Delta', 7: 'Max'}, inplace=True)
    print(after)
    toGUI += '\r\n' + str(after)

    print()
    out += '{}{}{}'.format('number of frames: ', str(fcount), '\r\n')
    out += '{}{}{}'.format('num. of ignored MACS: ', str(len(Irrlist)), '\r\n')
    out += '{}{}{}{}{}'.format('searched lines: ', str(i), ' out of ', str(len(RequestPacket.frames)), '\r\n')
    out += '{}{}{}'.format('Derandomized frames ', str(len(after)), '\r\n')
    out += '{}{}{}'.format('Unique MAC addresses: ', str(len(avdict)), '\r\n')
    out += '{}{}{}{}'.format('Processing time: ', str(round(timer.time() - exectime, 2)), 's', '\r\n')
    out += '{}{}'.format('-------------------------------------------------------------------', '\r\n')
    print(out)
    toGUI += '\r\n' + out
    if target_mac in Irrlist:
        print('<<<DESIGNATED IS IN IRRLIST>>>')

if __name__ == "__main__":
    makeDlist()
    dlist = openShark()
    print(dlist[0])
    frames = [None] * len(dlist)
    target_mac = 'e8:36:17:0d:34:63'
    for num, line in enumerate(dlist):
        frames[num] = RequestPacket(*line)

    target_frame = RequestPacket.boundaries(target_mac)
    from timeit import Timer
    t = Timer(lambda: magic(target_frame))
    print(t.timeit(number=1))

