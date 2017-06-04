#!/usr/bin/env python

from __future__ import print_function
import sys
import subprocess
try:
	from subprocess import getoutput
except:
	from commands import getoutput

import re

args = sys.argv

#ifconfig
ifconfig = "ifconfig "+str(args[1])
print("$"+ifconfig)
sys.stdout.flush()
proc = subprocess.call( ifconfig , shell=True)

#get ipv4 address
v4ifconfig = "ifconfig "+str(args[1])+" |grep 'inet\s'"
v4inet = getoutput(v4ifconfig)
<<<<<<< HEAD
if v4inet != "" and re.match('ifconfig:\s\w+',v4inet) == None:
	v4address = v4inet.split(" ")
	print("\nipv4 address: "+v4address[1])
	sys.stdout.flush()
else:
	print("\nipv4 address: NG")
	sys.stdout.flush()
=======
v4address = v4inet.split(" ")
print("\nipv4 address: "+v4address[1])
v6ifconfig = "ifconfig "+str(args[1])+" |grep 'inet6 2001'"
v6inet = getoutput(v6ifconfig)
v6address = v6inet.split(" ")
print("\nipv6 address: "+v6address[1])
>>>>>>> 95aea9459a63ec4cfa1a913a8ec142c36a2a11cd

#get ipv6 address
v6ifconfig = "ifconfig "+str(args[1])+" |grep 'inet6 2001'"
v6inet = getoutput(v6ifconfig)
if v6inet != "" and re.match('ifconfig:\s\w+',v6inet) == None:
	v6address = v6inet.split(" ")
	print("ipv6 address: "+v6address[1])
	sys.stdout.flush()
else:
	print("ipv6 address: NG")
	sys.stdout.flush()

#get v4default gateway
netstat = "netstat -rn |grep default |grep "+str(args[1])
default = getoutput(netstat)
line = default.split('\n')
if line[0] != "":
	v4addr = re.split('\s+',str(line[0]))
	v4gw = v4addr[1]
else:
	v4gw = "NG"
print("ipv4 gateway: "+v4gw)
sys.stdout.flush()

#get v6default gateway
if len(line) > 1:
	v6addr = re.split('\s+',str(line[1]))
	word = v6addr[1].split('%')
	v6gw = word[0]
else:
	v6gw = "NG"
print("ipv6 gateway: "+v6gw)
sys.stdout.flush()

#v4 ping gateway
if v4gw != "NG":
	iping4 = "ping -c 5 -D -s 1472 "+v4gw
	print("\n$"+iping4)
	sys.stdout.flush()
	proc = subprocess.call( iping4 , shell=True)

#v6 ping gateway
if v6gw != "NG":
	iping6 = "sudo ping6 -c 5 -m -D -s 1232 -I "+str(args[1])+" "+v6gw
	print("\n$"+iping6)
	sys.stdout.flush()
	proc = subprocess.call( iping6 , shell=True)

#v4 ping pubdns
wping4 = "ping -c 5 -D -s 1472 8.8.8.8"
print("\n$"+wping4)
sys.stdout.flush()
proc = subprocess.call( wping4 , shell=True)

#v6 ping pubdns
wping6 = "sudo ping6 -c 5 -m -D -s 1232 -I "+str(args[1])+" 2001:4860:4860::8888"
print("\n$"+wping6)
sys.stdout.flush()
proc = subprocess.call( wping6 , shell=True)

#v4 dig
dns4 = "dig www.wide.ad.jp A"
print("\n$"+dns4)
sys.stdout.flush()
proc = subprocess.call( dns4 , shell=True)

#v6 dig
dns6 = "dig www.wide.ad.jp AAAA"
print("\n$"+dns6)
sys.stdout.flush()
proc = subprocess.call( dns6 , shell=True)

#v4 traceroute
trace4 = "traceroute -q1 -w1 -m30 -I 8.8.8.8"
print("\n$"+trace4)
sys.stdout.flush()
proc = subprocess.call( trace4 , shell=True)

#v6 traceroute
trace6 = "traceroute6 -q1 -w1 -m30 -I 2001:4860:4860::8888"
print("\n$"+trace6)
sys.stdout.flush()
proc = subprocess.call( trace6 , shell=True)
