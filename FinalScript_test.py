#!/usr/bin/env python3
# Import modules used for this script
import subprocess

# Set output file and open it
sbafile = open("sbaOutput.txt", "a+")

# Get the user name and system id (Can be improved. Just a working example!)
STUUSER = "examuser"
hostname =  subprocess.run("cat /etc/hostname", capture_output=True, text=True, shell=True)
STUVMID = hostname.stdout.find("2480-")+5

# Get ip address
IPfull = subprocess.run("ip address show", capture_output=True, text=True, shell=True)
IP = IPfull.stdout[IPfull.stdout.find("inet 172.17.50.") + 15: IPfull.stdout.find("/24")]
STUVMIP = "172.17.50." + IP

blog_url = f"http://{STUVMIP}/blog"


# Define aptcheck for checking installed programs
def aptcheck(installed, command, name):
    if installed in command.stdout:
        print(f"{name} is installed", file=sbafile)
    else:
        print(f"{name} is NOT installed!", file=sbafile)
        subprocess.run(f"apt install -y {name}", capture_output=True, text=True, shell=True, errors='ignore')


# Define simple command for repeated command usage
def simplecommand(command):
    output = subprocess.run(f"{command}", capture_output=True, text=True, shell=True, errors='ignore')
    print(output.stdout.strip(), file=sbafile)


# Define 'ls -al' command for repeated command usage
def lsalcommand(command):
    output = subprocess.run(f"ls -al {command}", capture_output=True, text=True, shell=True, errors='ignore')
    output2 = subprocess.run(f"ls -al {command} | cat -n | head", capture_output=True, text=True, shell=True,
                             errors='ignore')
    output3 = subprocess.run(f"ls -al {command} | cat -n | tail", capture_output=True, text=True, shell=True,
                             errors='ignore')
    if output.stdout.strip() != '':
        print(output.stdout.strip() + "\n" + output2.stdout.strip() + "\n" + output3.stdout.strip(), file=sbafile)
    else:
        print(output.stderr.strip() + "\n" + output2.stderr.strip() + "\n" + output3.stderr.strip(), file=sbafile)


# Define 'locate' command for both head and tails content
def locate(command):
    Files = subprocess.run(f"locate {command}", capture_output=True, text=True, shell=True, errors='ignore')
    for i in Files.stdout.splitlines():
        print(i + " contents:", file=sbafile)
        content = subprocess.run(f"cat -n {i} | head", capture_output=True, text=True, shell=True, errors='ignore')
        content2 = subprocess.run(f"cat -n {i} | tail", capture_output=True, text=True, shell=True, errors='ignore')
        print(content.stdout.strip() + "\n" + content2.stdout.strip(), file=sbafile)


# Define 'locate' command for tail content
def locatetail(command):
    Files = subprocess.run(f"locate {command}", capture_output=True, text=True, shell=True, errors='ignore')
    for i in Files.stdout.splitlines():
        print(i + " contents:", file=sbafile)
        content = subprocess.run(f"cat -n {i} | tail", capture_output=True, text=True, shell=True, errors='ignore')
        print(content.stdout.strip(), file=sbafile)


# Define 'locate' command for both head and tails tar content
def locatetar(command):
    Files = subprocess.run(f"locate {command}", capture_output=True, text=True, shell=True, errors='ignore')
    for i in Files.stdout.splitlines():
        print(i + " contents:", file=sbafile)
        content = subprocess.run(f"tar -ztvf {i} | cat -n | head", capture_output=True, text=True, shell=True,
                                 errors='ignore')
        content2 = subprocess.run(f"tar -ztvf {i} | cat -n | tail", capture_output=True, text=True, shell=True,
                                  errors='ignore')
        print(content.stdout.strip() + "\n" + content2.stdout.strip(), file=sbafile)


