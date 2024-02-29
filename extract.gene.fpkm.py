import os
import sys
import argparse

parser=argparse.ArgumentParser(description='extract the expression data')
parser.add_argument('-input', type =argparse.FileType('r'),help='the input file path')
parser.add_argument('-output', type =argparse.FileType('w'),help='the output file')

args=parser.parse_args()

debug=True

dict1={}
lst_set=[]
head_str='geneID\t'

for eachline in args.input:
	eachline=eachline.strip()
	if eachline[0]=='#':
		continue
	else:
		i=eachline.split('/')
		nameID=i[-2].split('_')[0]
		head_str+=nameID+'\t'
		print(nameID)
		newfile=open(eachline,'r')
		for line in newfile:
			line=line.strip()
			code_lst=line.split('\t')
			if line[0]!='#' and  code_lst[2]=='transcript':
				geneID=code_lst[8].split(';')[0].split()[1][1:-1]
				fpkm=code_lst[8].split(';')[-2].split()[-1][1:-1]
				if geneID not in lst_set:
					lst_set.append(geneID)
					dict1[geneID]=geneID+'\t'+fpkm+'\t'
				else:
					dict1[geneID]+=fpkm+'\t'
			else:
				continue
args.output.write(head_str.strip()+'\n')
for it in lst_set:
	args.output.write(dict1[it].strip()+'\n')
