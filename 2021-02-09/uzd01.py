# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:39:00 2021

@author: antons.sincovs
"""
#make a list only from integer from the initial list

saraksts = [2,3.75,"ABC",59.354,6,7.7777,8,9, [1,2]]

integers = []

for elem in saraksts:
    if isinstance(elem , int):
        integers.append(elem)
print(integers)

integers_01 = [elem for elem in saraksts if isinstance(elem, int)]

print (integers_01)