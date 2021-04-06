#!/usr/bin/env python3
# This script will check ITC2480 Lab 11 for successful completion
# Import OS Library
import os
import re

def completion():
    print("-" * 45, "\n" "You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)

done = 0
total = 3

fv = 0

# Define variables in /etc/fstab
fstab = open('/etc/fstab', "r")
fstab2 = open('/etc/fstab', "r")
fst1 = "/dev/sdb1"
fst2 = ['/dev/sdb1', '/mnt/part1', 'ext4', 'defaults', '0', '0']
fst3 = "/dev/sdb2"
fst4 = ['/dev/sdb2', '/mnt/btrfs', 'btrfs', 'defaults', '0', '0']


# Define variables in /proc/mounts
mnt1 = "/dev/sdb1 /mnt/part1 ext4"
mnt2 = "/dev/sdb2 /mnt/btrfs btrfs"

print("-" * 45)

# Check /etc/fstab
for line in fstab:
	if re.match(fst1, line):
		if line.split() == fst2:
			fv = fv + 1

for line2 in fstab2:
	if re.match(fst3, line2):
		if line2.split() == fst4:
			fv = fv + 1

if fv == 2:
	print("Good work, fstab is configured correctly.")
	done = done + 1
else:
	print("Try again, fstab is not configured correctly.")


# Check if sdb1 is mounted
with open("/proc/mounts") as b:
	if mnt1 in b.read():
		print("Good work, sdb1 is mounted.")
		done = done + 1
	else:
		print("Try again, sdb1 is not mounted.")

# Check if sdb2 is mounted
with open("/proc/mounts") as b:
	if mnt2 in b.read():
		print("Good work, sdb2 is mounted.")
		done = done + 1
	else:
		print("Try again, sdb2 is not mounted.")

completion()
