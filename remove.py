#!/bin/env python3
import sys,readline
path=""
output=""
text=""
usage="""
NAME
       remove.py

SYNOPSIS
       ./remove.py [INPUT FILE] [OUTPUT] [string] 
       python3 remove.py [INPUT FILE] [OUTPUT] [string]

DESCRIPTION
	Simply it's a script to remove a string
	from each line in file except the first string

	simply say thank you ahmed <3
"""
if(len(sys.argv)>3 and sys.argv[1]!="-h"):
 path=sys.argv[1]
 output=sys.argv[2]
 text=sys.argv[3]
elif(len(sys.argv)>1 or sys.argv[1]=="-h"):
	print(usage)
	exit(0)
else:
	path=str(input("\x1b[93mFile Name \x1b[92m:"))
	output=str(input("\x1b[93mOutput \x1b[92m:"))
	text=str(input("\x1b[93mOutput \x1b[92m:"))
file=open(path,"rb")
opt=open(output,"wb")
lines=file.readlines()
print(lines[0])
for i in range(1,len(lines)-1):
	z=lines[i].decode().replace(text,"")
	print(z.encode())
	opt.write(z.encode())
	pass