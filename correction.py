#!/usr/bin/env python
#created by Maosong Pei
import re
from sys import argv
a=open(argv[1])
b=open(argv[2],'w')
header=1

for line in a:
    if header:
        header-=1
    else:
        line=line.strip().split('\t')
        count=len(line)
        seq=range(1,count,3)
        b.write(line[0]+"\t")
        for i in seq:
            if i <count-3:

                li=[float(line[i]),float(line[i+1]),float(line[i+2])]
                if li.count(0)>=2:
                    b.write("0"+"\t"+"0"+"\t"+"0"+"\t")
                else:
                    b.write(line[i]+"\t"+line[i+1]+"\t"+line[i+2]+"\t")
            else:
                li=[float(line[i]),float(line[i+1]),float(line[i+2])]
                if li.count(0)>=2:
                    b.write("0"+"\t"+"0"+"\t"+"0"+"\n")
                else:
                    b.write(line[i]+"\t"+line[i+1]+"\t"+line[i+2]+"\n")
        
a.close()
b.close()
