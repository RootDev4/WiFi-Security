#!/usr/bin/python

__author__ = 'Ramon Fontes'
__url__ = 'https://github.com/intrig-unicamp/mininet-wifi/blob/master/examples/authentication.py'

'This example shows how to work with WPA3 authentication'
'Updated version by RootDev4 @ 06/2021'

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def topology():
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', passwd='123456789a', encrypt='wpa3')
    sta2 = net.addStation('sta2', passwd='123456789a', encrypt='wpa3')
    ap1 = net.addAccessPoint('ap1', ssid="wpa3wifi", mode="g", channel="1",
                             passwd='123456789a', encrypt='wpa3',
                             failMode="standalone", datapath='user', 
                             wpa_key_mgmt='SAE', ieee80211w=2)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating Stations\n")
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)

    info("*** Starting network\n")
    net.build()
    ap1.start([])

    info("*** Adding interface hwsim0\n")
    ap1.cmd('ifconfig hwsim0 up')

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