# Read "print statments" for info. Wanted to keep things compact. Can update if other people are going to use this!
print("#" * 25 + " BEGIN runtime parameters ##", file=sbafile)
print(f"Student Username: {STUUSER}", file=sbafile)
print(f"Student VM ID: {STUVMID}", file=sbafile)
print(f"Student VM IP: {STUVMIP}", file=sbafile)
print("#" * 25 + " END runtime parameters ##" + "\n\n\n" + "#" * 25 + " BEGIN installed package check ##", file=sbafile)
aptcheck("install",
         subprocess.run("dpkg --get-selections locate", capture_output=True, text=True, shell=True, errors='ignore'),
         "locate")
aptcheck("install",
         subprocess.run("dpkg --get-selections curl", capture_output=True, text=True, shell=True, errors='ignore'),
         "curl")
aptcheck("install",
         subprocess.run("dpkg --get-selections dnsutils", capture_output=True, text=True, shell=True, errors='ignore'),
         "dnsutils")
aptcheck("install",
         subprocess.run("dpkg --get-selections python3", capture_output=True, text=True, shell=True, errors='ignore'),
         "python3")
aptcheck("install", subprocess.run("dpkg --get-selections python3-requests", capture_output=True, text=True, shell=True,
                                   errors='ignore'), "python3-requests")
print("#" * 25 + " END installed package check ##" + "\n\n\n" + "#" * 25 + " BEGIN /etc/hostname output ##",
      file=sbafile)
simplecommand("cat /etc/hostname")
print("#" * 25 + " END /etc/hostname output ##" + "\n\n\n" + "#" * 25 + " BEGIN /etc/passwd output ##", file=sbafile)
simplecommand("cat /etc/passwd | grep linuxgeek")
print("#" * 25 + " END /etc/passwd output ##" + "\n\n\n" + "#" * 25 + " BEGIN /etc/sudoers output ##", file=sbafile)
simplecommand("cat /etc/sudoers | grep linuxgeek")
print("#" * 25 + " END /etc/sudoers output ##" + "\n\n\n" + "#" * 25 + " BEGIN /etc/group output ##", file=sbafile)
simplecommand("cat /etc/group | grep sudo")
simplecommand("cat /etc/group | grep students")
print("#" * 25 + " END /etc/group output ##" + "\n\n\n" +
      "#" * 25 + " BEGIN Line-numbered /home/linuxgeek/recent-log output ##" + "\n" + "There should only be 10 lines!",
      file=sbafile)
locatetail("recent-log")
print(
    "#" * 25 + " END Line-numbered /home/linuxgeek/recent-log output ##" + "\n\n\n" + "#" * 25 + " BEGIN ls -l /home/linuxgeek output ##",
    file=sbafile)
simplecommand("ls -l /home/linuxgeek/")
print(
    "#" * 25 + " END ls -l /home/linuxgeek output ##" + "\n\n\n" + "#" * 25 + f" BEGIN ls -l /home/{STUUSER} output ##",
    file=sbafile)
simplecommand(f"ls -l /home/{STUUSER}/")
print(
    "#" * 25 + f" END ls -l /home/{STUUSER} output ##" + "\n\n\n" + "#" * 25 + f" BEGIN ls -l /home/{STUUSER}/itcfinal output ##",
    file=sbafile)
simplecommand(f"ls -l /home/{STUUSER}/itcfinal/")
print("#" * 25 + f" END ls -l /home/{STUUSER}/itcfinal output ##" + "\n\n\n" +
      "#" * 25 + f" BEGIN Head/Tail of Line-numbered /home/{STUUSER}/itcfinal/kernmsg.txt output ##", file=sbafile)
locate("kernmsg.txt")
print("#" * 25 + f" END Head/Tail of Line-numbered /home/{STUUSER}/itcfinal/kernmsg.txt output ##" + "\n\n\n" +
      "#" * 25 + f" BEGIN Head/Tail of Line-numbered ls -al /home/{STUUSER}/backups/orig-config/ output ##" + "\n" + "ls -al /home/$STUUSER/backups/orig-config/",
      file=sbafile)
