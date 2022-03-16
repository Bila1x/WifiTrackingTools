ifconfig 
ifconfig eth0 up
sudo ifconfig eth0 up
ifconfig 
apt update
sudo apt update
dpkg -i /home/pi/Downloads/VNC-Server-6.7.1-Linux-ARM.deb 
sudo dpkg -i /home/pi/Downloads/VNC-Server-6.7.1-Linux-ARM.deb 
vncserver
ps aux
ps aux|grep vnc
service vncserver stop
sudo -s
ifconfig 
ping google.com
ifconfig 
sudo -s
ping google.com
exit
xrandr 
xrandr --help
sudo -s
sudo -s
sudo -s
ifconfig
ping google.com
clear
sudo apt-get install libguestfs-tools
sudo apt-get install guestmount
sudo apt-get install libguestfs-tools
guestmount --add /home/pi/Desktop/ --inspector --rw /mnt/s
guestmount --add /home/pi/Desktop/test.vhdx --inspector --rw /mnt/s
guestmount --add /home/pi/Desktop/test.vhdx --inspector --ro /mnt/s
tail -n 30 /var/log/syslog
sudo service hostapd stop
tail -n 30 /var/log/syslog
guestmount --add /home/pi/Desktop/test.vhdx --inspector --ro /mnt/s
tail -n 30 /var/log/syslog
journalctl -xe
sudo guestmount --add /home/pi/Desktop/test.vhdx --inspector --rw /mnt/s
sudo guestmount --add /home/pi/Desktop/test.vhdx --inspector --ro /mnt/s
mkdir /mnt/s
sudo mkdir /mnt/s
ls /mnt/s/
ls /mnt/
guestmount --add /home/pi/Desktop/test.vhdx --inspector --rw /mnt/s
sudo guestmount --add /home/pi/Desktop/test.vhdx --inspector --rw /mnt/s
export LIBGUESTFS_DEBUG=1 LIBGUESTFS_TRACE=1
sudo guestmount --add /home/pi/Desktop/test.vhdx --inspector --rw /mnt/s
guestmount --add /home/pi/Desktop/test.vhdx --inspector --rw /mnt/s
libguestfs-test-tool
sudo apt install gnulib
guestmount --add /home/pi/Desktop/test.vhdx --inspector --rw /mnt/s
feboot
sudo apt install qemu-utils 
sudo apt install nbd-client
sudo rmmod nbd;sudo modprobe nbd max_part=16
sudo rmmod nbd
sudo modprobe nbd max_part=16
qemu-nbd -c /dev/nbd0 /home/pi/Desktop/test.vhdx 
sudo qemu-nbd -c /dev/nbd0 /home/pi/Desktop/test.vhdx 
tcpdump -w /home/login.cap
sudo tcpdump -w /home/login.cap
sudo apt install tshark
tshark -f "port 80" -w /home/login.cap
tshark -f "port 80" -w /home/login.cap -i wlan1mon
sudo tshark -f "port 80" -w /home/login.cap -i wlan1mon
sudo tshark -f "port 80" -w /home/login.cap -i wlan1
tshark -r /home/login.cap
sudo tshark -r /home/login.cap
sudo chmod 777 /home/login.cap 
tshark -r /home/login-test.cap
tshark -w /home/login-test.cap -i wlan1
sudo tshark -F pcap-w /home/login-test.cap -i wlan1
sudo tshark -F pcap -w /home/login-test.cap -i wlan1
sudo tshark -F pcap -w /home/login-test.cap -i eth0
sudo chmod 777 /home/login-test.cap 
sudo tshark -F pcap -w /home/login-test.cap -i eth0
nc
echo -n -e "\x50\x4f\x53\x54\x20\x2f\x6c\x6f\x67\x69\x6e\x20\x48\x54\x54\x50\x2f\x31\x2e\x31\x0d\x0a\x48\x6f\x73\x74\x3a\x20\x31\x30\x2e\x31\x30\x2e\x31\x2e\x32\x35\x34\x0d\x0a\x43\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e\x3a\x20\x6b\x65\x65\x70\x2d\x61\x6c\x69\x76\x65\x0d\x0a\x43\x6f\x6e\x74\x65\x6e\x74\x2d\x4c\x65\x6e\x67\x74\x68\x3a\x20\x31\x30\x31\x0d\x0a\x43\x61\x63\x68\x65\x2d\x43\x6f\x6e\x74\x72\x6f\x6c\x3a\x20\x6d\x61\x78\x2d\x61\x67\x65\x3d\x30\x0d\x0a\x4f\x72\x69\x67\x69\x6e\x3a\x20\x68\x74\x74\x70\x3a\x2f\x2f\x65\x72\x64\x62\x65\x72\x67\x2e\x72\x7a\x32\x31\x2e\x6e\x65\x74\x0d\x0a\x55\x70\x67\x72\x61\x64\x65\x2d\x49\x6e\x73\x65\x63\x75\x72\x65\x2d\x52\x65\x71\x75\x65\x73\x74\x73\x3a\x20\x31\x0d\x0a\x43\x6f\x6e\x74\x65\x6e\x74\x2d\x54\x79\x70\x65\x3a\x20\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x78\x2d\x77\x77\x77\x2d\x66\x6f\x72\x6d\x2d\x75\x72\x6c\x65\x6e\x63\x6f\x64\x65\x64\x0d\x0a\x55\x73\x65\x72\x2d\x41\x67\x65\x6e\x74\x3a\x20\x4d\x6f\x7a\x69\x6c\x6c\x61\x2f\x35\x2e\x30\x20\x28\x57\x69\x6e\x64\x6f\x77\x73\x20\x4e\x54\x20\x31\x30\x2e\x30\x3b\x20\x57\x69\x6e\x36\x34\x3b\x20\x78\x36\x34\x29\x20\x41\x70\x70\x6c\x65\x57\x65\x62\x4b\x69\x74\x2f\x35\x33\x37\x2e\x33\x36\x20\x28\x4b\x48\x54\x4d\x4c\x2c\x20\x6c\x69\x6b\x65\x20\x47\x65\x63\x6b\x6f\x29\x20\x43\x68\x72\x6f\x6d\x65\x2f\x37\x39\x2e\x30\x2e\x33\x39\x34\x35\x2e\x31\x33\x30\x20\x53\x61\x66\x61\x72\x69\x2f\x35\x33\x37\x2e\x33\x36\x0d\x0a\x41\x63\x63\x65\x70\x74\x3a\x20\x74\x65\x78\x74\x2f\x68\x74\x6d\x6c\x2c\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x78\x68\x74\x6d\x6c\x2b\x78\x6d\x6c\x2c\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x78\x6d\x6c\x3b\x71\x3d\x30\x2e\x39\x2c\x69\x6d\x61\x67\x65\x2f\x77\x65\x62\x70\x2c\x69\x6d\x61\x67\x65\x2f\x61\x70\x6e\x67\x2c\x2a\x2f\x2a\x3b\x71\x3d\x30\x2e\x38\x2c\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x73\x69\x67\x6e\x65\x64\x2d\x65\x78\x63\x68\x61\x6e\x67\x65\x3b\x76\x3d\x62\x33\x3b\x71\x3d\x30\x2e\x39\x0d\x0a\x52\x65\x66\x65\x72\x65\x72\x3a\x20\x68\x74\x74\x70\x3a\x2f\x2f\x65\x72\x64\x62\x65\x72\x67\x2e\x72\x7a\x32\x31\x2e\x6e\x65\x74\x2f\x0d\x0a\x41\x63\x63\x65\x70\x74\x2d\x45\x6e\x63\x6f\x64\x69\x6e\x67\x3a\x20\x67\x7a\x69\x70\x2c\x20\x64\x65\x66\x6c\x61\x74\x65\x0d\x0a\x41\x63\x63\x65\x70\x74\x2d\x4c\x61\x6e\x67\x75\x61\x67\x65\x3a\x20\x65\x6e\x2d\x55\x53\x2c\x65\x6e\x3b\x71\x3d\x30\x2e\x39\x2c\x61\x72\x3b\x71\x3d\x30\x2e\x38\x2c\x64\x65\x3b\x71\x3d\x30\x2e\x37\x0d\x0a\x0d\x0a\x75\x73\x65\x72\x6e\x61\x6d\x65\x3d\x31\x30\x31\x32\x5f\x31\x39\x42\x26\x70\x61\x73\x73\x77\x6f\x72\x64\x3d\x36\x65\x36\x62\x66\x34\x61\x62\x63\x32\x61\x31\x38\x36\x30\x32\x34\x64\x39\x66\x31\x39\x39\x62\x32\x31\x35\x34\x63\x61\x35\x66\x26\x64\x73\x74\x3d\x68\x74\x74\x70\x25\x33\x41\x25\x32\x46\x25\x32\x46\x31\x30\x2e\x30\x2e\x30\x2e\x31\x33\x38\x25\x32\x46\x26\x70\x6f\x70\x75\x70\x3d\x74\x72\x75\x65" | nc 213.185.178.165 80
ifconfig 
sudo tshark -F pcap -w /home/login-test.cap -i eth0
echo -n -e "\x50\x4f\x53\x54\x20\x2f\x6c\x6f\x67\x69\x6e\x20\x48\x54\x54\x50\x2f\x31\x2e\x31\x0d\x0a\x48\x6f\x73\x74\x3a\x20\x31\x30\x2e\x31\x30\x2e\x31\x2e\x32\x35\x34\x0d\x0a\x43\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e\x3a\x20\x6b\x65\x65\x70\x2d\x61\x6c\x69\x76\x65\x0d\x0a\x43\x6f\x6e\x74\x65\x6e\x74\x2d\x4c\x65\x6e\x67\x74\x68\x3a\x20\x31\x30\x31\x0d\x0a\x43\x61\x63\x68\x65\x2d\x43\x6f\x6e\x74\x72\x6f\x6c\x3a\x20\x6d\x61\x78\x2d\x61\x67\x65\x3d\x30\x0d\x0a\x4f\x72\x69\x67\x69\x6e\x3a\x20\x68\x74\x74\x70\x3a\x2f\x2f\x65\x72\x64\x62\x65\x72\x67\x2e\x72\x7a\x32\x31\x2e\x6e\x65\x74\x0d\x0a\x55\x70\x67\x72\x61\x64\x65\x2d\x49\x6e\x73\x65\x63\x75\x72\x65\x2d\x52\x65\x71\x75\x65\x73\x74\x73\x3a\x20\x31\x0d\x0a\x43\x6f\x6e\x74\x65\x6e\x74\x2d\x54\x79\x70\x65\x3a\x20\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x78\x2d\x77\x77\x77\x2d\x66\x6f\x72\x6d\x2d\x75\x72\x6c\x65\x6e\x63\x6f\x64\x65\x64\x0d\x0a\x55\x73\x65\x72\x2d\x41\x67\x65\x6e\x74\x3a\x20\x4d\x6f\x7a\x69\x6c\x6c\x61\x2f\x35\x2e\x30\x20\x28\x57\x69\x6e\x64\x6f\x77\x73\x20\x4e\x54\x20\x31\x30\x2e\x30\x3b\x20\x57\x69\x6e\x36\x34\x3b\x20\x78\x36\x34\x29\x20\x41\x70\x70\x6c\x65\x57\x65\x62\x4b\x69\x74\x2f\x35\x33\x37\x2e\x33\x36\x20\x28\x4b\x48\x54\x4d\x4c\x2c\x20\x6c\x69\x6b\x65\x20\x47\x65\x63\x6b\x6f\x29\x20\x43\x68\x72\x6f\x6d\x65\x2f\x37\x39\x2e\x30\x2e\x33\x39\x34\x35\x2e\x31\x33\x30\x20\x53\x61\x66\x61\x72\x69\x2f\x35\x33\x37\x2e\x33\x36\x0d\x0a\x41\x63\x63\x65\x70\x74\x3a\x20\x74\x65\x78\x74\x2f\x68\x74\x6d\x6c\x2c\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x78\x68\x74\x6d\x6c\x2b\x78\x6d\x6c\x2c\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x78\x6d\x6c\x3b\x71\x3d\x30\x2e\x39\x2c\x69\x6d\x61\x67\x65\x2f\x77\x65\x62\x70\x2c\x69\x6d\x61\x67\x65\x2f\x61\x70\x6e\x67\x2c\x2a\x2f\x2a\x3b\x71\x3d\x30\x2e\x38\x2c\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x73\x69\x67\x6e\x65\x64\x2d\x65\x78\x63\x68\x61\x6e\x67\x65\x3b\x76\x3d\x62\x33\x3b\x71\x3d\x30\x2e\x39\x0d\x0a\x52\x65\x66\x65\x72\x65\x72\x3a\x20\x68\x74\x74\x70\x3a\x2f\x2f\x65\x72\x64\x62\x65\x72\x67\x2e\x72\x7a\x32\x31\x2e\x6e\x65\x74\x2f\x0d\x0a\x41\x63\x63\x65\x70\x74\x2d\x45\x6e\x63\x6f\x64\x69\x6e\x67\x3a\x20\x67\x7a\x69\x70\x2c\x20\x64\x65\x66\x6c\x61\x74\x65\x0d\x0a\x41\x63\x63\x65\x70\x74\x2d\x4c\x61\x6e\x67\x75\x61\x67\x65\x3a\x20\x65\x6e\x2d\x55\x53\x2c\x65\x6e\x3b\x71\x3d\x30\x2e\x39\x2c\x61\x72\x3b\x71\x3d\x30\x2e\x38\x2c\x64\x65\x3b\x71\x3d\x30\x2e\x37\x0d\x0a\x0d\x0a\x75\x73\x65\x72\x6e\x61\x6d\x65\x3d\x31\x30\x31\x32\x5f\x31\x39\x42\x26\x70\x61\x73\x73\x77\x6f\x72\x64\x3d\x36\x65\x36\x62\x66\x34\x61\x62\x63\x32\x61\x31\x38\x36\x30\x32\x34\x64\x39\x66\x31\x39\x39\x62\x32\x31\x35\x34\x63\x61\x35\x66\x26\x64\x73\x74\x3d\x68\x74\x74\x70\x25\x33\x41\x25\x32\x46\x25\x32\x46\x31\x30\x2e\x30\x2e\x30\x2e\x31\x33\x38\x25\x32\x46\x26\x70\x6f\x70\x75\x70\x3d\x74\x72\x75\x65" | nc 213.185.178.165 80
ssh 10.50.10.1
ps aux | grep dnsm
kill 14760
sudo kill 14760
ps aux | grep dnsm
ifconfig 
ifconfig wlan1 10.50.10.1/24
sudo ifconfig wlan1 10.50.10.1/24
ifconfig 
sudo ifconfig wlan1 10.50.10.20/24
ifconfig 
sudo ifconfig wlan1 10.50.10.20/24
ifconfig 
ping 10.50.10.1
ssh 10.50.10.1
ip route
ip route add 10.50.10.0/24 dev wlan1
sudo ip route add 10.50.10.0/24 dev wlan1
ip route add 10.50.10.0/24 dev wlan1
ip route
ping 10.50.10.1
ifconfig 
ip route del 10.50*
ip route del 10.50.10.1
sudo ip route del 10.50.10.1
sudo ip route del 10.50.10.0
sudo ip route del
sudo ip route
sudo ip route del 10.50.10.0
sudo ip route del 10.50.10.0/24
sudo ip route
ifconfig 
ifconfig wlan1 down
sudo ifconfig wlan1 down
ping 10.50.10.1
sudo tshark -w login.cap wlan1
sudo ifconfig wlan1 up
ifconfig wlan1 192.168.0.50
sudo ifconfig wlan1 192.168.0.50
ifconfig 
sudo ifconfig wlan1 192.168.0.50/24
ifconfig 
ip route
ip route add 192.168.0.0/24 dev wlan1 192.168.0.50
ip route add 192.168.0.0/24 192.168.0.50 dev wlan1
ip route add 192.168.0.0/24 via 192.168.0.50 dev wlan1
sudo ip route add 192.168.0.0/24 via 192.168.0.50 dev wlan1
ip route
sudo tail -n 35 /var/log/syslog
sudo tail -f /var/log/syslog
/opt/vc/bin/tvservice -o
sudo ifconfig wlan0 down
ifconfig 
ping google.com
ps aux | grep vnc
sudo service vncserver-x11-serviced status
sudo service vncserver-x11-serviced restart
sudo service vncserver-x11-serviced status
ifconfig 
sudo -s
sudo -s
sudo 0s
sudo -s
nano /tiamat
sudo nano /tiamat
ping google.com
exit
curl -sSL https://get.docker.com | sh
sudo usermod
sudo usermod pi
docker pull storjlabs/storagenode:beta
sudo docker pull storjlabs/storagenode:beta
curl icanhazip.com
sudo apt install openvpn
ifconfig 
cd /home/pi/storj/
mkdir pia
cd pia/
sudo wget https://www.privateinternetaccess.com/openvpn/openvpn.zip
unzip openvpn.zip 
cp ca.rsa.2048.crt ca.rsa.2048.pem /etc/openvpn/
sudo cp ca.rsa.2048.crt ca.rsa.2048.pem /etc/openvpn/
ls /etc/openvpn/
sudo cp ca.rsa.2048.crt ca.rsa.2048.pem /etc/openvpn/
sudo sudo cp ca.rsa.2048.pem /etc/openvpn/
cp
cp --help
sudo cp ca.rsa.2048.pem /etc/openvpn/
sudo cp crl.rsa.2048.pem /etc/openvpn/
ls /etc/openvpn/
sudo cp DE\ Berlin.ovpn /etc/openvpn/ex.conf
ls /etc/openvpn/
sudo su
sudo nano /etc/openvpn/login 
sudo nano /etc/openvpn/ex.conf 
sudo openvpn --config /etc/openvpn/ex.conf
sudo nano /etc/openvpn/ex.conf 
sudo openvpn --config /etc/openvpn/ex.conf
curl icanhazip.com
curl http://209.222.18.222:2000/?client_id=B26431AE2D26084266107303AEB0DDB458F4EBF30D09CE7BE846C1BDC2523AEA
nc
nc 32590
nc -u 32590
nc -u 0.0.0.0 32590
nc 0.0.0.0 32590
nc -z -v 0.0.0.0 32590
nc -v 0.0.0.0 32590
nc -u 0.0.0.0 32590
curl http://209.222.18.222:2000/?client_id=B26431AE2D26084266107303AEB0DDB458F4EBF30D09CE7BE846C1BDC2523AEB
curl http://209.222.18.222:2000/?client_id=B26431AE2D26084266107303AEB0DDB458F4EBF30D09CE7BE846C1BDC2523AEA
nc -u 127.0.0.1 32590
nc -lvu 32590
curl icanhazip.com
curl http://209.222.18.222:2000/?client_id=B26431AE2D26084266107303AEB0DDB458F4EBF30D09CE7BE846C1BDC2523AE1
nc -lvu 50463
ping google.com
nc -lvu 50463
iptables
iptables -h
iptables -L
sudo iptables -L
ifconfig 
sudo iptables -A OUTPUT -o tun+ -j ACCEPT
sudo iptables -A INPUT -i tun+ -j ACCEPT
nc -lvu 50463
sudo iptables -L
curl http://209.222.18.222:2000/?client_id=B26431AE2D26084266107303AEB0DDB458F4EBF30D09CE7BE846C1BDC2553AE1
ufw
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT
sudo iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
sudo iptables -A INPUT -p udp --sport 53 -j ACCEPT
sudo iptables -A OUTPUT -p udp --dport 1198 -j ACCEPT
sudo iptables -A INPUT -p udp --sport 1198 -j ACCEPT
sudo iptables -L
nc -lvu 50463
nc -lvu 55775
sudo iptables -A OUTPUT -o tun0 -j ACCEPT
sudo iptables -A INPUT -i tun0 -j ACCEPT
sudo iptables -L
nc -lvu 55775
curl whatismyip.akamai.com
curl http://209.222.18.222:2000/?client_id=B26431AE2D26084266107303AEB0DDB458F4EBF30D09CE7BE446C1BDC2553AE1
curl http://209.222.18.222:2000/?client_id=B26431AE2D26084266107303AEB0DDB458F4EBF30D05CE7BE446C1BDC2553AE1
curl http://209.222.18.222:2000/?client_id=B26431AE2D26084266107303AEB0DDB458F4EBF30D05CE7BB146C1BDC2553AE1
sudo iptables -A INPUT -p tcp --dport 20534 -j ACCEPT
curl whatismyip.akamai.com
sudo iptables -A INPUT -p udp --dport 20534 -j ACCEPT
nano /etc/openvpn/login 
nano /etc/openvpn/ex.conf 
history | grep cif
iptables -L
sudo iptables -L
sudo openvpn --config /etc/openvpn/ex.conf --daemon
service openvpn status
curl https://www.ovpn.com/v2/api/client/ptr | python -m json.tool
sudo service openvpn stop
ps aux | grep openv
curl https://www.ovpn.com/v2/api/client/ptr | python -m json.tool
kill 20105
sudo kill 20105
ps aux | grep openv
sudo openvpn --config /etc/openvpn/ex.conf 
sudo raspi-config 
ssh admin@192.168.51.254
ping google.com
ssh admin@192.168.51.254
ssh 192.168.51.254
ping google.com
nc -lvu 20534
nc
nc --help
man nc
nc -lv 20534
docker image ls
sudo docker image ls
history 
history | grep cif
ls /mnt/
ls /mnt/s
mkdir /mnt/tiamat
sudo mkdir /mnt/tiamat
sudo mount -t cifs -o username=admin //192.168.51.254/content /mnt/tiamat
sudo mount -t cifs -o username=admin //192.168.51.101/content /mnt/tiamat
ls /mnt/tiamat/
df -h
nano /mnt/tiamat/Documents/Stor/Stor.vhdx 
sudo umount /mnt/tiamat 
ls /mnt/tiamat/
sudo mount -t cifs -o username=admin,password=Schlumberger,dir_mode=0755,file_mode=0755 //192.168.51.101/content /mnt/tiamat
ls /mnt/tiamat/
ls /mnt/tiamat/Documents/Stor
ls /mnt/tiamat/Documents/Stor -la
nano /mnt/tiamat/Documents/111
id -u
id -g
cat /var/log/syslog
service nginx status
service nginx disable
systemctl disable nginx.service 
sudo systemctl disable nginx.service 
sudo systemctl status nginx.service 
sudo systemctl disable hostapd.service 
sudo systemctl status hostapd.service 
sudo systemctl stop hostapd.service 

