# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:36:18 2021

@author: antons.sincovs
"""

a = input("Enter a number ==> ")

while True:
    try:
        print(type(a))
        a = int(a)
        print(type(a))
        print(a)
        break
    except ValueError:
        print("a is not integer")
        a = input("Enter a number ==> ")
    
print("Program ends")