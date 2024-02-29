import os
import sys
import argparse

parser=argparse.ArgumentParser(description='extract part genotype from the whole genotype file')
parser.add_argument('-i', type =argparse.FileType('r'),help='the SNP data file')
parser.add_argument('-all', type =argparse.FileType('r'),help='the whole namelist file')
parser.add_argument('-part', type =argparse.FileType('r'),help='the part namelist file')
parser.add_argument('-o', type =argparse.FileType('w'),help='the name of output file')

args=parser.parse_args()

debug=True

dict1={}
dict2={}
lstorder=[]
for eachline in args.part:
	eachline=eachline.strip()
	dict1[eachline]=0
	lstorder.append(eachline)

index=0
for eachline in args.all:
	eachline=eachline.strip()
	i=eachline.split()
#	print(eachline)
	if i[0] not in dict1:
		pass
	else:
		dict2[i[0]]=index
	index+=1
	print(index)

for eachline in args.i:
	eachline=eachline.strip()
	i=eachline.split('\t')
	code_lst=i[2].split()
	str_out=''
	for it in lstorder:
		str_out+=code_lst[dict2[it]]+' '
#			str_out+=code_lst[index]+' '
	args.o.write(i[0]+'\t'+i[1]+'\t'+str_out.strip()+'\n')
