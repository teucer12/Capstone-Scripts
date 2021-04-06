#!/bin/bash
# Store on pastebin and then run like below (sed removes DOS newlines)
# wget https://pastebin.com/raw/fSWWy5T8 -qO- | sed 's/\r$//' > ca.sh; chmod u+x ca.sh; ./ca.sh
#
#ls -l /home
#echo Enter Username:
#read STUUSER
STUUSER="examuser"
echo Enter System ID:
read STUVMID
apt update
STUVMIP=`/sbin/ip -4 -o addr show dev ens192| awk '{split($4,a,"/");print a[1]}'`
echo Detected IP Address: $STUVMIP
echo Blog Check URL: http://$STUVMIP/blog
touch sbaOutput.txt
echo "######################### BEGIN runtime parameters ##" > sbaOutput.txt 2>&1
echo Student Username: $STUUSER >> sbaOutput.txt 2>&1
echo Student VM ID: $STUVMID >> sbaOutput.txt 2>&1
echo Student VM IP: $STUVMIP >> sbaOutput.txt 2>&1
echo "######################### END runtime parameters ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN installed package check ##" >> sbaOutput.txt 2>&1
if dpkg --get-selections | grep -q "^locate[[:space:]]*install$" >/dev/null; then
	echo -e "locate is already installed"  >> sbaOutput.txt 2>&1
else
	apt install -y locate
	updatedb
fi
if dpkg --get-selections | grep -q "^curl[[:space:]]*install$" >/dev/null; then
	echo -e "curl is already installed"  >> sbaOutput.txt 2>&1
else
	echo -e "curl is NOT installed"  >> sbaOutput.txt 2>&1
	apt install -y curl
fi
if dpkg --get-selections | grep -q "^dnsutils[[:space:]]*install$" >/dev/null; then
	echo -e "dnsutils is already installed"  >> sbaOutput.txt 2>&1
else
	echo -e "dnsutils is NOT installed"  >> sbaOutput.txt 2>&1
	apt install -y dnsutils
fi
if dpkg --get-selections | grep -q "^python3[[:space:]]*install$" >/dev/null; then
	echo -e "python3 is already installed"  >> sbaOutput.txt 2>&1
else
	echo -e "python3 is NOT installed"  >> sbaOutput.txt 2>&1
	apt install -y python3
fi
if dpkg --get-selections | grep -q "^python3-requests[[:space:]]*install$" >/dev/null; then
	echo -e "python3-requests is already installed"  >> sbaOutput.txt 2>&1
else
	echo -e "python3-requests is NOT installed"  >> sbaOutput.txt 2>&1
	apt install -y python3-requests
fi
echo "######################### END installed package check ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN /etc/hostname output ##" >> sbaOutput.txt 2>&1
cat /etc/hostname >> sbaOutput.txt 2>&1
echo "######################### END /etc/hostname output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN /etc/passwd output ##" >> sbaOutput.txt 2>&1
cat /etc/passwd 2>&1 | grep linuxgeek >> sbaOutput.txt 2>&1
echo "######################### END /etc/passwd output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN /etc/sudoers output ##" >> sbaOutput.txt 2>&1
cat /etc/sudoers 2>&1 | grep linuxgeek >> sbaOutput.txt 2>&1
echo "######################### END /etc/sudoers output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN /etc/group output ##" >> sbaOutput.txt 2>&1
cat /etc/group 2>&1 | grep sudo >> sbaOutput.txt 2>&1
cat /etc/group 2>&1 | grep students >> sbaOutput.txt 2>&1
echo "######################### END /etc/group output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN Line-numbered /home/linuxgeek/recent-log output ##" >> sbaOutput.txt 2>&1
echo There should only be 10 lines! >> sbaOutput.txt 2>&1
FILES=`locate recent-log`
for f in $FILES
do
	echo $f contents: >> sbaOutput.txt 2>&1
	cat -n $f 2>&1 | tail >> sbaOutput.txt 2>&1
done
echo "######################### END Line-numbered /home/linuxgeek/recent-log output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN ls -l /home/linuxgeek output ##" >> sbaOutput.txt 2>&1
ls -l /home/linuxgeek/ >> sbaOutput.txt 2>&1
echo "######################### END ls -l /home/linuxgeek output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN ls -l /home/$STUUSER output ##" >> sbaOutput.txt 2>&1
ls -l /home/$STUUSER/ >> sbaOutput.txt 2>&1
echo "######################### END ls -l /home/$STUUSER output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN ls -l /home/$STUUSER/itcfinal output ##" >> sbaOutput.txt 2>&1
ls -l /home/$STUUSER/itcfinal/ >> sbaOutput.txt 2>&1
echo "######################### END ls -l /home/$STUUSER/itcfinal output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN Head/Tail of Line-numbered /home/$STUUSER/itcfinal/kernmsg.txt output ##" >> sbaOutput.txt 2>&1
FILES=`locate kernmsg.txt`
for f in $FILES
do
	echo $f contents: >> sbaOutput.txt 2>&1
	cat -n $f 2>&1 | head >> sbaOutput.txt 2>&1
	cat -n $f 2>&1 | tail >> sbaOutput.txt 2>&1
