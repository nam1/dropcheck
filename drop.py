#!/usr/bin/env python

import sys
import subprocess
import re

args = sys.argv

ifconfig = "ifconfig "+str(args[1])
#print("\n$"+ifconfig)
proc = subprocess.call( ifconfig , shell=True)
v4ifconfig = "ifconfig "+str(args[1])+" |grep 'inet\s'"
v4inet = subprocess.getoutput(v4ifconfig)
v4address = v4inet.split(" ")
print("\nipv4 address: "+v4address[1])
v6ifconfig = "ifconfig "+str(args[1])+" |grep 'inet6 2001'"
v6inet = subprocess.getoutput(v6ifconfig)
v6address = v6inet.split(" ")
print("\nipv6 address: "+v6address[1])


netstat = "netstat -rn |grep default |grep "+str(args[1])
default = subprocess.getoutput(netstat)
line = default.split('\n')
v4addr = re.split('\s+',str(line[0]))
v4gw = v4addr[1]
v6addr = re.split('\s+',str(line[1]))
word = v6addr[1].split('%')
v6gw = word[0]
print("\nipv4 gateway: "+v4gw)
print("\nipv6 gateway: "+v6gw)
iping4 = "ping -c 5 -D -s 1472 "+v4gw
#print("\n$"+iping4)
proc = subprocess.call( iping4 , shell=True)
iping6 = "sudo ping6 -c 5 -m -D -s 1232 -I "+str(args[1])+" "+v6gw
#print("\n$"+iping6)
proc = subprocess.call( iping6 , shell=True)
wping4 = "ping -c 5 -D -s 1472 8.8.8.8"
#print("\n$"+wping4)
proc = subprocess.call( wping4 , shell=True)
wping6 = "sudo ping6 -c 5 -m -D -s 1232 -I "+str(args[1])+" www.wide.ad.jp"
#print("\n$"+wping6)
proc = subprocess.call( wping6 , shell=True)
dns4 = "dig www.wide.ad.jp A"
#print("\n$"+dns4)
proc = subprocess.call( dns4 , shell=True)
dns6 = "dig www.wide.ad.jp AAAA"
#print("\n$"+dns6)
proc = subprocess.call( dns6 , shell=True)
trace4 = "traceroute -q1 -w1 -m30 www.wide.ad.jp"
proc = subprocess.call( trace4 , shell=True)
trace6 = "traceroute6 -q1 -w1 -m30 www.wide.ad.jp"
proc = subprocess.call( trace6 , shell=True)
v4web = "open http://www.nicovideo.jp/"
proc = subprocess.call( v4web , shell=True)
v6web = "open https://ipv6.google.com/"
proc = subprocess.call( v6web , shell=True)