lsalcommand(f"/home/{STUUSER}/backups/orig-config/")
print("\n\n" + "ls -al /home/$STUUSER/backups/orig-config/etc/", file=sbafile)
lsalcommand(f"/home/{STUUSER}/backups/orig-config/etc/")
print("#" * 25 + f" END Head/Tail of Line-numbered ls -al /home/{STUUSER}/backups/orig-config/ output ##" + "\n\n\n" +
      "#" * 25 + f" BEGIN Tail of Line-numbered /home/{STUUSER}/backups/system-users output ##", file=sbafile)
locatetail("system-users | grep -E 'home|root'")
print("#" * 25 + f" END Tail of Line-numbered /home/{STUUSER}/backups/system-users output ##" + "\n\n\n" +
      "#" * 25 + f" BEGIN Head/Tail of Line-numbered /home/{STUUSER}/itcfinal/systemlogs.tar.gz output ##",
      file=sbafile)
locatetar("systemlogs.tar.gz")
print("#" * 25 + f" END Head/Tail of Line-numbered /home/{STUUSER}/itcfinal/systemlogs.tar.gz output ##" + "\n\n\n" +
      "#" * 25 + " BEGIN Softlink Check on /home/linuxgeek/itcfinal-backups ##", file=sbafile)
print("ls -al /home/linuxgeek/", file=sbafile)
simplecommand("ls -al /home/linuxgeek/ | head")
print("ls -al /home/linuxgeek/itcfinal-backups", file=sbafile)
simplecommand("ls -al /home/linuxgeek/itcfinal-backups | head")
print(
    "#" * 25 + " END Softlink Check on /home/linuxgeek/itcfinal-backups ##" + "\n\n\n" + "#" * 25 + " BEGIN ifconfig output ##",
    file=sbafile)
simplecommand("ifconfig")
print("#" * 25 + " END ifconfig output ##" + "\n\n\n" + "#" * 25 + " BEGIN check apache installed ##", file=sbafile)
simplecommand("dpkg -s apache2 2>&1 | head -2")
simplecommand("dpkg -s php 2>&1 | head -2")
simplecommand("dpkg -s php-mysql 2>&1 | head -2")
simplecommand("dpkg -s libapache2-mod-php 2>&1 | head -2")
simplecommand("dpkg -s mariadb-server 2>&1 | head -2")
simplecommand("dpkg -s wordpress 2>&1 | head -2")
print(
    "#" * 25 + " END check apache installed ##" + "\n\n\n" + "#" * 25 + " BEGIN Webserver content check ##" + "\n" + "ls -l /var/www",
    file=sbafile)
simplecommand("ls -l /var/www")
print("\n" + "ls -l /var/www/html", file=sbafile)
simplecommand("ls -l /var/www/html")
print("\n" + "ls -l /var/www/html/blog", file=sbafile)
simplecommand("ls /var/www/html/blog")
print("###CURL OUTPUT###" + "\n" + f"Site Title: ", file=sbafile)
simplecommand(f'curl -s {STUVMIP}/blog/ | grep -o "<title>[^<]*" | tail -c+8')
print("\n" + "Entry Titles: ", file=sbafile)
simplecommand(f"curl -s {STUVMIP}/blog/ | grep -o -P '(?<=<h. class=\"entry-title heading-size-1\">).*(?=</h.>)'")
print("#" * 25 + " END Webserver content check ##" + "\n\n\n" + "#" * 25 + " BEGIN fdisk -l /dev/sdb output ##",
      file=sbafile)
simplecommand("fdisk -l /dev/sdb")
print(
    "#" * 25 + " END fdisk -l /dev/sdb output ##" + "\n\n\n" + "#" * 25 + " BEGIN listing of filesystems on /dev/sdb ##",
    file=sbafile)
simplecommand("file -sL /dev/sdb*")
print("\n\n", "#" * 25, " END listing of filesystems on /dev/sdb ##", "\n\n", "#" * 25, " BEGIN listing of mounts ##",
      file=sbafile)
