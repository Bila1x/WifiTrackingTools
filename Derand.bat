set /p id=Enter ID: 
::set /p mac=Enter MAC: 
:: echo %id%
"c:\Program Files\Wireshark\tshark.exe" -r %id%.cap -Y "wlan.sa_resolved contains "Apple" || (not wlan.sa_resolved contains "_" && wlan.fc.type_subtype == 4 && wlan_radio.signal_dbm >= -90)" -T fields -e wlan.sa_resolved -e wlan.seq -e frame.time_epoch -e wlan_radio.signal_dbm -e wlan.tag.length -e wlan.sa > Derand-%id%.xls
:: frame.time
:: wlan.fc.retry == 0
pause