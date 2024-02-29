import os
import sys
import argparse
import re

parser=argparse.ArgumentParser(description='extract the seq according to a interval')
parser.add_argument('-genome', type =argparse.FileType('r'),help='the genome sequence')
parser.add_argument('-chr', type =str,help='the chr ID')
parser.add_argument('-start', type =int,help='the chr ID')
parser.add_argument('-end', type =int,help='the chr ID')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True

dict1={}
flag=0
for eachline in args.genome:
	eachline=eachline.strip()
	if flag==0:
		if eachline[0]=='>':
			ID=eachline[1:]
			dict1[ID]=''
			strout=''
			flag=1
	else:
		if eachline[0]!='>':
			strout+=eachline
		else:
			dict1[ID]=strout
			ID=eachline[1:]
			dict1[ID]=''
			strout=''
dict1[ID]=strout

targetseq=dict1[args.chr][args.start-1:args.end]	
args.o.write('>%s_%d_%d\n%s\n' % (args.chr,args.start,args.end,targetseq))
