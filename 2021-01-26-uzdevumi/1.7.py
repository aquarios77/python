# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:22:10 2021

@author: antons.sincovs
"""

number = int(input("Enter int n: "))
sum = 0
drobj = 1
fakt = 1

for i in range(1, number + 1):
    for k in range(1, i + 1):
        fakt *= k
        drobj = 1/fakt
    sum += drobj
    fakt=1
print(sum+1)