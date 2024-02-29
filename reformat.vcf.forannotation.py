import os
import sys
import argparse

parser=argparse.ArgumentParser(description='change the vcf format for SV annotation')
parser.add_argument('-input', type =argparse.FileType('r'),help='the input vcf file')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True

for eachline in args.input:
	eachline=eachline.strip()
	i=eachline.split()
	if eachline[0]=='#':
		args.o.write(eachline+'\n')
	else:
		if '<' in i[4]:
			if i[4][-3:-1]=='AL':
				continue
			else:
				args.o.write(eachline+'\n')
				chrID=i[0]
				pos=i[1]
				end=i[7].split(';')[0].split('=')[1]
				infor=eachline.split('\t',2)[2]
				args.o.write(chrID+'\t'+end+'\t'+infor+'\n')
		else:
			args.o.write(eachline+'\n')
