# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:01:47 2021

@author: antons.sincovs
"""

from vector import Vector

my_vec01 = Vector(2,3)
my_vec02 = Vector(4,7)
my_vec03 = Vector(3,2)

print("Vector 01: ", my_vec01)
print("Vector 02: ", my_vec02)
print("Vector 01 + Vector 02: ", my_vec01 + my_vec02)

print("Vector 01 * number : ", str(my_vec01 * 4))
print("Vector 01 * Vector02 : ", str(my_vec01 * my_vec02))


# vector01 * number is not equal to number * vector01
print("Vector 01 * number : ", str(4 * my_vec01))

print("Vec01 == Vec03 ? " , my_vec01 == my_vec03)
print("Vec01 == Vec02 ? " , my_vec01 == my_vec02)

print(my_vec01[0])
print(my_vec01[1])