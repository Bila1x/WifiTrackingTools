This project is a demonstration of wifi tracking in action, in a wardriving manner, using a Raspberry Pi for packet capture, and analyzing data for tracking wifi devices.  
MAC address anonymization was introduced as an anecdote to tracking, but it has its limitations and can be bypassed (to an extent) as demonstrated in this project.  

Pack up your backpack with a Raspberry Pi, powered by a battery bank, and take a walk around town, in different locations, you'll be surprised to encounter a device in both locations. It's a small world!.  

```
                                             \   /
                                            \ \ / /
                                            / /|\ \
                                             / | \
                                               |               +-------------------------+
                          +--------------+     |               | Index to csv            |
                          |  Capture     |     |               | Store in db             |
+-------+    Bluetooth    |  De-anonymize|     |               | Analyze                 |
|+-----+|    Tethering    |              |     |               |                         |
||     || --------------> |              ++---++               |                         |
||     ||                 |      RPi     ||NIC||               |            PC           |
||     || <-------------- |              ++---++               |                         |
|+-----+|    Notify       |              |                     |                         |
+-------+    Show stats   +---+   +------+                     +---+                +----+
   Phone                  |CAP|   |tshark|                     |CSV|                | DB |
                          +---+---+------+                     +---+----------------+----+
          ++------------++        ^
          || -        + ||        |
          || Power Bank |+--------+
          ++------------++

             --------------------+--------------------         -----------+----------
                                 |                                        |
                                 |                                        |
                                 v                                        v

                            Collection                                 Analysis
```

**Requirements**
- Raspberry Pi.
- USB wifi adapter with Monitor-Mode support. A separate strong antenna turns better results.
- tshark on PC and RPi.
- tcpdump on RPi is required for `py-seek.py`.
- aircrack-ng on RPi to start Monitor-mode.
- Python 3.x on PC (scapy, sqlite3).
- WinDump on PC (Optional) for `Analyzer.py`.

**Analysis Tools**
- `capture.sh`. initiates the wifi capture with tshark.
- `Indexer.py`. Indexes capture files into a csv with information about APs, Clients and the timerange of their appearance.
- `associate.py` & `monitor_associate.py`. Sets up a fake AP to help De-Anonymize devices that randomize MAC addresses.
- `py-seek.py`/`pyshake.py`. Sends notifications when a desired MAC address is in proximity.
- `db.py`. Used to add csv files created by `Indexer.py` to an SQlite3 database.
- `Analyzer` De-Anonymizes devices that advertise randomized MAC addresses.

**RPi tracking tools**
1. `capture.sh`. Make sure to run this first so the capture starts.  
Turns on Monitor-mode on your wifi adapter and switches to channel 6.  
Turns off the embedded wifi adapter and HDMI port to save energy.  
Starts the packet capture with `tshark` excluding the capture of AP beacon frames to save space.
Make sure to replace wlan1mon with your wifi adapter's interface name.  
The capture is completely passive. Nothing is being transmitted actively by the wifi adapter.
2. `deanonymize.py` (Optional). Run this script to initiate a fake AP with multiple SSIDs. If clients are configured to connect to these SSIDs, they will use their real MAC address and try to connect to your AP.
replace the list of SSIDs you'd like to use. Use SSIDs that are commonly used in your region in order for clients that are preconfigured to connect to these SSIDs, attempt connecting to it. Clients will fail with associating with your hotspot since it only announces SSIDs and never authenticates with clients. When clients attempt to associate, they use their real MAC address which will be captured with `capture.sh`.  
3. `py-seek.py` sends a notification when a preset MAC address is in proximity. Set a list of MAC addresses to track in `MACS` file one perline, each followed with a name e.g. `00:11:22:33:44:55,test`
4. `pyshake.py` (Optional) same as `py-seek.py` with the addition of de-authenticating random clients connected to random APs in order to collect authentication handshakes (with `capture.py`) to use for cracking.
5. new parts of the capture file to be analyzed by `py-seek.py` using tcpdump every 5 seconds.   
Use a service like Pushover to send notifications to your phone. Notifications are sent when a tracked client is in proximity and also in case tshark stopped working. if you choose another service, make sure to adapt the http request in the script.
Modify the script's TOKEN and USER variables obtained from Pushover. You can also modify the interval of checking for clients.

**Analysis Tools**
1. `Indexer.py` creates a csv for each cap file in a folder to keep track of all detected devices and the timerange in which they appeared.
2. `dbbb.py` adds csvs created by `Indexer.py` to database.
3. `derand.py` attempts to de-anonymize devices based on interval of probe requests, signal strength and other variables to get the real timerange in which a given device appears. E.g. if a device uses its real MAC address once, all antecedent and subsequent probe requests can be inferred using the aforementioned variables.

The csv is split into APs, clients and Unknown, with the following columns:  
**APs:**  
'BSSID', 'First seen', 'Last seen', 'Cipher', 'Authentication', 'Channel', 'Packets', 'Least dBm', 'SSID'  
**Clients:**  
'Station','First seen','Last seen','Least dBm','Packets','BSSID','Probed SSIDs'  
**Undefined:**  
'Undefined', 'First seen', 'Last seen', 'Least dBm', 'Packets'

**TODO**  
- integrating GPS in the pipeline.

**Q&A**  
Q: What is undefined?  
A: MAC addresses that appear in the receiver or transmitter fields of an Ethernet frame but never as a sender or destination in the whole capture file. It's not possible to determine if this is an AP or a station.  
Q: Do these tools work passively or actively?
A: Only `pyshake.py` and `deanonymize.py` send out frames.
Q: Why channel 6 is used for capture?
A: This allows for capturing data from slightly lower or higher channels, meaning more data!. When devices probe, they do so on all channels sequentially. APs usually stay within the same channel.  
Q: Why use bluetooth tethering instead of a wifi hotspot using the embedded wifi interface to connect my phone?
A: Bluetooth tethering saves energy. Moreover, a wifi hotspot will add unneeded noise to your capture file.  
Q: Is this legal?  
A: This is meant for demonstration purposes only. Check your local laws. Capturing data **passively** is allowed in some jurisdictions.