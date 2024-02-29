import os
import sys
import argparse

parser=argparse.ArgumentParser(description='creat the command for per individual bam file')
parser.add_argument('-i', type =argparse.FileType('r'),help='the gz file path')
parser.add_argument('-ref', type =str,help='the ref')

args=parser.parse_args()

debug=True

dict1={}
dict2={}

for eachline in args.i:
	eachline=eachline.strip()
	i=eachline.split('/')
	ID=i[-1].split('_')[0]
	if ID not in dict1:
		dict1[ID]=eachline+' '
		dict2[ID]=1
	else:
		dict1[ID]+=eachline+' '
for it in dict1:
	command1='mkdir '+it
	os.system(command1)
	p=open('work.sh','w')
	p.write('#!/bin/sh\n')
	p.write('bwa mem -M -R  "@RG\\tID:%s\\tLB:%s\\tPL:ILLUMINA\\tSM:%s" %s  %s > %s.sam\n' % (it,it,it,args.ref,dict1[it],it))
	p.write('samtools sort -o %s.bam %s.sam\n' % (it,it))
	p.write('rm -rf %s.sam\n' % (it))
	p.write('samtools index %s.bam\n' % (it))
	p.write('samtools flagstat %s.bam > output.infor\n' % (it))
	p.write('samtools depth %s.bam | wc -l >> output.infor\n' % (it))
	p.write("samtools depth %s.bam | awk '{sum+=$3} END {print sum/NR}' >> output.infor\n" % (it))
	p.write('gatk MarkDuplicates -I %s.bam -O %s.sorted.markdup.bam -M %s.markdup.metrics.txt\n' % (it,it,it))
	p.write('rm -rf %s.bam\n' % (it))
	p.write('samtools index %s.sorted.markdup.bam\n' % (it))
	p.write('gatk HaplotypeCaller -R %s --sample-ploidy 2 --emit-ref-confidence GVCF -I %s.sorted.markdup.bam -O %s.sample.gvcf\n' % (args.ref,it,it))
	p.write('bgzip -f %s.sample.gvcf\ntabix -f -p vcf %s.sample.gvcf.gz' % (it,it))
	p.close()
	command2='mv work.sh '+it
	os.system(command2)
