# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:34:03 2021

@author: antons.sincovs
"""
def fib(n):
    if n < 0:
        raise ValueError("N should be positive!")
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(-1))