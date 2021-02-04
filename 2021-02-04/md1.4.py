# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:26:46 2021

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

for i in range(len(arr)):
    for k in range(len(arr)):
        if arr [i] < arr[k]:
            arr[i] , arr [k] = arr [k] , arr[i]

print("Arranged array: ", arr)

diff_count = 1

for i in range(len(arr) - 1):
    if arr[i] != arr[i+1]:
        diff_count += 1
print("Differen number count: ", diff_count)