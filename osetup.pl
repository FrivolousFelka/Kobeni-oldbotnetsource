#!/usr/bin/perl

system("yum install php php-mysql");
system("sudo chkconfig httpd on");
system("chkconfig mysqld on");
system("yum install php5 - y");
system("yum install wget");
system("service httpd restart");
system("firewall-cmd --permanent --zone=public --add-service=http");
system("firewall-cmd --permanent --zone=public --add-service=https");
system("firewall-cmd --reload");
system("yum install python3");
system("sudo yum install epel-release");
system("sudo yum install python-pip");
system("python -m pip install --upgrade pip");
system("yum install screen");
system("yum install nano");
system("pip3 install requests");
print "Packages Install...\n";
sleep(2);	
system("yum install httpd mod_ssl");
system("/sbin/chkconfig httpd on");
system("yum install php-mysql php-devel php-gd php-pecl-memcache php-pspell php-snmp php-xmlrpc php-xml");
system("/usr/sbin/apachectl restart");
system("yum install make");
system("yum install gcc");
system("yum install perl");
print "\nL'Installation OK !\n";
print "SSH2 Installation...\n";
sleep(2);	
system("yum install php php-pear libssh2 libssh2-devel");
system("pecl install -f ssh2");
system("touch /etc/php.d/ssh2.ini");
system("echo extension=ssh2.so > /etc/php.d/ssh2.ini");
system("/etc/init.d/httpd restart");
system("pip3 install pysocks");
system("pip3 install bs4");
print "\nVerification...\n";
system("php -m | grep ssh2");
print "If you see ssh2, it works!\n";
system("cd /var/www/html");
system("curl https://ipinfo.io/ip ; echo ");
system("echo http://IPHERE/ddos.php?key=key&host=host&port=port&bytes=power&time=time&method=method");
system("echo Installation Should Be Done Dipshit");
