# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:36:50 2021

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

arr_repeat_value = []

for k in range(len(arr)):
    for j in range(k, len(arr) - 1):
        if arr[k] == arr[j+1]:
            arr_repeat_value.append(arr[k])
            
for n in arr:
    if n not in arr_repeat_value:
        print(n, end=" ")
