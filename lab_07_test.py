#!/usr/bin/env python3
# This script will check ITC2480 Lab 7 for successful completion
# Import OS Library
import os.path
from os import path

def completion():
    print("-" * 45, "\n" "You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)

done = 0
total = 4

# Define directories to check
grp = os.path.expanduser("/srv/Group-Share")
gst = os.path.expanduser("/srv/Guest-Files")

print("-" * 45)

# Check to see if Group Share exists
if os.path.exists(grp):
	print("Good work. The Group Share exists.")
	done = done + 1
	if oct(os.stat(grp).st_mode & 0o777) == "0o777":
		print("Good work. The Group Share has correct permissions.")
		done = done + 1
	else:
		print("Try again. The Group Share has inccorrect permissions.")
else:
	print("Try again. The Group Share was not created correctly.")
	print("Try again. Could not check permissions on Group Share.")

# Check to see if Guest Share exists
if os.path.exists(gst):
	print("Good work. The Guest Share exists.")
	done = done + 1
	if oct(os.stat(gst).st_mode & 0o777) == "0o755":
		print("Good work. The Guest Share has correct permissions.")
		done = done + 1
	else:
		print("Try again. The Guest Share has incorrect permissions.")
else:
	print("Try again. The Guest Share was not created correctly.")
	print("Try again. Could not check permissions on Guest Share.")

completion()
