#!/usr/bin/env python3
# This script will check ITC2480 Lab 2 for successful completion
# Import OS Library
import os.path
from os import path

def completion():
    print("-" * 45, "\n" "You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)

done = 0
total = 4

# Define directories and tar file to check
html = os.path.expanduser("/var/www/html")
dir1 = os.path.expanduser("~/sample-files/Shakespeare")
dir2 = os.path.expanduser("~/sample-files")
tar = os.path.expanduser("~/sample-files/shakespeare.tar.gz")

print("-" * 45)

# Check to see if Shakespeare directory exists
if os.path.exists(dir1):
	print("Try again. The ~/sample-files/Shakespeare directory should have been deleted.")
else:
	print("Good work. The ~/sample-files/Shakespeare directory was successfully deleted.")
	done = done + 1

# Check to see if sample-files directory exists
if os.path.exists(dir2):
	print("Good work. The ~/sample-files directory exists.")
	done = done + 1
else:
	print("Try again. The ~/sample-files directory does not exist.")

# Check to see if shakespeare.tar.gz exists
if os.path.exists(tar):
	print("Good work. The ~/sample-files/shakespeare.tar.gz file exists.")
	done = done + 1
else:
	print("Try again. The ~/sample-files/shakespeare.tar.gz file does not exist.")

# Check to see if Apache is installed correctly
if os.path.exists(html):
        print("Good work. Apache was installed.")
        done = done + 1
else:
        print("Try again. Apache was not installed.")

completion()
