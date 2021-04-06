#!/usr/bin/env python3
# Import the subprocess module to run commands in shell
import subprocess

print("-" * 45)
# Used for telling the user what is installed and not installed at the end
# directories_present = False
# redteam_ours = False
# redteam_redteam = False
webmin = False

def completion():
    print("-" * 45, "\n" "You have completed", str(done), "out of 4 tasks for this lab!")
    if done == 4:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)
    else:
        print("-" * 45)

done = 0

# grab directory listing of redteam
redteam_directory = subprocess.run("ls -al /home/jsmith/redteam", capture_output=True, text=True, shell=True)

# grab appropriate values for redteam and ours
ours = subprocess.run("stat -c %G /home/jsmith/redteam/ours", capture_output=True, text=True, shell=True)

# grab directory listing of jsmith
redteam = subprocess.run("stat -c %G /home/jsmith/redteam", capture_output=True, text=True, shell=True)

# check webmin installation and format the data
# webmin_search = subprocess.run("apt-cache policy webmin", capture_output=True, text=True, shell=True)
webmin_version = subprocess.run("apt-cache policy webmin", capture_output=True, text=True, shell=True)
try:
    webmin_installed = webmin_version.stdout.splitlines()[1]
    webmin_latest = webmin_version.stdout.splitlines()[2]
    webmin_installed = webmin_installed.split()[1]
    webmin_latest = webmin_latest.split()[1]
except IndexError:
    pass

#check completion of tasks
if "theplan" and "yours" and "mine" and "ours" in redteam_directory.stdout:
    print("All directories successfully created!")
    done = done + 1
else:
    print("Some required directories are missing.")

if ours.stdout.strip() == "redteam":
    print("redteam owns /home/jsmith/redteam/ours")
    done = done + 1
else:
    print("redteam is not the owner of /home/jsmith/redteam/ours.")

if redteam.stdout.strip() == 'redteam':
    print("redteam owns /home/jsmith/redteam")
    done = done + 1
else:
    print("redteam is not the owner of /home/jsmith/redteam.")

try:
    if webmin_latest == webmin_installed:
        print("You have installed Webmin")
        done = done + 1
        pass
except NameError:
    print("Webmin is not installed correctly.")

completion()
