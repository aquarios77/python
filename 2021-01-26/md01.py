# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:12:03 2021

@author: antons.sincovs
"""
num_greater = 0
previous = int (input('Enter an int: '))
if previous != 0:
    current = int(input('Enter an int: '))
    while current != 0:
        if previous < current:
            num_greater += 1
        previous = current
        current = int(input('Enter an int: '))
    
print(num_greater)
    