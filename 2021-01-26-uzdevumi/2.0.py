# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:35:33 2021

@author: antons.sincovs
"""

n = int(input("Enter number of el-ts: "))
sum_missing = 0
sum_full = 0
for i in range(n-1):
    number = int(input("Enter an int: "))
    sum_missing += number

for k in range(1, n+1):
    sum_full += k

print("The missin number is: ", sum_full-sum_missing)
