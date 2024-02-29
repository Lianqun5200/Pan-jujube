import os
import sys
import argparse

parser=argparse.ArgumentParser(description='extract the genes affected by selected sv result')
parser.add_argument('-i', type =argparse.FileType('r'),help='the filtered sv result')
parser.add_argument('-gff', type =argparse.FileType('r'),help='the gff3 file')
parser.add_argument('-o1', type =argparse.FileType('w'),help='sv overlap with gene cds region')
parser.add_argument('-o2', type =argparse.FileType('w'),help='sv overlap with gene upstream region')

args=parser.parse_args()

debug=True

dict1={}
dict2={}
dict0={}
for eachline in args.gff:
	eachline=eachline.strip()
	i=eachline.split()
	if eachline[0]=='#':
		continue
	else:
		if i[2]=='gene':
			strant=i[6]
			chrID=i[0]
			start=int(i[3])
			end=int(i[4])
			geneID=i[-1].split(';')[0].split('=')[1]
			dict0[geneID]=[]
			dict0[geneID].append(start)
			dict0[geneID].append(end)
#			dict0[geneID].append(chrID)
			for index in range(start,end+1):
				ID1=chrID+'\t'+str(index)
				dict1[ID1]=geneID
			if strant=='+':
				for it in range(start-2000,start):
					ID2=chrID+'\t'+str(it)
					dict2[ID2]=geneID
			else:
				for it in range(end+1,end+2000+1):
					ID3=chrID+'\t'+str(it)
					dict2[ID3]=geneID

def overlaplen(svstart,svend,genestart,geneend):
	if svend <= genestart:
		return('N')
	else:
		if svstart>=geneend:
			return('N')
		else:
			if svstart<genestart:
				if svend>=geneend:
					return('Y')
				else:
					if (svend-geneend)/(geneend-genestart)>=0.5:
						return('Y')
					else:
						return('N')
			else:
				if svend<=geneend:
					if (svstart-svend)/(geneend-genestart)>=0.5:
						return('Y')
					else:
						return('N')
				else:
					if (svstart-geneend)/(geneend-genestart)>=0.5:
						return('Y')
					else:
						return('N')


dict3={}
dict4={}
for eachline in args.i:
	eachline=eachline.strip()
	print(eachline)
	i=eachline.split()
	chrID=i[0]
	pos1=int(i[1])
	pos2=int(i[7].split(';')[0].split('=')[1])
	lstpos=[]
	lstpos.append(pos1)
	lstpos.append(pos2)
	start=min(lstpos)
	end=max(lstpos)
	infor=i[0]+'\t'+str(start)+'\t'+str(end)+'\t'+i[2]
	for index in range(start,end+1):
		ID=chrID+'\t'+str(index)
		if ID in dict1:
			if overlaplen(start,end,dict0[dict1[ID]][0],dict0[dict1[ID]][1])=='Y':
				if dict1[ID] not in dict3:
					args.o1.write(infor+'\t'+dict1[ID]+'\n')
					dict3[dict1[ID]]=0
				else:
					continue
			else:
				continue
		else:
			if ID in dict2:
				if dict2[ID] not in dict4:
					args.o2.write(infor+'\t'+dict2[ID]+'\n')
					dict4[dict2[ID]]=0
				else:
					continue

"""
for it in dict3:
	args.o1.write(it+'\n')

for it in dict4:
	args.o2.write(it+'\n')
"""