done
echo "######################### END Head/Tail of Line-numbered /home/$STUUSER/itcfinal/kernmsg.txt output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN Head/Tail of Line-numbered ls -al /home/$STUUSER/backups/orig-config/ output ##" >> sbaOutput.txt 2>&1
echo ls -al /home/$STUUSER/backups/orig-config/ >> sbaOutput.txt 2>&1
ls -al /home/$STUUSER/backups/orig-config/ 2>&1 | cat -n | head >> sbaOutput.txt 2>&1
ls -al /home/$STUUSER/backups/orig-config/ 2>&1 | cat -n | tail >> sbaOutput.txt 2>&1
echo -e "\n" >> sbaOutput.txt 2>&1
echo ls -al /home/$STUUSER/backups/orig-config/etc/ >> sbaOutput.txt 2>&1
ls -al /home/$STUUSER/backups/orig-config/etc/ 2>&1 | cat -n | head >> sbaOutput.txt 2>&1
ls -al /home/$STUUSER/backups/orig-config/etc/ 2>&1 | cat -n | tail >> sbaOutput.txt 2>&1
echo "######################### END Head/Tail of Line-numbered ls -al /home/$STUUSER/backups/orig-config/ output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN Tail of Line-numbered /home/$STUUSER/backups/system-users output ##" >> sbaOutput.txt 2>&1
FILES=`locate system-users | grep -E 'home|root'`
for f in $FILES
do
	echo $f contents: >> sbaOutput.txt 2>&1
	cat -n $f 2>&1 | tail >> sbaOutput.txt 2>&1
done
echo "######################### END Tail of Line-numbered /home/$STUUSER/backups/system-users output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN Head/Tail of Line-numbered /home/$STUUSER/itcfinal/systemlogs.tar.gz output ##" >> sbaOutput.txt 2>&1
FILES=`locate systemlogs.tar.gz`
for f in $FILES
do
	echo $f contents: >> sbaOutput.txt 2>&1
	tar -ztvf $f  2>&1 | cat -n | head >> sbaOutput.txt 2>&1
	tar -ztvf $f  2>&1 | cat -n | tail >> sbaOutput.txt 2>&1
