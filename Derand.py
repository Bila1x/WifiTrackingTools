import csv
import time as timer
from math import log10
#from PyQt4 import QtGui
import sys
import os
import subprocess
import datetime
import pandas as pd
#import GUI

capsDir = 'C:\\Users\\Bilal\\Desktop\\whereabouts\\'
MaxAV = -99
#MaxSNgap = 240
# flags = dlist[start - 1][4]
showAppl = False
flags = ''
MaxDb = "-99"
cap = "6oct"
dname = "Derand-17sep"
global MAC
MAC = 'Apple_d2:f1:53'.lower()
global start
start = 4924  # 8379
isStartFound = False
eq1 = 26; eq2 = 50; eq3 = 60

def makeDlist():
    global p
    global capSize
    p = 1
    try:
        capSize = os.path.getsize(r'C:\Users\Bilal\Desktop\whereabouts\%s.cap' % cap) >> 20
    except FileNotFoundError:
        capSize = 0
        return

    if os.path.isfile(r'C:\Users\Bilal\Desktop\whereabouts\scripts\Derand\%s.xls' % dname) == False:
        #41s per 100MB
        p = subprocess.Popen(r'"c:\Program Files\Wireshark\tshark.exe" -r ' + capsDir + cap + '.cap -Y "wlan.sa_resolved contains "Apple" || (not wlan.sa_resolved contains "_" && wlan.fc.type_subtype == 4)" -T fields -e wlan.sa_resolved -e wlan.seq -e frame.time_epoch -e wlan_radio.signal_dbm -e wlan.tag.length > Derand\Derand-' + cap + '.xls', shell=True)
        #openShark()

def openShark():
    try:
        with open(r'C:\Users\Bilal\Desktop\whereabouts\scripts\Derand\%s.xls' % dname, 'r') as d:
            global dlist
            reader = csv.reader(d, delimiter='\t')
            dlist = list(reader)
            #for line in dlist:
                #line[2] = timer.strftime('%H:%M:%S', timer.localtime(float(line[2])))
            #dlist = str(dlist)
    except FileNotFoundError:
        capSize = 0
        return

