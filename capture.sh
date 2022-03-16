# turn off HDMI port
#/opt/vc/bin/tvservice -o
# turn off integrated wifi adapter
#sudo ifconfig wlan0 down
#sleep 1

# turn on external wifi adapter and switch to channel 6
sudo airmon-ng start wlan1
sleep 1
sudo iwconfig wlan1mon channel 11

# create a ramdisk
mkdir -p /ramdisk
if ! mountpoint -q -- "/ramdisk"; then
  mount -t tmpfs -o size=50M tmpfs /ram
  printf "created a ramdisk at /ramdisk\n"
fi
rm /ramdisk/*.cap
rm /ramdisk/*.html

# run tshark
fname=$(date +"%Y%m%d%H%M%S")
sudo touch "./cap/$fname".cap
sudo tshark -w "./cap/$fname".cap -f "wlan[0] != 0x80" -F pcap -i wlan1mon
