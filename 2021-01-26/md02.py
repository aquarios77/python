# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:37:54 2021

@author: antons.sincovs
"""

maximum = 0
second_to_max = 0

while True:
    number = int(input("Enter an integer: "))
    if number > maximum:
        second_to_max = maximum
        maximum = number
    elif number > second_to_max and number != maximum:
        second_to_max = number
    elif number == 0:
        break
print(second_to_max)
