from scapy.all import *
import time
import random

class Monitor:
    def __init__(self, mon_ifc, s):
        with open('Apple-lowcase-oui.txt', 'r') as f:
            ouis = f.readlines()
            ouiList = [x.strip() for x in ouis]
        #ouiList = set(ouiList)
        # print(type(ouiList))
        self.ouiList = set(ouiList)
        self.mon_ifc = mon_ifc
        # self.sta_mac = sta_mac
        # self.bssid = bssid
        # self.auth_found = False
        # self.assoc_found = False
        # self.dot11_rates = Dot11EltRates()
        self.s = s
        self.tap = '\x00\x00\x08\x00\x00\x00\x00\x00'
        self.probe = '\x50\x00\x00\x00'
        self.myaddr = '\x22\x22\x22\x22\x22\x22\x22\x22\x22\x22\x22\x22\x00\x00'
        self.fixedparms = '\x00\x00\x00\x00\x00\x00\x00\x00\x64\x00'
        # self.adds = [RadioTap(), Dot11(subtype=5, addr1='11:11:11:11:11:11', addr2='22:22:22:22:22:22', addr3='22:22:22:22:22:22'), Dot11ProbeResp(cap=0x1104), Dot11Elt(ID=0, info='ME'),'\x01\x08\x82\x84\x8b\x96\x24\x30\x48\x6c\x03\x01\x06\x2a\x01\x00\x32\x04\x0c\x12\x18\x60']
        self.ssids = ['OEBB','AndroidAP','eduroam', 'OEBB-station', 'Freewave', 'Wiener Linien Free WiFi', '.wienatPublicWLAN', 'Austrian Free Wifi']
        #self.ssids = ['3HuiTube_2.4Ghz_7369', 'UPCBF384AA', 'Alice_Im_Wland', 'UPC Wi-Free', 'UPC1376137', 'WLAN1-97M4E3', 'UPC4D24DEF']
        #self.WPA = Raw('\x30\x14\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x01\x0c\x00')
        self.AP = '\x30\x14\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x02\x0c\x00'
        self.WF = '\x30\x18\x01\x00\x00\x0f\xac\x02\x02\x00\x00\x0f\xac\x04\x00\x0f\xac\x02\x01\x00\x00\x0f\xac\x01\x00\x00'
        self.ER = '\x30\x14\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x01\x28\x00'
        self.OPN = ''
        self.counter = 0
        # self.count = 0
        # self.timer = 0
        self.rest = '\x01\x08\x82\x84\x8b\x96\x24\x30\x48\x6c\x03\x01\x06\x2a\x01\x00\x32\x04\x0c\x12\x18\x60'

    def SSIDparams(self,randssid):
        return '{:02x}{:02x}{}'.format(0, len(randssid), randssid.encode('hex')).decode('hex')

    def send_packet(self, packet, packet_type=None):
        # Send out the packet
        # if packet_type is None:
        #     send(packet)
        # elif packet_type == "AssoReq":
        #     packet /= self.dot11_rates
        #     send(packet)
        # else:
        #     print("Packet Type '{0}' unknown".format(packet_type))
        #before = time.time()
        seen_sender = packet[Dot11].addr2
        # dot11elt = packet.getlayer(Dot11Elt)
        # while dot11elt and dot11elt.ID != 221:
        #     dot11elt = dot11elt.payload.getlayer(Dot11Elt)
        # aa = str(dot11elt).find('\xdd\x0b\x00\x17\xf2\x0a\x00\x01\x04\x00\x00\x00\x00')
        # print(hexdump(packet[Dot11Elt][3]))
        # if dot11elt:
        #packet /= self.dot11_rates
        #if seen_sender[:8] not in self.ouiList:
        #print(packet.command())
        #print(packet.payload)
        if seen_sender[:8] == 'da:a1:19'\
                or ('\xdd\x0b\x00\x17\xf2\x0a\x00\x01\x04\x00\x00\x00\x00' in str(packet)
                    and seen_sender[:8] not in self.ouiList):

            # randssid = random.choice(self.ssids)
            rand = random.randint(1, 100)
            # print(rand)
            if rand <= 25:  # 29
                ssidChoice = 0
            elif rand <= 45:  # 21
                ssidChoice = 1
            elif rand <= 65:  # 19
                ssidChoice = 2
            elif rand <= 75:  # 16
                ssidChoice = 3
            elif rand <= 85:  # 16
                ssidChoice = 4
            elif rand <= 90:  # 16
                ssidChoice = 5
            elif rand <= 95:  # 16
                ssidChoice = 6
            else:  # 15
                ssidChoice = 7
            randssid = self.ssids[ssidChoice]
            # if self.counter == 4: self.counter = 0
            # else: self.counter += 1
            if randssid == 'AndroidAP': keyType = self.AP; caps = '\x11\x04'
            #elif randssid == 'UPC Wi-Free': keyType = self.WF; caps = '\x11\x04'
            elif randssid == 'eduroam': keyType = self.ER; caps = '\x31\x14'
            else: keyType = self.OPN; caps = '\x21\x04'
            #self.adds[1][Dot11].addr1 = seen_sender
            #self.adds[3][Dot11Elt].info = randssid
            #final = self.adds / keyType
            #final = '{}{}{}{}{}{}'.format(self.adds[0], self.adds[1], self.adds[2], self.adds[3], self.adds[4], keyType)
            final = '{}{}{}{}{}{}{}{}{}'.format(self.tap, self.probe, seen_sender.replace(':','').decode('hex'), self.myaddr, self.fixedparms, caps, self.SSIDparams(randssid), self.rest, keyType)

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
        sniff(iface=self.mon_ifc, filter='type mgt subtype probe-req and wlan broadcast',
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