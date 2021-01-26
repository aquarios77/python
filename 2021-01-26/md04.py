# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:02:35 2021

@author: antons.sincovs
"""

current = int(input("Enter an int: "))
previous = -1
prev_num_of_equal = 1
cur_num_of_equal = 1

while current !=0:
    if previous == current:
        cur_num_of_equal+=1
    elif previous != current:
        if cur_num_of_equal > prev_num_of_equal:
            prev_num_of_equal = cur_num_of_equal
        cur_num_of_equal = 1
    
    previous = current
    current = int(input("Enter an int: "))

print(max(prev_num_of_equal, cur_num_of_equal))
