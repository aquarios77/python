# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:08:09 2021

@author: antons.sincovs
"""
import time

def fact_rec(n):
    if n == 1:
        return n
    else:
        return n * fact_rec(n-1)
    
#def fact

pk1 = time.perf_counter()    
print(fact_rec(10))
pk2 = time.perf_counter()
print(pk2 - pk1)
