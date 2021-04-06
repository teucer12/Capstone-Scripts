#!/usr/bin/env python3
import subprocess
# Could use regex in this to check domains ([A-Za-z0-9]+.itc2480.campus.ihitc.net)

done = 0
bind_options = subprocess.run("cat /etc/bind/named.conf.options", capture_output=True, text=True, shell=True)
interfaces = subprocess.run("cat /etc/network/interfaces", capture_output=True, text=True, shell=True)
host = subprocess.run("cat /var/lib/bind/*.itc2480.campus.ihitc.net.hosts", capture_output=True, text=True, shell=True)
print("-" * 45)


def completion():
    print("-" * 45, "\n" "You have completed", str(done), "out of 3 tasks for this lab!")
    if done == 3:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)


if "172.17.139.11" in bind_options.stdout:
    print("Good work. Bind file has ip 172.17.139.11 stored in it!")
    done += 1
else:
    print("Bind file has wrong ip address stored!")

if "127.0.0.1" in interfaces.stdout:
    print("Good work. Interfaces file has ip 127.0.0.1 stored in it!")
    done += 1
else:
    print("Interfaces file has wrong ip address stored!")

if "MX" and "CNAME" and "AAAA" in host.stdout:
    print("Good work. Mail, CNAME, and IPv6 address found in bind hosts file!")
    done += 1
else:
    print("Missing MX, CNAME, or IPv6 address in your DNS settings for the 'itc2480.campus.ihitc.net.' domain!")

completion()
