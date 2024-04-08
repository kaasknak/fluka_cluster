#!/usr/bin/env python3

"""
For use with FLUKA if you need to convert your input file 
to work on a cluster system.

NOTE: The space padding is important to have a good random seed 
See the documentation for the RANDOMIZE seed, which states "any number < 9.E8": 
http://www.fluka.org/content/manuals/online/RANDOMIZ.html
    
    Example 2:
 * This run will be completely independent statistically from the previous one
 *...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8
RANDOMIZ         1.0  4042731.       0.0       0.0       0.0       0.0       0.0

"""


import os	# Command line interactions
import sys	# in order to read arguments

fname = sys.argv[1]
fstem = fname[:-4]
first=int(sys.argv[2])
last=int(sys.argv[3]) + 1
folder=sys.argv[4]

os.system(f'mkdir {folder}')
os.system(f'cp {fname} {folder}')

for i in range(first, last):
    if i < 676:
        os.system(f"cat {fname} | sed 's/RANDOMIZ.*/RANDOMIZ         1.0{i:>9d}./ > {folder}/{fstem}_{i}.inp")
    else:
        print("Woops! Something went wrong, you are not supposed to see this.")
        print("Did you try to enter a number higher than 676?")
        exit()
