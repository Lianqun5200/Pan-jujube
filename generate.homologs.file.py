import os
import sys
import argparse

parser=argparse.ArgumentParser(description='prepare the homologs paired gene file for kaks calculation')
parser.add_argument('-group', type =argparse.FileType('r'),help='the ortho group file')

args=parser.parse_args()

debug=True

for eachline in args.group:
	eachline=eachline.strip()
	i=eachline.split()
	if i[0]=='Orthogroup':
		continue
	else:
		dirname=i[0]
		command='mkdir '+dirname
		os.system(command)
		p=open('homologs.file','w')
		lst1=[]
		lst2=[]
		dict_set={}
		for it in i:
			if it==dirname or len(it)==0:
				continue
			else:
				code_lst=it.split(', ')
				for factor in code_lst:
					lst1.append(factor)
					lst2.append(factor)
		for it1 in lst1:
			for it2 in lst2:
				if it1==it2:
					continue
				else:
					if it1[-1]==',':
						it1=it1[:-1]
					else:
						it1=it1
					if it2[-1]==',':
						it2=it2[:-1]
					else:
						it2=it2
					set_code1=it1+'#'+it2
					set_code2=it2+'#'+it1
					if (set_code1 not in dict_set) and (set_code2 not in dict_set):
						p.write(it1+'\t'+it2+'\n')
						dict_set[set_code1]=0
						dict_set[set_code2]=0
					else:
						continue
		command2='mv homologs.file '+dirname
		os.system(command2)