service --status-all
sudo systemctl disable dnsmasq.service 
sudo systemctl status dnsmasq.service 
sudo systemctl stop dnsmasq.service 
sudo systemctl status dnsmasq.service 
sudo systemctl disable dnsmasq.service 
sudo systemctl status dnsmasq.service 
sudo systemctl status apache2.service 
sudo systemctl stop apache2.service 
sudo systemctl status apache2.service 
sudo systemctl disable apache2.service 
sudo systemctl status apache2.service 
ls /mnt/s2/
ls /mnt/s2/storagenode2/
ls /mnt/s2/storagenode2/storage/
top
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 14002 -j ACCEPT
tail -n 20 /var/log/syslog
ifconfig 
top
curl icanhazip.com
iptables -L
sudo iptables -L
nano /mnt/s2/test
rm /mnt/s2/test
nc -lv 31531
sudo iptables -A INPUT -p tcp --dport 31531 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 31531 -j ACCEPT
nc -lv 31531
ping google.com
nc -lu 31531
nc -lv 31531
nc --help
man nc
nc -lv 31531
curl icanhazip.com
ifconfig 
curl icanhazip.com
curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+'
curl icanhazip.com
sudo iptables -A INPUT -p tcp --dport 50967 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 50967 -j ACCEPT
top
sudo systemctl stop bluetooth.service 
sudo systemctl status bluetooth.target 
sudo systemctl stop bluetooth.target 
sudo service --status-all
sudo systemctl status nbd-client.service 
sudo systemctl status exim4.service 
sudo systemctl stop exim4.service 
sudo systemctl disable exim4.service 
top
sudo systemctl status raspi-config.service 
sudo systemctl status nginx.service 
sudo systemctl disable nginx.service 
sudo systemctl status nginx.service 
sudo systemctl status apache2.service 
top
curl 10.10.1.254
top
bmon 
bmon -U
ls /mnt/
ls /mnt/s2
ls /media/
ls /media/pi
ls /media/pi/D82428EE2428D0F4/
umount /media/pi/D82428EE2428D0F4 
sudo mount /dev/sda1 /mnt/s2
ls /mnt/s2/
sudo openvpn --config /etc/openvpn/ex.conf
service openvpn status
service openvpn stop
service openvpn status
sudo openvpn --config /etc/openvpn/ex.conf
vcgencmd measure_temp
bmon -U
tail -n 20 /var/log/syslog
bmon -U
tail -n 20 /var/log/syslog
/opt/vc/bin/tvservice -o
ifconfig 
sudo ifconfig wlan0 down
curl icanhazip.com
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
$port
sudo iptables -A INPUT -p tcp --dport $port -j ACCEPT
sudo iptables -A INPUT -p udp --dport $port -j ACCEPT
nc -lv $port
docker run -d --restart always --stop-timeout 300 -p 34331:28967 -p 127.0.0.1:14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="185.230.127.235:31531 -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
docker run -d --restart always --stop-timeout 300 -p 34331:28967 -p 127.0.0.1:14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="185.230.127.235:31531" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
docker container ls
sudo docker container ls
sudo docker rm storagenode
sudo docker run -d --restart always --stop-timeout 300 -p 34331:28967 -p 127.0.0.1:14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="185.230.127.235:31531" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
docker container ls
sudo docker container ls
sudo docker stop -t 300
sudo docker stop -t 300 storagenode
docker run -d --restart always --stop-timeout 300 -p 31531:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="193.176.86.125:31531" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker rm storagenode
docker run -d --restart always --stop-timeout 300 -p 31531:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="193.176.86.125:31531" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker container ls
docker run -d --restart always --stop-timeout 300 -p 31531:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="193.176.86.125:31531" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker run -d --restart always --stop-timeout 300 -p 31531:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="193.176.86.125:31531" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker logs storagenode
sudo docker stop -t 300 storagenode
sudo docker rm storagenode
sudo docker run -d --restart always --stop-timeout 300 -p 31531:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="185.230.127.235:31531" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker logs storagenode
sudo docker stop -t 300 storagenode
sudo docker logs storagenode
sudo docker run -d --restart always --stop-timeout 300 -p 31531:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="185.230.127.235:31531" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker rm storagenode
docker run -d --restart always --stop-timeout 300 -p 31531:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="185.230.127.235:31531" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker run -d --restart always --stop-timeout 300 -p 31531:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="185.230.127.235:31531" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker logs storagenode
sudo docker stop -t 300 storagenode
sudo docker rm storagenode
sudo docker run -d --restart always --stop-timeout 300 -p 50967:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="185.230.127.228:50967" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker logs storagenode
sudo docker stop -t 300 storagenode
sudo docker start storagenode
sudo docker logs storagenode
tail -n 20 /var/log/syslog
sudo apt-get install speedometer
speedometer 
speedometer eth0
sudo apt-get install bmon
bmon 
tail -n 20 /var/log/syslog
bmon --help
bmon -U
sh /storj/successrate.sh
sh /storj/successrate.sh1
sh /home/pi/storj/successrate.sh 
sh /home/pi/storj/successrate.sh storagenode
./home/pi/storj/successrate.sh storagenode
cd /home/pi/storj/
ls
./successrate.sh
chmod +x successrate.sh 
./successrate.sh
./successrate.sh storagenode
sudo ./successrate.sh storagenode
docker stop -t 300 storagenode
sudo docker stop -t 300 storagenode
curl 
curl --help
curl http://ipv4.download.thinkbroadband.com/512MB.zip /mnt/s2/test.temp
curl http://ipv4.download.thinkbroadband.com/512MB.zip --output /mnt/s2/test.temp
sudo docker start storagenode
bmon -U
top
nano /etc/openvpn/ex.conf 
sudo nano /etc/openvpn/ex.conf 
top
bmon -U
docker stop -t 300 storagenode
sudo docker stop -t 300 storagenode
sudo docer rm storagenode
sudo docker rm storagenode
ip=$(curl icanhazip.com)
curl icanhazip.com
sudo nano /etc/openvpn/ex.conf 
curl icanhazip.com
sudo nano /etc/openvpn/ex.conf 
curl icanhazip.com
sudo nano /etc/openvpn/ex.conf 
curl icanhazip.com
sudo nano /etc/openvpn/ex.conf 
curl icanhazip.com
sudo nano /etc/openvpn/ex.conf 
curl icanhazip.com
sudo nano /etc/openvpn/ex.conf 
curl icanhazip.com
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
$port
ip=$(curl icanhazip.com)
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
bmon -U
docker logs storagenode
sudo docker logs storagenode
sudo docker stop -t 300 storagenode
sudo docker rm storagenode
sudo nano /etc/openvpn/ex.conf 
curl icanhazip.com
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
docker logs tail storagenode
tail docker logs storagenode
docker logs storagenode
sudo docker logs storagenode
sudo docker stop -t 300 storagenode
sudo docker rm storagenode
ip=$(curl icanhazip.com)
ping google.com
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker logs storagenode
bmon -U
docker logs storagenode
sudo nano /etc/openvpn/ex.conf 
top
bmon -U
perf
perf recorm
perf record
sudo apt install linux-perf
perf
perf record
sudo apt install linux-perf-4.19
uname -r
apt search linux-tools
apt update
sudo apt update
sudo apt install linux-perf-4.19
sudo docker stop -t 300 storagenode
sudo docker rm storagenode
tail -n 20 /var/log/syslog
tail -f /var/log/syslog
curl http://10.10.1.254/
tail -f /var/log/syslog
taile docker logs storagenode
tail docker logs storagenode
docker logs storagenode
sudo docker logs storagenode
exit
sudo service openvpn stop
sudo openvpn --config /etc/openvpn/ex.conf
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
sudo mount /dev/sda1 /mnt/s2
nc -lv $port
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
bmon -U
top
bmon -U
sh /home/pi/storj/successrate.sh 
sudo sh /home/pi/storj/successrate.sh 
sudo sh /home/pi/storj/successrate.sh storagenode
bmon -U
bmon --help
bmon -U
vcgencmd measure_volts
vcgencmd measure_volts 1
$core
vcgencmd measure_volts sdram_c
vcgencmd measure_volts sdram_c,core
vcgencmd measure_volts sdram_c core
vcgencmd measure_volts sdram_c sdram_i
vcgencmd measure_volts sdram_c,sdram_i
vcgencmd measure_volts sdram_i
vcgencmd measure_volts sdram_p
vcgencmd measure_volts core
bmon -U
/opt/vc/bin/tvservice -o
bmon -U
df -h
sudo sh ./storj/successrate.sh 
nano /etc/openvpn/login 
nano /etc/openvpn/ex.conf 
bmon -U
ls /mnt/s2
ping google.com
docker stop -t 300 storagenode
sudo docker stop -t 300 storagenode
sudo docker rm storagenode
ifconfig 
ifdown eth0
ifconfig 
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
ls
sh storj/successrate.sh 
sudo sh storj/successrate.sh 
bmon -U
lsblk
df -h
ls -la /mnt/s2
ls -la /mnt/s2/storagenode2/
ls /home/
ls /mnt/
ls /mnt/s2/
ls /mnt/s2/storagenode2/
ls /mnt/s2/storagenode2/storage/
ls /home/
. /home/pi/storj/successrate.sh 
sudo . /home/pi/storj/successrate.sh 
sudo sh /home/pi/storj/successrate.sh 
nano /etc/openvpn/ex.conf 
bmon -U
curl http://10.10.1.254/
ip route add 10.10.1.254/32 via 192.168.51.254 dev eth0
sudo ip route add 10.10.1.254/32 via 192.168.51.254 dev eth0
curl http://10.10.1.254/
curl http://10.10.1.254/status
curl http://10.10.1.254/status | grep left
ls
curl https://pastebin.com/raw/FgN72mY0 --output wifilogin.py
curl http://10.10.1.254/logout
python3
python3 wifilogin.py 
pip3 install js2py
docker stop storagenode
sudo docker stop storagenode
sudo docker rm storagenode
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
docker logs storagenode
sudo docker logs storagenode
pip3 install requests js2py
nano wi
nano wifilogin.py 
python3 wifilogin.py 
sudo docker logs storagenode
history | grep succ
sh storj/successrate.sh 
sudo sh storj/successrate.sh 
free -m
top
echo $ip:$port
bmon -U
ping google.com
lsblk 
df -h
docker logs storagenode
sudo docker logs storagenode
top
docker stop storagenode
sudo docker stop storagenode
sudo docker rm storagenode
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker logs storagenode
sh storj/successrate.sh 
sudo sh storj/successrate.sh 
sh storj/successrate.sh 
sudo sh storj/successrate.sh 
sudo docker logs storagenode
sudo docker image ls
sudo docker stop storagenode
sudo docker rm storagenode
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode
sudo docker logs storagenode
docker update
sudo docker stop storagenode
sudo docker rm storagenode
docker
sudo docker pull storjlabs/storagenode
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode
sudo docker logs storagenode
ls /mnt/s1
ls /mnt/s2/
ls /mnt/s2/storagenode2/
ls /mnt/s2/storagenode2/storage/
sudo docker logs storagenode
ls /mnt/s2/
curl http://10.10.1.254/status
python3 wifilogin.py 
curl http://10.10.1.254/logout
python3 wifilogin.py 
ping google.com
python3 wifilogin.py 
ping google.com
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
$ip$port
sudo stop -t 300 storagenode
sudo docker stop storagenode
sudo docker rm storagenode
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode
sudo docker logs storagenode
ping google.com
sudo docker logs storagenode
$port
sudo docker pull storjlabs/storagenode:beta
ping google.com
sudo docker -t 300 stop storagenode
sudo docker stop -t 300 storagenode
sudo docker rm storagenode
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
free -m
sudo docker stop -t 300 storagenode
sudo docker rm storagenode
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --memory=800m --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode
free -m
sudo docker logs storagenode
free -m
top
kill 802
top
sudo docker logs storagenode
sh succ
ls
sh storj/successrate.sh 
sudo sh storj/successrate.sh 
top
sudo sh storj/successrate.sh 
docker logs storagenode
sudo docker logs storagenode
docker logs storagenode
sudo sh storj/successrate.sh 
df -h
free -h
free -m
top
free -m
top
sudo top
sudo docker logs storagenode
sh storj/successrate.sh 
sudo sh storj/successrate.sh 
df -h
sudo sh storj/successrate.sh 
sudo docker --tail logs storagenode
sudo docker --tail 20 logs storagenode
sudo docker logs --tail 20 storagenode
sudo sh storj/successrate.sh 
sudo docker --tail 20 logs storagenode
sudo docker logs --tail 20 storagenode
ping google.com
python3 wifilogin.py 
sudo docker logs --tail 20 storagenode
df -h
sudo storj/successrate.sh 
ping google.com
curl http://10.10.1.254/logout && python3 wifilogin.py 
ping google.com
python3 wifilogin.py 
ip route add 10.10.1.254 via 192.168.51.254 dev eth0
sudo ip route add 10.10.1.254 via 192.168.51.254 dev eth0
sudo ip route add 10.10.1.254/32 via 192.168.51.254 dev eth0
ping google.com
python3 wifilogin.py 
curl http://10.10.1.254/logout && python3 wifilogin.py 
chromium-browser 
ping google.com
sudo docker stop -t 300 storagenode && sudo docer rm storagenode
sudo docker stop -t 300 storagenode && sudo docker rm storagenode
ping google.com
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --memory=800m --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode
sudo docker logs --tail 20 storagenode
ip route
ping 10.10.1.254
python3 wifilogin.py 
sudo storj/successrate.sh 
ping google.com
df -h
htop
sudo docker logs --tail 20 storagenode
sudo storj/successrate.sh 
df -h
free -m
htop
bmon -U
python3 wifilogin.py 
df -h
free -m
bmon -U
sudo storj/successrate.sh 
htop
sudo storj/successrate.sh 
free -m
df -h
ping google.com
sudo docker stop -t 300 storagenode && sudo docker rm storagenode
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --memory=800m --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
free -m
sudo docker logs --tail 20 storagenode
df -h
sudo storj/successrate.sh 
sudo docker logs --tail 20 storagenode
bmon -U
sudo docker logs --tail 20 storagenode
sudo storj/successrate.sh 
history | grep 100mb
history | grep 100
curl http://speedtest.sea01.softlayer.com/downloads/test100.zip --output /mnt/s2/100mb.test
curl http://speedtest.sea01.softlayer.com/downloads/test100.zip --output /dev/null
curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -
sudo apt install speedtest-cli 
speedtest-cli 
speed
speedtest
nano /etc/openvpn/ex.conf 
sudo nano /etc/openvpn/ex.conf 
sudo docker stop -t 300 storagenode && sudo docker rm storagenode
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
$port
speedtest
curl http://10.10.1.254/logout
python3 wifilogin.py 
ping google.com
python3 wifilogin.py 
history | grep route
sudo ip route add 10.10.1.254/32 via 192.168.51.254 dev eth0
python3 wifilogin.py 
ip route
python3 wifilogin.py 
ping google.com
chromium-browser 
ping google.com
speedtest
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --memory=800m --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker logs  --tail 20 storagenode
ping google.com
sudo storj/successrate.sh 
sudo docker logs  --tail 20 storagenode
speedtest
sudo docker logs  --tail 20 storagenode
sudo storj/successrate.sh 
df -h
python3 wifilogin.py 
ipconfig
ifconfig 
ethtool
ethtool -h
ethtool -a eth0
sudo ethtool -a eth0
iperf
free -m
sudo apt install iperf
iperf -s
mv /etc/openvpn/ex.conf /etc/openvpn/openvpn.conf
sudo mv /etc/openvpn/ex.conf /etc/openvpn/openvpn.conf
sudo raspi-config 
pwd
passwd 
sudo -s
passwd 
passwd pi
raspi-config 
sudo raspi-config 
sudo docker stop -t 300 storagenode && sudo docker rm storagenode
reboot
df -h
lsblk 
history | grep mount
history | grep "mount -t"
sudo -s
mount -t ntfs-3g -o rw,big_writes,noatime /dev/sda1 /mnt/s2
sudo mount -t ntfs-3g -o rw,big_writes,noatime /dev/sda1 /mnt/s2
ls /mnt/s2/
free -m
ps aux
free -m
service vncserver-x11-serviced status
service vncserver-x11-serviced stop
sudo service vncserver-x11-serviced stop
sudo service vncserver-x11-serviced status
sudo service vncserver-x11-serviced disable
sudo service vncserver-x11-serviced status
sudo service vncserver-x11-serviced disable
sudo service vncserver-x11-serviced disablea
sudo service vncserver-x11-serviced
sudo service vncserver-x11-serviced 
sudo service --status-all
free -m
sudo service vncserver-x11-serviced mask
top
ifconfig 
ping google.com
service openvpn status
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
service openvpn restart
sudo service openvpn restart
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
$port
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --memory=800m --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker logs --tail 20 storagenode
free -m
sudo docker logs --tail 20 storagenode
top
sudo docker logs --tail 20 storagenode
speedtest
sudo docker logs --tail 20 storagenode
sudo docker stop -t 300 storagenode && sudo docker rm storagenode
ping google.com
sudo service openvpn restart
ping google.com
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
speedtest
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --memory=800m --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
free -m
top
sudo docker logs --tail 20 storagenode
speedtest --help
speedtest --no-download
cat /var/log/syslog
time
date 
ip=$(curl icanhazip.com)
sudo ethtool eth0
cat /sys/class/net/eth0/speed 
ifconfig 
iperf 
iperf -s
iperf -c 192.168.50.161
iperf -s
nano wifilogin.py 
ip route 10.10.1.254/32 
ip route
ip route 10.10.1.254/32 via 192.168.51.254 dev eth0
ip route add 10.10.1.254/32 via 192.168.51.254 dev eth0
sudo ip route add 10.10.1.254/32 via 192.168.51.254 dev eth0
ip route
curl http://10.10.1.254/logout && python3 wifilogin.py 
ping google.com
speedtest --no-download
sudo docker logs --tail 20 storagenode
ping google.com
sudo docker stop -t 300 storagenode && sudo docker rm storagenode
sudo service stop openvpn
sudo service openvpn stop
speedtest --no-download
sudo service openvpn start
ip=$(curl icanhazip.com)
port=$(curl -Ss http://209.222.18.222:2000/?client_id=$(openssl rand -hex 64) | grep -oE '[0-9]+')
sudo docker run -d --restart always --stop-timeout 300 -p $port:28967 -p 14002:14002 -e WALLET="0xb2fcdb01f466a1583cca7d9ee65553c17c3859c6" -e EMAIL="bil258@hotmail.com" -e ADDRESS="$ip:$port" -e STORAGE="1.5TB" --memory=800m --log-opt max-size=50m --log-opt max-file=10 --memory=800m --mount type=bind,source=/home/pi/storj/identity_2,destination=/app/identity --mount type=bind,source=/mnt/s2/storagenode2,destination=/app/config --name storagenode storjlabs/storagenode:beta
sudo docker logs --tail 20 storagenode
ifconfig 
speedtest --no-download
sudo docker logs --tail 20 storagenode
sudo /home/pi/storj/successrate.sh 
exit
sudo /home/pi/storj/successrate.sh 
df -h
sudo /home/pi/storj/successrate.sh 
sudo docker logs --tail 20 storagenode
sudo -s
sudo docker logs --tail 20 storagenode
sudo storj/successrate.sh 
lsblk 
sudo docker stop -t 300 storagenode && sudo docker rm storagenode
su
sudo -s
speedtest
service --status-all
cat /var/log/syslog
halt
sudo halt
sudo -s
su
sudo -s
startx --help
service startx stop
service x11-common status
pkill x
su
startx
exit
airmon-ng start wlan1
sudo -s
su
sudo -s
sudo s
sudo -s
su
sudo -s
startx
stopx
startx --help
ifconfig 
ip address
ip address 
ip address --help
ip address help
ifdown eth0
ifconfig 
ifdown eth0
ifup eth0
sudo ifdown eth0
sudo ifup eth0
ifconfig 
networkctl 
ifconfig 
ifup eth0
ifdown eth0
nano /etc/network/interfaces
dhcpcd
sudo dhcpcd
ifconfig 
ifconfig 78.104.181.103
ping 78.104.181.103
reboot
su
sudo -s
ifconfig 
dhcpcd
sudo dhcpcd
ifconfig 
sudo -s
su
sudo -s
sudo -s
ps aux ¦ grep tshark
sudo -s
ps aux | grep tshark
shutdown
sudo shutdown
startx
ifconfig
vncserver-x11
service --list-all
sudo service --list-all
sudo service vncserver start
service
service --status-all
vncserver-x11
sudo -s
shutdown -h
sudo shutdown -h
sudo -s
sudo -s
history 
sudo -s
history 
cat /etc/issue
sudo -s
startx