done
echo "######################### END Head/Tail of Line-numbered /home/$STUUSER/itcfinal/systemlogs.tar.gz output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN Softlink Check on /home/linuxgeek/itcfinal-backups ##" >> sbaOutput.txt 2>&1
echo ls -al /home/linuxgeek/ >> sbaOutput.txt 2>&1
ls -al /home/linuxgeek/ 2>&1 | head >> sbaOutput.txt 2>&1
echo ls -al /home/linuxgeek/itcfinal-backups >> sbaOutput.txt 2>&1
ls -al /home/linuxgeek/itcfinal-backups 2>&1 | head >> sbaOutput.txt 2>&1
echo "######################### END Softlink Check on /home/linuxgeek/itcfinal-backups ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN ifconfig output ##" >> sbaOutput.txt 2>&1
ifconfig >> sbaOutput.txt 2>&1
echo "######################### END ifconfig output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN check apache installed ##" >> sbaOutput.txt 2>&1
dpkg -s apache2 2>&1 | head -2 >> sbaOutput.txt 2>&1
dpkg -s php 2>&1 | head -2 >> sbaOutput.txt 2>&1
dpkg -s php-mysql 2>&1 | head -2 >> sbaOutput.txt 2>&1
dpkg -s libapache2-mod-php 2>&1 | head -2 >> sbaOutput.txt 2>&1
dpkg -s mariadb-server 2>&1 | head -2 >> sbaOutput.txt 2>&1
dpkg -s wordpress 2>&1 | head -2 >> sbaOutput.txt 2>&1
echo "######################### END check apache installed ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN Webserver content check ##" >> sbaOutput.txt 2>&1
echo ls -l /var/www >> sbaOutput.txt 2>&1
ls -l /var/www >> sbaOutput.txt 2>&1
echo ls -l /var/www/html >> sbaOutput.txt 2>&1
ls -l /var/www/html >> sbaOutput.txt 2>&1
echo ls /var/www/html/blog >> sbaOutput.txt 2>&1
ls /var/www/html/blog >> sbaOutput.txt 2>&1
echo "###CURL OUTPUT###" >> sbaOutput.txt 2>&1
WPSITETITLE=`curl -s $STUVMIP/blog/ | grep -o "<title>[^<]*" | tail -c+8`
echo Site Title: $WPSITETITLE >> sbaOutput.txt 2>&1
echo Entry Titles:  >> sbaOutput.txt 2>&1
curl -s $STUVMIP/blog/ | grep -o -P '(?<=<h. class=\"entry-title heading-size-1\">).*(?=</h.>)' >> sbaOutput.txt 2>&1
echo "######################### END Webserver content check ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN fdisk -l /dev/sdb output ##" >> sbaOutput.txt 2>&1
fdisk -l /dev/sdb >> sbaOutput.txt 2>&1
echo "######################### END fdisk -l /dev/sdb output ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN listing of filesystems on /dev/sdb ##" >> sbaOutput.txt 2>&1
file -sL /dev/sdb* >> sbaOutput.txt 2>&1
echo "######################### END listing of filesystems on /dev/sdb ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN listing of mounts ##" >> sbaOutput.txt 2>&1
mount 2>&1 | grep sd >> sbaOutput.txt 2>&1
echo "######################### END listing of mounts ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN listing of fstab ##" >> sbaOutput.txt 2>&1
cat /etc/fstab >> sbaOutput.txt 2>&1
echo "######################### END listing of fstab ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN check samba installed ##" >> sbaOutput.txt 2>&1
dpkg -s samba 2>&1 | head -2 >> sbaOutput.txt 2>&1
echo "######################### END check samba installed ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN tail samba config ##" >> sbaOutput.txt 2>&1
tail -20 /etc/samba/smb.conf >> sbaOutput.txt 2>&1
echo "######################### END tail samba config ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN windows file share check ##" >> sbaOutput.txt 2>&1
ls -l "/home/$STUUSER/Windows File Test/" >> sbaOutput.txt 2>&1
echo "######################### END windows file share check ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN permissions check on /winshare/students ##" >> sbaOutput.txt 2>&1
ls -al /winshare/students >> sbaOutput.txt 2>&1
echo "######################### END permissions check on /winshare/students ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN check bind installed ##" >> sbaOutput.txt 2>&1
dpkg -s bind9 2>&1 | head -2 >> sbaOutput.txt 2>&1
echo "######################### END check bind installed ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN caching nameserver check ##" >> sbaOutput.txt 2>&1
nslookup google.com 127.0.0.1 >> sbaOutput.txt 2>&1
echo "######################### END caching nameserver check ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN zone sba-$STUVMID checks ##" >> sbaOutput.txt 2>&1
nslookup sba-$STUVMID.itc2480.campus.ihitc.net 127.0.0.1 >> sbaOutput.txt 2>&1
nslookup mymachine.sba-$STUVMID.itc2480.campus.ihitc.net 127.0.0.1 >> sbaOutput.txt 2>&1
nslookup mailserver.sba-$STUVMID.itc2480.campus.ihitc.net 127.0.0.1 >> sbaOutput.txt 2>&1
nslookup www.sba-$STUVMID.itc2480.campus.ihitc.net 127.0.0.1 >> sbaOutput.txt 2>&1
nslookup -q=MX sba-$STUVMID.itc2480.campus.ihitc.net 127.0.0.1 >> sbaOutput.txt 2>&1
cat /var/lib/bind/sba-$STUVMID.itc2480.campus.ihitc.net.hosts >> sbaOutput.txt 2>&1
cat /var/lib/bind/sba-${STUVMID^^}.itc2480.campus.ihitc.net.hosts >> sbaOutput.txt 2>&1
echo "######################### END zone checks ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN DHCP config tail ##" >> sbaOutput.txt 2>&1
cat /etc/dhcp/dhcpd.conf 2>&1 | tail >> sbaOutput.txt 2>&1
echo "######################### END DHCP config tail ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN firewalld config ##" >> sbaOutput.txt 2>&1
firewall-cmd --list-all-zones >> sbaOutput.txt 2>&1
echo "######################### END firewalld config ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN iptables FW config ##" >> sbaOutput.txt 2>&1
iptables-legacy -L >> sbaOutput.txt 2>&1
echo "######################### END iptables FW config ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN iptables NAT config ##" >> sbaOutput.txt 2>&1
iptables-legacy -t nat -L -n -v >> sbaOutput.txt 2>&1
echo "######################### END iptables NAT config ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN IP ROUTING config ##" >> sbaOutput.txt 2>&1
sysctl net.ipv4.ip_forward >> sbaOutput.txt 2>&1
echo "######################### END IP ROUTING config ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1
echo "######################### BEGIN script listing ##" >> sbaOutput.txt 2>&1
FILES=`locate myscript`
for f in $FILES
do
	ls -l $f >> sbaOutput.txt 2>&1
	echo $f contents: >> sbaOutput.txt 2>&1
	cat $f >> sbaOutput.txt 2>&1
done
echo "######################### END script listing ##" >> sbaOutput.txt 2>&1
echo -e "\n\n" >> sbaOutput.txt 2>&1