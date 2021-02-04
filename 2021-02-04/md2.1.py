# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:40:02 2021

@author: antons.sincovs
"""
import random

num_of_el = int(input("Enter the num of el-ts: "))
arr = []
for i in range(num_of_el):
    arr.append(random.randint(1 , 10))

print("Generated array: ", arr)

arr_repeat_value = []

for k in range(len(arr)):
    for j in range(k, len(arr) - 1):
        if arr[k] == arr[j+1]:
            arr_repeat_value.append(arr[k])
 
unique_arr = [] 
            
for n in arr:
    if n not in arr_repeat_value:
        unique_arr.append(n)
        

print("Unique value array: ", unique_arr)

for i in range(len(unique_arr)):
    for k in range(len(unique_arr)):
        if unique_arr [i] < unique_arr[k]:
            unique_arr[i] , unique_arr [k] = unique_arr [k] , unique_arr[i]

for i in range(len(arr)):
    for k in range(len(arr)):
        if arr [i] < arr[k]:
            arr[i] , arr [k] = arr [k] , arr[i]
            
print("Arranged array: ", arr)

distinct_arr = []
distinct_arr.append(arr[0])

for z in range(1, len(arr)):
    if arr[z-1] != arr[z]:
        distinct_arr.append(arr[z])
print("Distinct array: ", distinct_arr)


print("Arranged unique array: ", unique_arr)

counter = 0
for i in range(len(distinct_arr)):
    print("[" , distinct_arr[i] , "]:", arr.count(distinct_arr[i]), sep="")
    
for i in range(len(distinct_arr)):
    print("%2s | %s" % (distinct_arr[i] , '*'*arr.count(distinct_arr[i])))