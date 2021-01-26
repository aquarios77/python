# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:54:07 2021

@author: antons.sincovs
"""

current_max = 0
num_of_max = 1
previous_max = 0

while True:
    number = int(input("Enter an int: "))
    if number > current_max:
        num_of_max = 1
        previous_max , current_max = current_max , number
    elif number == current_max:
       previous_max , current_max = current_max , number
       num_of_max += 1
    elif number == 0:
        break
print(num_of_max)
