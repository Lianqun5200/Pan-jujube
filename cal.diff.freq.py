f1=open('wild.cul.infor','r')
f2=open('name.list','r')
f3=open('genotypes.vcf','r')
p=open('sv.genotype.diff.freq','w')

dict_cul={}
dict_wild={}
for eachline in f1:
	eachline=eachline.strip()
	i=eachline.split()
	if i[1]=='Wild':
		dict_wild[i[0]]=0
	else:
		dict_cul[i[0]]=0

cul_index={}
wild_index={}
index=0
for eachline in f2:
	eachline=eachline.strip()
	if eachline in dict_cul:
		cul_index[index]=0
	else:
		if eachline in dict_wild:
			wild_index[index]=0
		else:
			print(eachline)
	index+=1

for eachline in f3:
	eachline=eachline.strip()
	if eachline[0]=='#':
		continue
	else:
		i=eachline.split('\t',9)
		chrID=i[0]
		pos=i[1]
		codelst=i[9].split()
		total=0
		cul=0
		wild=0
		for index in range(len(codelst)):
			infor=codelst[index].split(':')[0]
			if infor=='./.' or infor=='.|.':
				continue
			else:
				total+=2
				if index in cul_index:
					if infor=='0/0' or infor=='0|0':
						cul+=2
					elif infor=='0/1' or infor=='0|1':
						cul+=1
					elif infor=='1/1' or infor=='1|1':
						cul+=0
				elif index in wild_index:
					if infor=='0/0' or infor=='0|0':
						wild+=2
					elif infor=='0/1' or infor=='0|1':
						wild+=1
					elif infor=='1/1' or infor=='1|1':
						wild+=0
				else:
					continue
		wildfreq=wild/total
		culfreq=cul/total
		p.write('%s\t%s\t%f\t%f\n' % (chrID,pos,culfreq,wildfreq))
