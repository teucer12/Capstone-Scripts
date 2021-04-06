#!/usr/bin/env python3
# Import the subprocess module to run commands in shell
import subprocess

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

# Check if open vm tools is installed
open_vm_tools = subprocess.run("dpkg -s open-vm-tools", capture_output=True, text=True, shell=True)

if "Debian" in os_version.stdout:
    os_debian = True
    pass
if "(ssh) open" in ssh_on.stderr:
    ssh_open = True
    pass
if "sudo" in is_sudo.stdout:
    user_sudo = True
    pass
if "Status: install ok installed" in open_vm_tools.stdout:
    vm_tools = True
    pass


def completion():
    if os_debian and ssh_open and user_sudo and vm_tools is True:
        print("Everything is installed correctly. Great Work!")
    if os_debian is False:
        print("Debian is not installed!")
    if ssh_open is False:
        print("Port 22/SSH is not open!")
    if user_sudo is False:
        print("You are not a sudo user!")
    if vm_tools is False:
        print("Open-vm-tools is not installed!")


completion()