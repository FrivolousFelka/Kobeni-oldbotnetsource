#!/usr/bin/perl

#centos 7 
system("rm /var/log/lastlog");
system("yum install python3");
system("sudo yum install epel-release");
system("sudo yum install python-pip");

system("python -m pip install --upgrade pip");
system("yum install screen");
system("yum install nano");
system("pip3 install requests");
system("Installation Should Be Done Farthead");


