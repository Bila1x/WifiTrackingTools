import multiprocessing
from scapy.all import *

from monitor_ifc import Monitor


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