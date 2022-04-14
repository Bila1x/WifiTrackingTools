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
#MaxSNgap = 240
# flags = dlist[start - 1][4]
showAppl = False
flags = ''
MaxDb = "-99"
cap = "1dec"
dname = "derand"
global MAC
MAC = '6c:8d:c1:38:7b:2c'.lower()
# global start
# start = 4924  # 8379
# isStartFound = False
eq1 = 40; eq2 = 191; eq3 = 60
capSize = 0
toGUI = ''

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


# class IterFrames(type):
#     def __iter__(cls):
#         return iter(cls._frames)


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
        if self.mac in RequestPacket.frame_count:
            RequestPacket.frame_count[self.mac] += 1
        else:
            RequestPacket.frame_count[self.mac] = 1
        self.frame_num = self.frame_num
        RequestPacket.frame_num += 1
        # set the first frame of MAC
        if mac == MAC and not RequestPacket.start_frame:
            RequestPacket.start_frame = self

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


def magic():
    exectime = timer.time()
    if not os.path.exists(f'./Derand/{cap}.xls'):
        return 1
    with open(f'./Derand/{cap}.xls', 'r', encoding='utf-8') as d:
        reader = csv.reader(d, delimiter='\t')
        dlist = list(reader)

    Irrlist = set()

    # LastRandMac = dlist[start - 1][0]
    LastRandMac = MAC
    Designated = LastRandMac
    global before; global after; global toGUI
    toGUI = ''; over100 = 0

    # Get average DBm for each MAC
    avlist = [['', 1]]
    avdict = {'':1}
    prev = ''
    dbm = 1
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

            if showAppl is True and Designated in prev:
                toGUI = toGUI + str(dline) + '\r\n'
                print(dline)
    avdict[prev] = -round(100 - 10 ** (avdict[prev] / packet_count))  # get average of last line
    print(avdict)

    # print(avdict)
    # avlist = RequestPacket.get_av_dbm()
    print(dlist[0])
    #-------------------------#

    if Designated in avdict.keys():
        ApplAV = avdict[Designated]
        print('Designated MAC average db', ApplAV)
        if ApplAV < MaxAV:
            return
    for x in dlist: x += [0,0]

    MACfirstseen = MAC
    first_seen = RequestPacket.start_frame
    if not first_seen:
        print('MAC DOES NOT EXIST')
        return True
    SN = int(first_seen.seq)
    time = float(first_seen.epoch)
    i, fcount = 0, 0
    LastAVdb = ApplAV
    before = list()
    firstMACtime = 0
    lastMACtime = 0
    started = False

    for frame in reversed(RequestPacket.frames): #before start
        # i += 1
        if not started and not (frame == first_seen or frame == RequestPacket.start_frame): # jump to start or LastRandMac's first occurrence
            started = True
            if before and frame.mac != LastRandMac:
                Irrlist.add(frame.mac)
            continue

        if frame.mac in Irrlist:
            continue

        # print([frame.ext_cap ,  first_seen.ext_cap ,  frame.ht_cap ,  first_seen.ht_cap ,  frame.ampduparam ,  first_seen.ampduparam
        # ,  frame.vendor_data ,  first_seen.vendor_data ,  frame.rbitmask_8to15 ,  first_seen.rbitmask_8to15
        # ])

        if not (frame.ext_cap == first_seen.ext_cap and frame.ht_cap == first_seen.ht_cap and frame.ampduparam == first_seen.ampduparam
                and frame.vendor_data == first_seen.vendor_data and frame.rbitmask_8to15 == first_seen.rbitmask_8to15):
            Irrlist.add(frame.mac)
            continue

        if frame.mac in avdict.keys():
            macfcount = RequestPacket.frame_count[frame.mac]
        delta = time - float(frame.epoch)

        if delta < 0.3 and LastRandMac != frame.mac:
            Irrlist.add(frame.mac)
            continue
        elif delta < 3.8:
            Max = eq1; eq = "1"
        elif delta < 11.4:
            if LastAVdb - avdict[frame.mac] > 3: Max = -30
            else: Max = -eq2
            eq = "2"
        elif delta < 360:
            if LastAVdb - avdict[frame.mac] > 5: Max = -80
            else: Max = -eq3
            eq = "3"
        else:
            break

        if ((frame.seq < SN) and (frame.seq >= (SN + Max)))\
                or (4096 + SN - frame.seq <= -Max) or (LastRandMac == frame.mac)\
                or (Designated == frame.mac): #if SN within range or it's the same last MAC

            human_time = datetime.datetime.fromtimestamp(frame.epoch).strftime("%H:%M:%S.%f")
            before.append([frame.mac, frame.seq, human_time, frame.dbm, str(round(delta, 3)), str(Max), eq, str(SN - frame.seq)])

            LastRandMac = frame.mac
            LastAVdb = RequestPacket.frame_count[frame.mac]
            SN = frame.seq
            time = frame.epoch
            fcount += macfcount
            if len(before) == 1:
                lastMACtime = frame.epoch
            firstMACtime = frame.epoch

            # for first in dlist: #get mac first seen in list
            #     f += 1
            #     if first[0] == dline[0]: # update stuff when mac first seen is found
            #         MACfirstseen = f
            #         SN = int(first[1])
            #         time = float(first[2])
            #         first[5] = RequestPacket.frame_count[dline[0]]
            #         firstMACtime = float(first[2])
            #         if first not in before[-1]: before.append(first + ['-', '-', '-', '-']) #avoid double printing
            #         f = 0
            #         break

            # Find first seen of this MAC
            for f in frames:
                if f == frame:
                    started = False
                    first_seen = f
                    SN = f.seq
                    time = f.epoch
                    count = RequestPacket.frame_count[frame.mac]
                    firstMACtime = f.epoch
                    # if str(f) not in before[-1]: before.append(str(f))# + ['-', '-', '-', '-'])  # avoid double printing
                    break

        else: Irrlist.add(frame.mac)

    before = before[::-1]

    # for line in before:
    #     #line[2] = timer.strftime('%H:%M:%S.%f', timer.localtime(float(line[2])))
    #     line[2] = datetime.datetime.fromtimestamp(frame.epoch).strftime("%H:%M:%S.%f")
        #print(line)
        #toGUI += '\r\n' + str(line)

    pd.set_option('expand_frame_repr', False)
    before = pd.DataFrame(before)
    pd.set_option('display.max_rows', len(before))
    before.rename(
        columns={0: 'MAC', 1: 'SN', 2: 'Time', 3: 'dBm', 4: 'Flags', 5: 'AVdb', 6: '0', 7: 'Delta', 8: 'Max',
                 9: 'eq', 10: 'SN delta', }, inplace=True)
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

    if Designated in Irrlist:
        print('<<<DESIGNATED IS IN IRRLIST>>>')
        for line in Irrlist:
            print(line)
    out += "-------------------------------------------------------------------" + '\r\n'
    out += timer.strftime('%H:%M:%S', timer.localtime(first_seen.epoch)) + '\r\n'
    out += str(first_seen) + '\r\n'
    out += "-------------------------------------------------------------------" + '\r\n'
    print(out)
    toGUI += out

    MACfirstseen = MAC
    LastRandMac = first_seen.mac
    SN = first_seen.seq
    time = first_seen.epoch
    after = list()
    firstMACtime = 0; lastMACtime = 0
    i = 0; f = 0; fcount = 0; LastAVdb = ApplAV
    started = False

    for frame in RequestPacket.frames: #after start
        # i+=1
        if not started and not (frame == first_seen or frame == RequestPacket.start_frame): # jump to start or LastRandMac's first occurrence
            started = True
            if after and frame.mac != LastRandMac:
                Irrlist.add(frame.mac)
            continue

        if frame.mac in Irrlist:
            continue

        # if 'Apple' in frame.mac or frame.mac == Designated:
        # for avline in avlist:
        #     if avline[0] == dline[0]:
        #         dline[5] = avline[1];# macfcount = avline[2]
        #         macfcount = RequestPacket.frame_count[dline[0]]
        #         break
        if frame.mac in avdict.keys():
            macfcount = RequestPacket.frame_count[frame.mac]
        delta = frame.epoch - time

        if delta < 0.3 and LastRandMac != frame.mac:
            Irrlist.add(frame.mac)
            continue
        elif delta < 3.8:
            Max = eq1; eq = "1"
        elif delta < 11.4:
            if LastAVdb - RequestPacket.frame_count[frame.mac] > 4: Max = (30)
            else: Max = eq2
            eq = "2"
        elif delta < 360:
            if LastAVdb - RequestPacket.frame_count[frame.mac] > 4: Max = (70)
            else: Max = eq3
            eq = "3"
        else:
            break

                #if (int(dline[3]) <= int(MaxDb)): # or (int(dline[1]) - SN > MaxSNgap):
                    #Irrlist.add(dline[0])
                    #continue
        if ((frame.seq > SN) and (frame.seq <= (SN + Max))) or (4096 - SN + frame.seq <= Max) or (LastRandMac == frame.mac) or (Designated == frame.mac): #if SN within range or it's the same last MAC

            human_time = datetime.datetime.fromtimestamp(frame.epoch).strftime("%H:%M:%S.%f")
            after.append([frame.mac, frame.seq, human_time, frame.dbm, str(round(delta, 3)), str(Max), eq, str(frame.seq - SN)])

            LastRandMac = frame.mac
            # LastDb = int(dline[3])
            SN = frame.seq
            time = float(frame.epoch)

            fcount += macfcount
            if len(after) == 1:
                firstMACtime = frame.epoch
            lastMACtime = frame.epoch

            # for last in reversed(dlist): #get mac last seen in list
            #     f += 1
            #     if last[0] == frame.mac:
            #         MACfirstseen = len(dlist) - f + 1; SN = int(last[1]); time = float(last[2]); last[5] = RequestPacket.frame_count[frame.mac]; lastMACtime = float(last[2])
            #         #after.append(str(last) + "\t" + str(round(delta, 3)) + "\t" + str(round(Max)) + "\t" + eq)
            #         if last not in after[-1]: after.append(last + ['-', '-', '-', '-'])  # avoid double printing
            #         f = 0
            #         break

            for f in reversed(frames):
                if f == frame:
                    started = False
                    first_seen = f
                    SN = f.seq
                    time = f.epoch
                    count = RequestPacket.frame_count[frame.mac]
                    firstMACtime = f.epoch
                    # if str(f) not in after[-1]:
                    #     after.append(str(f))# + ['-', '-', '-', '-'])  # avoid double printing
                    break

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
        columns={0: 'MAC', 1: 'SN', 2: 'Time', 3: 'dBm', 4: 'Flags', 5: 'AVdb', 6: '0', 7: 'Delta', 8: 'Max',
                 9: 'eq', 10: 'SN delta', }, inplace=True)
    print(after)
    toGUI += '\r\n' + str(after)

    print()
    out += '{}{}{}'.format('number of frames: ', str(fcount), '\r\n')
    out += '{}{}{}'.format('num. of ignored MACS ', str(len(Irrlist)), '\r\n')
    #out += '{}{}{}'.format('output lines ', str(len(after)), '\r\n')
    out += '{}{}{}{}{}'.format('searched lines ', str(i), ' out of ', str(len(dlist)), '\r\n')
    out += '{}{}{}'.format('Average dict length ', str(len(avdict)), '\r\n')
    out += '{}{}{}{}'.format('in ', str(round(timer.time() - exectime, 2)), ' seconds', '\r\n')
    out += '{}{}'.format('-------------------------------------------------------------------', '\r\n')
    print(out)
    toGUI += '\r\n' + out
    if Designated in Irrlist:
        print('<<<DESIGNATED IS IN IRRLIST>>>')

if __name__ == "__main__":
    makeDlist()
    dlist = openShark()
    print(dlist[0])
    frames = [None] * len(dlist)

    for num, line in enumerate(dlist):
        frames[num] = RequestPacket(*line)
    # for a in RequestPacket.frames:
    #     print(1)
    from timeit import Timer
    t = Timer(lambda: magic())
    print(t.timeit(number=1))