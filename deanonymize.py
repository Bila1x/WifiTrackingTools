import multiprocessing

import scapy.layers.dot11
from scapy.all import *
import time
import random

# from monitor_associate import Monitor

class Monitor:
    def __init__(self, mon_ifc, s):
        with open('/home/pi/Apple-lowcase-oui.txt', 'r') as f:
            ouis = f.readlines()
            ouiList = [x.strip() for x in ouis]

        self.ouiList = set(ouiList)
        self.mon_ifc = mon_ifc
        self.s = s
        self.tap = '\x00\x00\x08\x00\x00\x00\x00\x00'
        self.assoc = '\x00\x00\x3a\x01'
        self.assoc = '\x50\x00\x00\x00'
        self.myaddr = '\x22\x22\x22\x22\x22\x22'
        self.caps = '\x31\x06\x05\x00'
        self.ht = '\x2d\x1a\xad\x01\x1b\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.fixedparms = '\x00\x00\x00\x00\x00\x00\x00\x00\x64\x00'
        self.ssids = ['OEBB','AndroidAP','eduroam', 'OEBB-station', 'Freewave', 'Wiener Linien Free WiFi', '.wienatPublicWLAN', 'Austrian Free Wifi']
        self.AP = '\x30\x14\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x02\x0c\x00'
        self.RSN = '\x30\x14\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x02\xac\x24'
        self.WF = '\x30\x18\x01\x00\x00\x0f\xac\x02\x02\x00\x00\x0f\xac\x04\x00\x0f\xac\x02\x01\x00\x00\x0f\xac\x01\x00\x00'
        self.ER = '\x30\x14\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x01\x28\x00'
        self.test = '\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x3a\x01\xb4\xf7\xa1\xc0\x8e\xc1\xf0\x8a\x76\x44\xc3\x06\xb4\xf7\xa1\xc0\x8e\xc1\x20\x00\x31\x06\x05\x00\x00\x0a\x42\x69\x6c\x61\x6c\x50\x68\x6f\x6e\x65\x01\x08\x82\x84\x8b\x0c\x12\x96\x18\x24\x32\x04\x30\x48\x60\x6c\x2d\x1a\x2d\x01\x17\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x14\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x02\xac\x24\x7f\x08\x00\x00\x00\x00\x00\x00\x00\x40\xdd\x07\x00\x50\xf2\x02\x00\x01\x00\x3b\x6f\x3a\x74'
        self.OPN = ''
        self.counter = 0
        self.rest = '\x01\x08\x82\x84\x8b\x96\x24\x30\x48\x6c\x32\x04\x0c\x12\x18\x60'

    def SSIDparams(self,randssid):
        return '{:02x}{:02x}{}'.format(0, len(randssid), randssid.encode('hex')).decode('hex')

    def send_packet(self, packet, packet_type=None):
        # seen_sender = packet[Dot11].addr2.replace(':', '').decode('hex')
        seen_sender = packet[Dot11].addr2.replace(':', '').decode('hex')
        # seen_sender = bytearray.fromhex(packet[Dot11].addr2.replace(':', ''))

        ssid = packet.info
        # print(ssid)

        # if seen_sender[:8] == 'da:a1:19'\
        # if '\xdd\x0b\x00\x17\xf2\x0a\x00\x01\x04\x00\x00\x00\x00' in str(packet):
        # str_packet = str(packet)

        # detect probe-req field and broadcast field

        if packet[Dot11].addr3 == 'ff:ff:ff:ff:ff:ff':
            # and seen_sender[:8] in self.ouiList):
            # print(seen_sender, type(seen_sender))
            randssid = self.ssids[0]

            # print(randssid)

            # if self.counter == 4: self.counter = 0
            # else: self.counter += 1
            if randssid == 'AndroidAP': keyType = self.AP; caps = '\x11\x04'
            #elif randssid == 'UPC Wi-Free': keyType = self.WF; caps = '\x11\x04'
            elif randssid == 'eduroam': keyType = self.ER; caps = '\x31\x14'
            else: keyType = self.OPN; caps = '\x21\x04'
            print('caps', caps, self.SSIDparams(ssid))
            #self.adds[1][Dot11].addr1 = seen_sender
            #self.adds[3][Dot11Elt].info = randssid
            #final = self.adds / keyType
            #final = '{}{}{}{}{}{}'.format(self.adds[0], self.adds[1], self.adds[2], self.adds[3], self.adds[4], keyType)
            final = '{}{}{}{}{}{}{}{}{}{}'.format(self.tap, self.assoc, seen_sender, self.myaddr, self.myaddr, '\x00\x00',
                                                  self.fixedparms, caps, self.SSIDparams(randssid), self.rest)
            print(final)
            # final = self.test

            self.s.send(final)
            #print(self.SSIDparams(randssid))
            #print(hexdump(final))

            # print(type(packet.getlayer(Dot11Elt)))
            return '{}ms\t{}\t{}'.format(int((time.time() - packet.time)*1000), randssid, seen_sender)
    # else: print(time.time() - before)
        # print(time.time() - before)
        # self.count += 1
        # self.timer += time.time() - before
        # print((self.timer) / self.count)


    def search_auth(self, mp_queue):
        # print("\nScanning max 5 seconds for Authentication "
        #       "from BSSID {0}".format(self.bssid))
        print('started')
        sniff(iface=self.mon_ifc, filter='type mgt subtype probe-req',
              prn=self.send_packet, store=False)
        # lfilter=lambda x: x.haslayer(Dot11ProbeReq)
        #s.close()
        # mp_queue.put(self.auth_found)

    # def search_assoc_resp(self, mp_queue):
    #     print("\nScanning max 5 seconds for Association Response "
    #           "from BSSID {0}".format(self.bssid))
    #     sniff(iface=self.mon_ifc, lfilter=lambda x: x.haslayer(Dot11AssoResp),
    #           stop_filter=self.check_assoc,
    #           timeout=5)
    #     mp_queue.put(self.assoc_found)

