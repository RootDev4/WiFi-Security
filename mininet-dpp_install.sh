#!/bin/bash

# Running DPP functionality inside Mininet-WiFi.
# @author: RootDev4 (c) 06/2021
# @url: https://github.com/RootDev4/Attacking-WLAN

# Check if Mininet-WiFi is installed
if ! command -v mn --wifi &> /dev/null
then
    echo "[!] Mininet-WiFi not found."
    exit
fi

echo "[>] Installing prerequisites"
apt update && apt upgrade -y
apt install wget -y

echo "[>] Downloading source code"
wget https://raw.githubusercontent.com/RootDev4/Attacking-WLAN/main/dpp-auth.py
chmod +x dpp-auth.py

echo "[>] Updating config of hostapd and wpa_supplicant"
cd /home/wifi/containernet/mininet-wifi/hostap
echo "CONFIG_INTERWORKING=y" >> ./hostapd/.config
echo "CONFIG_DPP=y" >> ./hostapd/.config
echo "CONFIG_IEEE80211W=y" >> ./wpa_supplicant/.config
echo "CONFIG_DPP=y" >> ./wpa_supplicant/.config

echo "[>] Building hostapd and wpa_supplicant with new config"
cd ./hostapd
make && make install
cd ../wpa_supplicant
make && make install

echo "[>] Done. Start script by running ./dpp-auth.py"
