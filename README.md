# WifiTrackingTools
___

- [x] tested with Wireshark 2.4.5
- [ ] tested with Wireshark 3.6.3

This project is a demonstration of wifi tracking in action, in a wardriving manner, using a Raspberry Pi for packet capture, and analyzing data for tracking wifi devices.  
MAC address anonymization was introduced as an anecdote to tracking, but it has its limitations and can be bypassed (to an extent) as demonstrated in this project.  

Pack up your backpack with a Raspberry Pi, powered by a battery bank, and take a walk around town in two different locations, you'll be surprised to encounter a device in both locations. It's a small world!.  

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
  Phone                   |CAP|   |tshark|                     |CSV|                | DB |
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

## Requirements
___
- Raspberry Pi.
- USB wifi adapter with Monitor-Mode support. A separate strong antenna turns better results.
- `aircrack-ng` on RPi to start Monitor-mode.
- `tcpdump` on RPi is required for `notifier.py`.
- `tshark` on PC and RPi. Required for `capture.sh` & `indexer.py`
- `Python 3.x` on PC + `scapy`, `sqlite3`.
- `WinDump` or `tcpdump` on Windows or Linux respectively. Required for `Analyzer.py`.

## Installation & Configuration
___
- Clone this repository to PC and RPi.
- Install PC requirements with `pip install pc-requirements.txt`.
- Install RPi requirements with `pip install rpi-requirements.txt`.
- Install `tshark` on PC & RPi.
- Configure zero or more MAC addresses in `MAC.txt` to be tracked with `notifier.py`.
- Configure one or more SSIDs in `SSIDs.txt` to be advertised with `associate.py`.
- Install `analyzer.py` dependency:
  - For Windows: Download `WinDump.exe` and place it in the project directory (depends on `WinPCAP`).
  - For Linux: install `tcpdump`.


## RPi tracking tools
___
1. `capture.sh` initiates the wifi capture with tshark. Make sure to run this first.  
   - Turns on Monitor-mode on your wifi adapter and switches to channel 6.  
   - Turns off the embedded wifi adapter and HDMI port to save energy.  
   - Starts the packet capture with `tshark` excluding the capture of AP beacon frames to save space.
   - Make sure to replace `wlan1mon` with your wifi adapter's interface name.  
   - The capture is **completely passive**. Nothing is being transmitted actively by the wifi adapter.


2. `deanonymizer.py` (Optional). Advertises a fake AP with multiple SSIDs. If clients are configured to connect to these SSIDs, they will use their real MAC address and try to connect to your AP.
replace the list of SSIDs you'd like to use. Use SSIDs that are commonly used in your region in order for clients that are preconfigured to connect to these SSIDs, attempt connecting to it. Clients will fail with associating with your hotspot since it only announces SSIDs and never authenticates with clients. When clients attempt to associate, they use their real MAC address which will be captured with `capture.sh`.  


3. `notifier.py` sends a notification when a tracked MAC address is in proximity. Set a list of MAC addresses to track in `MACS` file, one per line, each followed with a name e.g. `00:11:22:33:44:55,test`. New data in the capture file is analyzed using `tcpdump` every 5 seconds.
   - Use a free service like Pushover to send notifications to your phone. Notifications are sent when a tracked client is in proximity along with its signal strength and also in case tshark stopped working. if you choose another notification service, make sure to adapt the http request in the script.
   - Modify the script's `TOKEN` and `USER` variables obtained from Pushover. You can also modify the interval of checking for clients.  


4. `pyshake.py` (Optional) same as `notifier.py` with the addition of de-authenticating random clients connected to random APs in order to collect authentication handshakes (with `capture.py`) to use for cracking.  


## Analysis Tools
___
1. `indexer.py` creates a CSV for each CAP file to keep track of all detected devices and the timerange in which they appeared.
   The csv is split into **APs, clients and Undefined**, with the following columns:  
   **APs:**  
   `| BSSID | First seen | Last seen | Cipher | Authentication | Channel | Packets | Least dBm | SSID |`    
   **Clients:**  
   `Station | First seen | Last seen | Least dBm | Packets | BSSID | Probed SSIDs |`  
   **Undefined:**  
   `Undefined | First seen | Last seen | Least dBm | Packets |`  


2. `index_db.py` adds CSVs created by `indexer.py` to database `whereabouts.db`.  


3. `derand.py` uses CSVs generated by `indexer.py` and attempts to de-anonymize devices based on interval of probe requests, signal strength and other variables to get the actual timerange in which a given device appears. E.g. if a device uses its real MAC address once, all antecedent and subsequent probe requests can be inferred using the aforementioned variables.


4. `Analyzer.py` provides statistics from capture files by counting actual number of devices (ignoring randomized MAC addresses), statistics about devices de-anomymized by `deanonymize.py`.

## Query tool
___
`seen.py` fetches a MAC address (or a list of addresses) whereabouts from database.

## RPi resource usage
___
- The RPi tools are designed with low power usage in mind, capturing and notifying uses few CPU cycles and disables unneeded HDMI port and embedded wifi adapter.
- Power usage is measured using a USB XXXXXXXX. The following graph shows peeks every 5 senconds (`notifier.py` analysis interval).
- `deanonymizer.py` and `py-shake.py` use more energy since they actively send data over the external (power hungry) USB adapter. The usage varies depending on the number of devices in proximity. `deanonymizer.py` only sends probe responses to anomyized devices.
- ssh or vnc access can be done using bluetooth tethering instead of wifi to save power.

## Project folder structure
___
```
WifiTrackingTools/
├── cap/
│   ├── 20200101030015.cap
│   ├── ..
├── csv/
│   ├── 20200101030015.csv
│   └── ..
├── config/
│   ├── whereabouts.db
│   ├── create_oui.csv
│   └── proneOUIs.txt
├── indexer.py
├── db.py
├── analyzer.py
├── MACresolver.py
├── seen.py
├── derand.py
├── derandGUI.py
└── mostLines.py
```

## FAQ
___
> **Q: What is undefined?**  
> A: MAC addresses that appear in the receiver or transmitter fields of an Ethernet frame but never as a sender or destination in the whole capture file. It's not possible to determine if this is an AP or a station.  

> **Q: Do these tools work passively or actively?**  
> A: Only `pyshake.py` and `deanonymizer.py` send out frames.  

> **Q: Why channel 6 is used for capture?**  
> A: This allows for capturing data from slightly lower or higher channels, meaning more data!. When devices probe, they do so on all channels sequentially. APs usually stay within the same channel.  

> **Q: Why does the fake AP of `associate.py` not appear while looking for wifi networks on my phone?**  
> A: `associate.py` only replies to probe requests from devices with randomized MAC addresses. Only iOS and Android randomization is supported. Android randomization is supported only when a device uses Google's implementation. E.g. MACs beggining with `DA:A1:19`. Use the switch `-a` to advertise the SSID to all devices. Note that this will generate too much traffic.  

> **Q: Why use bluetooth tethering instead of a wifi hotspot using the embedded wifi interface to connect my phone?**  
> A: Bluetooth tethering saves energy. Moreover, a wifi hotspot will add unneeded noise to your capture file.  

> **Q: I keep seeing this device, am I being followed?**  
> No. Just no.

> **Q: Is this legal?**  
> A: This is meant for demonstration purposes only. Check your local laws. Capturing data **passively** is allowed in some jurisdictions.  


## TODO
___
- [ ] integrating GPS in the pipeline.