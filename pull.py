#!/usr/bin/env python3

import os
import sys
import re

"""
Python script to convert input and output files from FLUKA simulations. 
Limitations and Considerations:
    Works on files in the working directory! 
    It will require all (input and output) files to be in the same directory!
    If the original Flair input file is in the dir it will NOT be renamed!  
    The regular expressions are fixed in the following standard:
        a) Single ([1-9]) or double ([1-9][0-9]) digit pattern for input files: 
            _[1-9].inp  or  _[1-9][0-9].inp
            Number considered 1 - 40 (fixed by the number of cores allowed 
            to run on the cluster). 
        b) Single ([1-9]) or double ([1-9][0-9]) digit pattern for output files: 
            _[1-9]00[1-9]  or  _[1-9][0-9]00[1-9]
            Number considered 1 - 40 (fixed by the cluster)
            Number appearing after the 00 characters corresponds to N cycles, 
            where 1 <= N <= 9 (limit conming from output file size ~GB).  
"""

CONVERTER = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i",
             9:"j", 10:"k", 11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q",
             17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y",
             25:"z"}

def num_to_letter(num: int) -> str:
    """
    Convert a single digit number into a two letter sequence
    Example: 1 --> aa 
    
    :param num: Integer number >= 1
    """
    num = num - 1
    first = (num - num%26) / 26
    second = num % 26
    return CONVERTER[first] + CONVERTER[second]


file_stem = sys.argv[1]

f = os.listdir()

# Filter files and split into input and output
inp = sorted([k for k in f if file_stem in k and '.inp' in k])
out = sorted([k for k in f if file_stem in k and '.inp' not in k])

# Check if the original Flair input file was filtered. 
if f'{file_stem}.inp' in inp:
    inp.remove(f'{file_stem}.inp') 

# Rename all input files in the working directory
for i in inp:
    n = int(re.findall('_[1-9].inp|_[1-9][0-9].inp', i)[0][1:-4])
    new_inp_name = re.sub(f'_{n}', f'_{num_to_letter(n)}', i)
    print(i, ' --> ', new_inp_name) 
    os.rename(i, new_inp_name)

# Rename all output files in the working directory
for o in out:
    t = int(re.findall('_[1-9]00[1-9]|_[1-9][0-9]00[1-9]', o)[0][1:-3])
    new_out_name = re.sub(f'_{t}', f'_{num_to_letter(t)}', o)
    print(o, ' --> ', new_out_name)    
    os.rename(o, new_out_name)

print('Rename completed!')