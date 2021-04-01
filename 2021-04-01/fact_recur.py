# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:08:09 2021

@author: antons.sincovs
"""

def fac(n):
    if n == 1:
        print(n, "=", sep="", end="")
        return n
    else:
        print(n , "*" , sep="", end="")
        return n * fac(n-1)
    
print(fac(5))