simplecommand("mount 2>&1 | grep sd")
print("#" * 25 + " END listing of mounts ##" + "\n\n\n" + "#" * 25 + " BEGIN listing of fstab ##", file=sbafile)
simplecommand("cat /etc/fstab")
print("#" * 25 + " END listing of fstab ##" + "\n\n\n" + "#" * 25 + " BEGIN check samba installed ##", file=sbafile)
simplecommand("dpkg -s samba 2>&1 | head -2")
print("#" * 25 + " END check samba installed ##" + "\n\n\n" + "#" * 25 + " BEGIN tail samba config ##", file=sbafile)
simplecommand("tail -20 /etc/samba/smb.conf")
print("#" * 25 + " END tail samba config ##" + "\n\n\n" + "#" * 25 + " BEGIN windows file share check ##", file=sbafile)
simplecommand(f"ls -l /home/{STUUSER}/Windows\ File\ Test/")
print(
    "#" * 25 + " END windows file share check ##" + "\n\n\n" + "#" * 25 + " BEGIN permissions check on /winshare/students ##",
    file=sbafile)
simplecommand("ls -al /winshare/students")
print(
    "#" * 25 + " END permissions check on /winshare/students ##" + "\n\n\n" + "#" * 25 + " BEGIN check bind installed ##",
    file=sbafile)
simplecommand("dpkg -s bind9 2>&1 | head -2")
print("#" * 25 + " END check bind installed ##" + "\n\n\n" + "#" * 25 + " BEGIN caching nameserver check ##",
      file=sbafile)
simplecommand("nslookup google.com 127.0.0.1")
print("#" * 25 + " END caching nameserver check ##" + "\n\n\n" + "#" * 25 + f" BEGIN zone sba-{STUVMID} checks ##",
      file=sbafile)
simplecommand(f"nslookup sba-{STUVMID}.itc2480.campus.ihitc.net 127.0.0.1")
simplecommand(f"nslookup mymachine.sba-{STUVMID}.itc2480.campus.ihitc.net 127.0.0.1")
simplecommand(f"nslookup mailserver.sba-{STUVMID}.itc2480.campus.ihitc.net 127.0.0.1")
simplecommand(f"nslookup www.sba-{STUVMID}.itc2480.campus.ihitc.net 127.0.0.1")
simplecommand(f"nslookup -q=MX sba-{STUVMID}.itc2480.campus.ihitc.net 127.0.0.1")
simplecommand(f"cat /var/lib/bind/sba-{STUVMID}.itc2480.campus.ihitc.net.hosts")
print("#" * 25 + " END zone checks ##" + "\n\n\n" + "#" * 25 + " BEGIN DHCP config tail ##", file=sbafile)
simplecommand("cat /etc/dhcp/dhcpd.conf 2>&1 | tail")
print("#" * 25 + " END DHCP config tail ##" + "\n\n\n" + "#" * 25 + " BEGIN firewalld config ##", file=sbafile)
simplecommand("firewall-cmd --list-all-zones")
print("#" * 25 + " END firewalld config ##" + "\n\n\n" + "#" * 25 + " BEGIN iptables FW config ##", file=sbafile)
simplecommand("iptables-legacy -L")
print("#" * 25 + " END iptables FW config ##" + "\n\n\n" + "#" * 25 + " BEGIN iptables NAT config ##", file=sbafile)
simplecommand("iptables-legacy -t nat -L -n -v")
print("#" * 25 + " END iptables NAT config ##" + "\n\n\n" + "#" * 25 + " BEGIN IP ROUTING config ##", file=sbafile)
simplecommand("sysctl net.ipv4.ip_forward")
print("#" * 25 + " END IP ROUTING config ##" + "\n\n\n" + "#" * 25 + " BEGIN script listing ##", file=sbafile)
myscript = subprocess.run("locate myscript", capture_output=True, text=True, shell=True)
for i in myscript.stdout.splitlines():
    print(i + " Contents:", file=sbafile)
    content = subprocess.run(f"ls -l {i}", capture_output=True, text=True, shell=True, errors='ignore')
    content2 = subprocess.run(f"cat {i}", capture_output=True, text=True, shell=True, errors='ignore')
    print(content.stdout.strip(), content2.stdout.strip(), file=sbafile)
print("#" * 25 + "END script listing ##", file=sbafile)

sbafile.close()

sbafile2 = open("sbaOutput.txt", "r")

output = sbafile2.read()
print(output)
