# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:36:18 2021

@author: antons.sincovs
"""

a = float(input("Enter a number ==> "))
print(type(a))

if a.is_integer():
        a = int(a)
        print(type(a))
        print(a)
else:
    print("a is not integer4")