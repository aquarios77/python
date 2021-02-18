# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 18:16:30 2021

@author: antons.sincovs
"""

f  = open("Dogs.txt","r")
print(f)


# Open the file with read only permit
# use readline() to read the first line 
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    print(line)
    # use realine() to read next line
    line = f.readline()
f.close()