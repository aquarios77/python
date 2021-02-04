# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:17:15 2021

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

for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
       print(arr[i], end = " ")
else:
    print("")
