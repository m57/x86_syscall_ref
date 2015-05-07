#!/usr/bin/env python
#
# A simple console interface for SYSCALL Referencing
# by:	@__0x57__ / m57
#
# Thanks must go out to http://syscalls.kernelgrok.com/ as
# the data for sys call references has come from this site! 
# (Greg Ose)
#
# It has been created so that if you are without internet connection
# Or you simply wish to reference syscalls without a browser
# you can do so with your command line.
#
###########################################################

import sys

def banner():
	print "+======> Unix 32_bit syscall reference <======+"
	print "________________________________________ ~\\x90__"

columns = ["#", "Name", "eax", "ebx", "ecx", "edx", "esi", "edi", "Definition"]
names = []
f = open("syscall_data.txt", "r")
data = f.read()
f.close()
raw = data.decode("base64")
raw_newline = raw.split("\n")
raw_split = []

for i in raw_newline:
	raw_split.append(i.split("\t"))

raw_split.pop(len(raw_split)-1)
for i in raw_split:
	names.append(i[1])

def get_sys(int, sys_call, index):
	print "\n"	
	if int == -1:
		count = 0
		for i in raw_split[sys_call]:
			print "\033[1;94m"+columns[count] + "\033[0m : " + i	
			count = count + 1
	else:
		count = 0
		for i in raw_split[index]:
			print "\033[1;94m"+columns[count] + "\033[0m : " + i	
			count = count + 1


def do_console():

	while True:
		sys = raw_input("\033[1;92msyscall # or alias #\033[0m ")
		count = 0

		try:
			if int(sys) >= 0 and int(sys) < 338:
				get_sys(-1, int(sys), -1)

		except:
			for i in names:
				if sys in i:
					get_sys(count, sys, count)
				count = count + 1


banner()
do_console()
