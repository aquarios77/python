# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:34:29 2021

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

equal_pair_count = 0

for k in range(len(arr)):
    for i in range(k + 1 , len(arr)):
        if arr[k] == arr[i]:
           equal_pair_count += 1 

print("Equal pair count: ", equal_pair_count)