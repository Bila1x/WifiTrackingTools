import time
import subprocess


MACS = [["68:64:4b:65:8f:99","R",1],
["cc:08:e0:1e:dc:da","N",1],
["00:0E:8E:71:CA:EE","E",1],
["4C:66:41:60:A8:9F","E",1],
["C8:38:70:04:F2:DB","E",1],
["40:40:a7:62:b7:b9","H",1],
["84:C7:EA:29:83:BF","H",1],
["D8:C4:6A:4A:30:BE","D",1],
["30:07:4d:d2:97:33","D",1],
["14:56:8e:90:92:27","D",1],
["c0:11:73:6e:7f:fd","D",1],]

#print(MACS)
while True:
    for mac in MACS:
    result = subprocess.run(["tcpdump", "-r jjjjjj-01.cap ether src B4:F7:A1:C0:8E:C1"])
        if mac[2] != result:
            print("matched")
            #file = open("./data-01.cap", "r")
            mac[2]=something
            #file.close
    print(MACS)
    time.sleep(5)