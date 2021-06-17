#!/bin/bash

# Install Mininet with WiFi support (Mininet-WiFi).
# @author: RootDev4 (c) 06/2021
# @url: https://github.com/RootDev4/Attacking-WLAN

echo "[>] Installing prerequisites"
apt update && apt upgrade -y > /dev/null
apt install git mininet -y > /dev/null

echo "[>] Downloading Mininet-WiFi source code"
git clone https://github.com/intrig-unicamp/mininet-wifi > /dev/null
cd mininet-wifi

echo "[>] Installing Mininet-WiFi"
util/install.sh -Wlnfv > /dev/null
echo "[>] Done. Start example WiFi network with `mn --wifi`"
