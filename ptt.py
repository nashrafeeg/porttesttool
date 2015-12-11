#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author Nash Rafeeq 

import socket
import re
import sys
import csv
import os
from datetime import datetime

OUTPUTFILE = None
OUTPUTCSV = None

def check_server(address, port, protcol="TCP"):
	p = protcol
	if protcol.upper() == "TCP":
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	elif protcol.upper() == "UDP":
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	else:
		print "Unknown or unsuported protcol [%s] defaulting to TCP" % protcol
		p = "TCP"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5.0)
	try:
		s.connect((address, port))
		s.settimeout(None)
		print "Connection to %20s on port %5s[%s] ..... OK" % (address, port,p)
		s.close()
		if OUTPUTFILE is not None:
			OUTPUTCSV = csv.writer(OUTPUTFILE)
			OUTPUTCSV.writerow([address,port,p,"OK"])
		return True
	except socket.error, e:
		print "Connection to %20s on port %5s[%s]..... Failed \nReason: %s" % (address, port, p, e)
		s.close() 
		if OUTPUTFILE is not None:
			OUTPUTCSV = csv.writer(OUTPUTFILE)
			OUTPUTCSV.writerow([address, port,p,"Fail", e])
		return False


def read_file(portfile, header):
	reader = csv.reader(portfile)
	if header:
		next(reader, None)
	if OUTPUTFILE is not None:
		OUTPUTCSV = csv.writer(OUTPUTFILE)
		OUTPUTCSV.writerow(["Host,PORT,PROTOCOL,STATUS,FAILED REASON"])
	for row in reader: 
		if len(row) >2: 
				check_server(row[0], int(row[1]), row[2])
		else:
				check_server(row[0], int(row[1]))	



if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(
		prog="Ptt.exe",
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description='''
			Port Test Tool (Cause Fuck TCS)
			-------------------------------
				version: 1.11 (cause fuck TCS)
				Author: Nash Rafeeq (@nashrafeeg)
				RTFM: http://nashath.xyz/ptt/v1.11'
			
			Input file 
			----------
				format: CSV
				delimeter: , 
				header: fqdn/ip,port,[protocol]
				Eg: 8.8.8.8,53,TCP

			Outputfile
			----------
				format:CSV
				delimeter: , 
				header: fqdn/ip,port,protcol,status,[failed Reason]
				Eg: 8.8.8.8,53,TCP
			''', 
		epilog='''
		Please send any bugs or feature request to ptthelp@nashath.xyz
		Pull requests are welcome at https://github.com/nashrafeeg/porttesttool
			'''
		)
	parser.add_argument('portlist', nargs='?', type=argparse.FileType('r'),default='portlist.csv', help='path to csv file containing list of ports to test')
	parser.add_argument('-o', '--outputfile', nargs='?', type=argparse.FileType('wb'), help='path to output results to')
	parser.add_argument('-H', '--header', action='store_true',  help='set if the CSV file contains header row (igonore first row)')
	#TODO
	#paser.add_argument('-p', 'pingonfail', action='store_true', help='set to ping host if port test fails')
	args = parser.parse_args()
	
	OUTPUTFILE = args.outputfile
	read_file(args.portlist,args.header)
	sys.exit()