class ConnectionPhase:
    def __init__(self, monitor_ifc, s):
        self.state = "Not Connected"
        self.mon_ifc = monitor_ifc
        # self.sta_mac = sta_mac
        # self.bssid = bssid
        self.s = s

    def send_authentication(self):
        # packet = Dot11ProbeResp(
        #     cap=0x1100) / Dot11Elt(
        #     ID=0, info="{}".format('MACRAN')) / Raw('\x01\x08\x82\x84\x8b\x96\x24\x30\x48\x6c\x03\x01\x06\x2a\x01\x00\x32\x04\x0c\x12\x18\x60\x30\x14\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x02\x0c\x00')

        # packet.show()

        jobs = list()
        result_queue = multiprocessing.Queue()
        receive_process = multiprocessing.Process(
            target=self.mon_ifc.search_auth,
            args=(result_queue,))
        jobs.append(receive_process)
        # send_process = multiprocessing.Process(
        #     target=self.mon_ifc.send_packet,
        #     args=(packet,))
        # jobs.append(send_process)

        for job in jobs:
            job.start()
            break
        for job in jobs:
            job.join()

        if result_queue.get():
            self.state = "Authenticated"


def main():
    monitor_ifc = "wlan1mon"
    # sta_mac = "22:22:22:22:22:22"
    # bssid = "A4:67:06:80:06:BF"
    conf.iface = monitor_ifc

    # mac configuration per command line arguments, MACs are converted to
    # always use lowercase

    s = conf.L2socket(iface='wlan1mon')
    mon_ifc = Monitor(monitor_ifc, s)

    connection = ConnectionPhase(mon_ifc, s)

    # if connection.state == "Authenticated":
    #     print("STA is authenticated to the AP!")
    # else:
    #     print("STA is NOT authenticated to the AP!")
    while True:
        connection.send_authentication()



if __name__ == "__main__":
    sys.exit(main())