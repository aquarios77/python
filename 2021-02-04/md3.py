# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:54:21 2021

@author: antons.sincovs
"""
import random
import math
random.seed(100)

arr_x = [0]*10
arr_y = [0]*10
for i in range(len(arr_x)):
    arr_x[i] = random.randint(-10 , 10)
    arr_y[i] = random.randint(-10 , 10)

max_rad = 0    
for i in range(10):
    print("x%s:%3s y%s:%3s" % (i, arr_x[i] , i , arr_y[i]))
    rad = math.sqrt(arr_x[i]**2 + arr_y[i]**2)
    if rad > max_rad:
        max_rad = rad

print("Min circle radius to contain all points is: ", max_rad)

max_y = max(arr_y)
min_y = min(arr_y)
max_x = max(arr_x)
min_x = min(arr_x)

print("Point 1: x=", max_x, "y=", max_y, "Point 2: x=", min_x, "y=", min_y, "Area=", (max_x - min_x)*(max_y - min_y))
