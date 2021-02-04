# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:23:44 2021

@author: antons.sincovs
"""

import random

num_of_el = int(input("Enter the num of el-ts: "))
start_num = int(input("Enter the start point: "))
end_num = int(input("Enter the end point: "))
arr = []
for i in range(num_of_el):
    arr.append(random.randint(start_num , end_num))

print("Generated array: ", arr)

num_of_el = 0

for i in range(1,len(arr) - 1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        num_of_el += 1
print("Number of el-ts which are greater than both neighbours: ", num_of_el)