def magic():
    exectime = timer.time()

    with open(r'C:\Users\Bilal\Desktop\whereabouts\scripts\Derand\%s.xls' % dname, 'r') as d:
        reader = csv.reader(d, delimiter='\t')
        dlist = list(reader)

    Irrlist = set()
    z = 0
    global start; global isStartFound
    for line in dlist:
        z += 1
        if line[0].lower() == MAC:
            start = z
            isStartFound = True
            break
    if not isStartFound: print('MAC DOES NOT EXIST')
    #flags = dlist[start - 1][4]

    LastRandMac = dlist[start - 1][0]
    Designated = LastRandMac
    global before; global after; global toGUI
    toGUI = ''; over100 = 0

    #-----average db get------#
    avlist = list(); avlist.append(['',1,2])

    for dline in sorted(dlist):
        if not flags: dline[4] = ''
        if dline[3] and 99 + int(dline[3]) <= 0:
            over100 += 1
        if dline[3] != '' and dline[0] != avlist[-1][0] and 100 + int(dline[3]) > 0:
            avlist[-1][1] = -round(100 - 10**(avlist[-1][1]/avlist[-1][2])) # get average
            avlist.append([dline[0],log10(100+int(dline[3])),1])
        else:
            if dline[3] == '':
                continue
            if 100 + int(dline[3]) > 0:
                avlist[-1][1] += float(log10(100+int(dline[3])))
                avlist[-1][2] += 1
                if showAppl is True and Designated in avlist[-1][0]:
                    toGUI = toGUI + str(dline) + '\r\n'
                    print(dline)
    avlist[-1][1] = -round(100 - 10 ** (avlist[-1][1] / avlist[-1][2]))  # get average of last line
    #-------------------------#

    for avline in avlist:
        if Designated == avline[0]:
            ApplAV = avline[1]
            print('Designated MAC average db', ApplAV)
            if ApplAV < MaxAV:
                return
        if avline[1] < MaxAV: Irrlist.add(avline[0])
    for x in dlist: x += [0,0]

    MACfirstseen = start; SN = int(dlist[start - 1][1]); time = float(dlist[start - 1][2])
    i = 0; f = 0; fcount = 0; LastAVdb = ApplAV
    before = list()
    firstMACtime = 0; lastMACtime = 0

    for dline in reversed(dlist): #before start
        i+=1
        if i <= len(dlist) - MACfirstseen + 1: # jump to start or LastRandMac's first occurrence
            if before and dline[0] != LastRandMac:
                Irrlist.add(dline[0])
            continue

        if dline[0] not in Irrlist:
            if str(dline[4]) == str(flags) or 'Apple' in dline[0] or dline[0] == Designated:
                for avline in avlist:
                    if avline[0] == dline[0]:
                        dline[5] = avline[1]; macfcount = avline[2]
                        break
                delta = time - float(dline[2])

                if delta < 0.3 and LastRandMac != dline[0]:
                    Irrlist.add(dline[0])
                    continue
                elif delta < 3.8:
                    Max = eq1; eq = "1"
                elif delta < 11.4:
                    if LastAVdb - dline[5] > 3: Max = -30
                    else: Max = -eq2
                    eq = "2"
                elif delta < 360:
                    if LastAVdb - dline[5] > 5: Max = -80
                    else: Max = -eq3
                    eq = "3"
                else:
                    break

                #if (int(dline[3]) <= int(MaxDb)): # or (SN - int(dline[1]) > MaxSNgap):
                    #Irrlist.add(dline[0])
                    #continue

                if ((int(dline[1]) < SN) and (int(dline[1]) >= (SN + Max))) or (4096 + SN - int(dline[1]) <= -Max) or (LastRandMac == dline[0]) or (Designated == dline[0]): #if SN within range or it's the same last MAC

                    #before.append(str(dline) + "\t" + str(round(delta, 3)) + "\t" + str(Max) + "\t" + eq + "\t" + str(SN - int(dline[1])))
                    before.append(dline + [str(round(delta, 3)), str(Max), eq, str(SN - int(dline[1]))])

                    LastRandMac = dline[0]; LastAVdb = dline[5]; SN = int(dline[1]); time = float(dline[2])
                    fcount += macfcount
                    if len(before) == 1: lastMACtime = float(dline[2])
                    firstMACtime = float(dline[2])

                    for first in dlist: #get mac first seen in list
                        f += 1
                        if first[0] == dline[0]: # update stuff when mac first seen is found
                            MACfirstseen = f; SN = int(first[1]); time = float(first[2]); first[5] = dline[5]; firstMACtime = float(first[2])
                            if first not in before[-1]: before.append(first + ['-', '-', '-', '-']) #avoid double printing
                            f = 0
                            break
                else: Irrlist.add(dline[0])
            else: Irrlist.add(dline[0])

    before = before[::-1]

    for line in before:
        #line[2] = timer.strftime('%H:%M:%S.%f', timer.localtime(float(line[2])))
        line[2] = datetime.datetime.fromtimestamp(float(line[2])).strftime("%H:%M:%S.%f")
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
    out += timer.strftime('%H:%M:%S', timer.localtime(float(dlist[start - 1][2]))) + '\r\n'
    out += str(dlist[start - 1]) + '\r\n'
    out += "-------------------------------------------------------------------" + '\r\n'
    print(out)
    toGUI += out

    MACfirstseen = start; LastRandMac = dlist[start - 1][0]; SN = int(dlist[start - 1][1]); time = float(dlist[start - 1][2])
    after = list()
    firstMACtime = 0; lastMACtime = 0
    i = 0; f = 0; fcount = 0; LastAVdb = ApplAV

    for dline in dlist: #after start
        i+=1
        if i <= MACfirstseen: # jump to start or LastRandMac's first occurrence
            if after and dline[0] != LastRandMac:
                Irrlist.add(dline[0])
            continue

        if dline[0] not in Irrlist:
            if str(dline[4]) == str(flags) or 'Apple' in dline[0] or dline[0] == Designated:
                for avline in avlist:
                    if avline[0] == dline[0]:
                        dline[5] = avline[1]; macfcount = avline[2]
                        break
                delta = float(dline[2]) - time

                if delta < 0.3 and LastRandMac != dline[0]:
                    Irrlist.add(dline[0])
                    continue
                elif delta < 3.8:
                    Max = eq1; eq = "1"
                elif delta < 11.4:
                    if LastAVdb - dline[5] > 4: Max = (30)
                    else: Max = eq2
                    eq = "2"
                elif delta < 360:
                    if LastAVdb - dline[5] > 4: Max = (70)
                    else: Max = eq3
                    eq = "3"
                else:
                    break

                #if (int(dline[3]) <= int(MaxDb)): # or (int(dline[1]) - SN > MaxSNgap):
                    #Irrlist.add(dline[0])
                    #continue
                if ((int(dline[1]) > SN) and (int(dline[1]) <= (SN + Max))) or (4096 - SN + int(dline[1]) <= Max) or (LastRandMac == dline[0]) or (Designated == dline[0]): #if SN within range or it's the same last MAC

                    #after.append(str(dline) + "\t" + str(round(delta, 3)) + "\t" + str(Max) + "\t" + eq + "\t" + str(int(dline[1]) - SN))
                    after.append(dline + [str(round(delta, 3)), str(Max), eq, str(int(dline[1]) - SN)])

                    LastRandMac = dline[0]; LastDb = int(dline[3]); SN = int(dline[1]); time = float(dline[2])
                    fcount += macfcount
                    if len(after) == 1: firstMACtime = float(dline[2])
                    lastMACtime = float(dline[2])

                    for last in reversed(dlist): #get mac last seen in list
                        f += 1
                        if last[0] == dline[0]:
                            MACfirstseen = len(dlist) - f + 1; SN = int(last[1]); time = float(last[2]); last[5] = dline[5]; lastMACtime = float(last[2])
                            #after.append(str(last) + "\t" + str(round(delta, 3)) + "\t" + str(round(Max)) + "\t" + eq)
                            if last not in after[-1]: after.append(last + ['-', '-', '-', '-'])  # avoid double printing
                            f = 0
                            break
                else: Irrlist.add(dline[0])
            else: Irrlist.add(dline[0])

    out = ''
    if len(after):
        aftertime = timer.strftime('%H:%M:%S', timer.localtime(firstMACtime)) + ' - ' + timer.strftime('%H:%M:%S', timer.localtime(lastMACtime))
        toGUI += aftertime
        print(aftertime)
    for line in after:
        #line[2] = timer.strftime('%H:%M:%S.%f', timer.localtime(float(line[2])))
        line[2] = datetime.datetime.fromtimestamp(float(line[2])).strftime("%H:%M:%S.%f")
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
    out += '{}{}{}'.format('Average list length ', str(len(avlist)), '\r\n')
    out += '{}{}{}{}'.format('in ', str(round(timer.time() - exectime, 2)), ' seconds', '\r\n')
    out += '{}{}'.format('-------------------------------------------------------------------', '\r\n')
    print(out)
    toGUI += '\r\n' + out
    if Designated in Irrlist:
        print('<<<DESIGNATED IS IN IRRLIST>>>')

if __name__ == "__main__":
    from timeit import Timer
    t = Timer(lambda: magic())
    print(t.timeit(number=1))