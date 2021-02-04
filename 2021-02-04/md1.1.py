# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:35:01 2021

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

for i in range(len(arr) - 1):
    if arr[i+1] <0 and arr[i] <0:
        print(arr[i], arr[i+1], sep=' ')
        break
    if arr[i+1] >=0 and arr[i] >=0:
        print(arr[i], arr[i+1], sep=' ')
        break
