# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:59:02 2021

@author: antons.sincovs
"""

string = input()
find = string.find('h')
r_find = string.rfind('h')+1
first_part = string[0:find]
second_part = string[r_find:]

print(first_part + second_part)