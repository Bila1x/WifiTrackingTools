import time
import subprocess


MACS = [["11:22:33:44:55:66","R",1],
["22:33:44:55:66:11","N",1],

#print(MACS)
while True:
    for mac in MACS:
    result = subprocess.run(["tcpdump", "-r jjjjjj-01.cap ether src 44:55:66:11:22:33"])
        if mac[2] != result:
            print("matched")
            #file = open("./data-01.cap", "r")
            mac[2]=something
            #file.close
    print(MACS)
    time.sleep(5)