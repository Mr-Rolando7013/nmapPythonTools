#!/usr/bin/python3
#The purpose of this script is when you run a stealthy scan on a target to check open ports and export the nmap output with -oG

#This script will read the output and display the ports in a better format and paste the ports into your clipboard to do a more intensive scan into these ports.

import sys
import pyperclip

filename = sys.argv[-1]
result = ""
resultArray = []
counter = 1
data = ""
host = ""

with open(filename, "r") as fp:
	lines = fp.readlines()
	word = "Ports:"
	
	for row in lines:
		if filename in row:
			host = row.split(filename).pop()
		if word in row:
			#Getting all the ports into a string
			result = row.split("Ports:").pop()

print("Host Scanned: --", host, "--")
resultArray = result.split(",")
#Separate ports individually
for i in resultArray:

	if counter == len(resultArray):
		data =  data + i.split('/')[0]
	else:
		data = data + i.split('/')[0] + ","
	

	counter = counter + 1


secondArray = data.split()
printArray = data.split(",")

#Print ports in a certain format
for k in printArray:
	print('[*] Open Port:' + k + ' in: ' + host)
data = ""
#Save ports in the clipboard in a certain format
for j in secondArray:
	data = data + j
	
print('[=] Ports Copied in clipboard! ')
pyperclip.copy(data)
