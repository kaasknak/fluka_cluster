#!/usr/bin/env python3

#For use with fluka if you need to convert your input file to work on the cluster.

import sys	#in order to read arguments
import os	#Command line interactions

first=int(sys.argv[2])
last=int(sys.argv[3])+1
folder=sys.argv[4]

os.system("mkdir "+folder)

os.system("cp "+sys.argv[1]+" "+folder)

for i in range(first,last):
    if len(str(i))==1:
        os.system("cat "+sys.argv[1]+" | sed 's/RANDOMIZ.*/RANDOMIZ                    "+str(i)+"./' > "+folder+"/"+sys.argv[1][:-4]+"_"+str(i)+".inp")
    elif len(str(i))==2:
        os.system("cat "+sys.argv[1]+" | sed 's/RANDOMIZ.*/RANDOMIZ                   "+str(i)+"./' > "+folder+"/"+sys.argv[1][:-4]+"_"+str(i)+".inp")
    elif len(str(i))==3:
        os.system("cat "+sys.argv[1]+" | sed 's/RANDOMIZ.*/RANDOMIZ                  "+str(i)+"./' > "+folder+"/"+sys.argv[1][:-4]+"_"+str(i)+".inp")
    else:
        print("Woops! Something went wrong and you are not supposed to see this. Did you try to enter a number higher than 676?")
        exit()

