# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 19:01:04 2021

@author: antons.sincovs
"""

string = input("Enter a string: ")
for i in range(10):
    string = string.replace(str(i),'*')
print(string)