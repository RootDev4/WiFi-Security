#!/usr/bin/python
# This script generates a 7 digit pin out from a MAC address

mac = '84:C9:B2:C4:7F:C0' # MAC address of device
macInt = int(mac.replace(':', ''), 16) # 146001822515136
print((macInt & 0xFFFFFF) % 10000000) # 2877760
