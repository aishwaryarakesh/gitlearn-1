#!/usr/bin/env python3
import os
import shutil
import sys

def check_reboot();
	"""Returns true if the computer has a pending reboot"""
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_abs, min_percent):
	"""Returns True if there is not enough disk space"""
	du = shutil.disk_usage(disk)
	#Calculate the percent of free space
	percent_free = 100 * du.free / du.total
	#Calculate how manu free gigabytes
	gigabytes_free = du.free /2**30
	if percent_free < min_percent or gigabytes_free < min_abs:
		return True
	return False

def main():
	if check_reboot():
		print("Pending reboot")
		sys.exit(1)
	if check_disk_full("/",2,10):
		print("disk full")
		sys.exit(1)
main()
