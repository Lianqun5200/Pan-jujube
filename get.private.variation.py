import gzip
f1=gzip.open('all.snp.vcf.gz','rt')
f2=open('se;ected.list','r') # extract private variation according to a given sample list
p=open('private.out','w')

dict1={}
dict2={}
for eachline in f2:
	eachline=eachline.strip()
	dict1[eachline]=0

for eachline in f1:
	eachline=eachline.strip()
#	print(eachline)
	i=eachline.split('\t',9)
	codelst=i[9].split()
	if eachline[0]=='#':
		for it in range(len(codelst)):
			if codelst[it] in dict1:
				dict2[it]=0
			else:
				continue
	else:
		lstset1=[]
		lstset2=[]
		for it in range(len(codelst)):
			infor=codelst[it].split(':')[0]
			if infor=='./.' or infor=='.|.':
				continue
			else:
				if it in dict2:
					infor=infor.replace('|','/')
					if infor not in lstset1:
						lstset1.append(infor)
					else:
						continue
				else:
					infor=infor.replace('|','/')
					if infor not in lstset2:
						lstset2.append(infor)
					else:
						continue
		if len(lstset1)>1 and  len(lstset2)==1:
			p.write(eachline+'\n')
		else:
			continue
