#!/usr/bin/env python3
import os
import sys
import shutil

def numToLetter(num):
    convert={
    0:"a",
    1:"b",
    2:"c",
    3:"d",
    4:"e",
    5:"f",
    6:"g",
    7:"h",
    8:"i",
    9:"j",
    10:"k",
    11:"l",
    12:"m",
    13:"n",
    14:"o",
    15:"p",
    16:"q",
    17:"r",
    18:"s",
    19:"t",
    20:"u",
    21:"v",
    22:"w",
    23:"x",
    24:"y",
    25:"z"}
    num=num-1
    first=(num-num%26)/26
    second=num%26
    return convert[first]+convert[second]

filename=sys.argv[1][:-4]
first=int(sys.argv[2])
last=int(sys.argv[3])+1
cycle=int(sys.argv[4])

if shutil.which("rename")==None:
    print("rename is missing. Please install rename.\nOn Ubuntu you can do this by running 'sudo apt install rename'")
    exit()

for i in range(first,last):
    os.system("rename 's/_"+str(i)+".inp/_"+numToLetter(i)+".inp/' "+filename+"*")
    for j in range(1, cycle+1):
        os.system("rename 's/_"+str(i)+"00"+str(j)+"_/_"+numToLetter(i)+"00"+str(j)+"_/' "+filename+"*")
        os.system("rename 's/_"+str(i)+"00"+str(j)+"\./_"+numToLetter(i)+"00"+str(j)+"\./' "+filename+"*")
