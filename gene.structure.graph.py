
import sys
import os
import re
import argparse
import svgwrite
from svgwrite import cm, mm


parser = argparse.ArgumentParser(description = 'Format tansformation to New file')
parser.add_argument('-input', type = argparse.FileType('r'), help = 'Gene exon information file')
parser.add_argument('-o', type = str, help = 'Output of result graph')

args = parser.parse_args()


debug = True


width=400*cm
height=200*cm
dwg=svgwrite.Drawing(filename=args.o,size=(width,height))
num=0
for eachline in args.input:
	eachline=eachline.strip()
	i=eachline.split()
	if i[0]=='mRNA':
		ori_pos=float(i[1])
		start_pos=float(float(i[1])-ori_pos)/100
		end_pos=float(float(i[2])-ori_pos)/100
		dwg.add(dwg.line(start=((start_pos)*cm,10*cm),end=((end_pos)*cm,10*cm),stroke='black',fill='black',stroke_width=0.5))
#		dwg.add(dwg.line(x1=start_pos*cm,y1=10*cm,x2=end_pos*cm,y2=10*cm))
	elif i[0]=='exon':
#		prfloat(eachline)
		new_start=float(float(i[1])-ori_pos)/100
		print(new_start)
		new_end=float(float(i[2])-ori_pos)/100
		dwg.add(dwg.rect(insert=((new_start)*cm,10*cm),size=((new_end-new_start)*cm,5*cm),fill='red',stroke='black',stroke_width=0.5))
#		dwg.add(dwg.rect(x=new_start*cm,y=10*cm,width=(new_end-new_start)*cm,height=5*cm,fill='red',stroke='black'))
	else:
		new_start=float(float(i[1])-ori_pos)/100
		dwg.add(dwg.line(start=((new_start)*cm,10*cm),end=((new_start)*cm,15*cm),stroke='black',fill='black',stroke_width=0.5))
dwg.save()
