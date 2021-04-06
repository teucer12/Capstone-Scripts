#!/usr/bin/env python3
# Import the subprocess module to run commands in shell
import subprocess


print("-" * 45)

def completion():
    print("-" * 45, "\n" "You have completed", str(done), "out of 7 tasks for this lab!")
    if done == 7:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)
    else:
        print("-" * 45)

done = 0

# Used for telling the user what is installed and not installed at the end
os_debian = False
ssh_open = False
user_sudo = False
vm_tools = False

# Auto grab username of currently logged in user
who_output = subprocess.run("who", capture_output=True, text=True, shell=True)
who_split = who_output.stdout.split()
username = str(who_split[0])

# Check if debian is installed
os_version = subprocess.run("cat /etc/issue", capture_output=True, text=True, shell=True)

# Check if localhost has port 22 open
ssh_on = subprocess.run("nc -z -v localhost 22", capture_output=True, text=True, shell=True)

# Grab a list of groups current user is in
is_sudo = subprocess.run("groups " + username, capture_output=True, text=True, shell=True)

# Check if apps are installed
def appcheck(apptocheck):
    appname = subprocess.run("dpkg -s "+apptocheck, capture_output=True, text=True, shell=True)
    return appname.stdout

if "Debian" in os_version.stdout:
    print("OS is Debian Buster")
    done = done + 1
else:
    print("Debian is not installed!")

if "(ssh) open" in ssh_on.stderr:
    print("SSH port has been opened")
    done = done + 1
else:
    print("Port 22/SSH is not open!")

if "sudo" in is_sudo.stdout:
    print(username + " can execute commands with sudo.")
    done = done + 1
else:
    print("You are not a sudo user!")

apps = {"open-vm-tools", "python3", "curl", "nmap"}
for apptocheck in apps:
    appname = appcheck(apptocheck)
    if "Status: install ok installed" in appname:
        print("You have installed "+apptocheck)
        done = done + 1
    else:
        print(apptocheck+" is not installed!")


completion()
