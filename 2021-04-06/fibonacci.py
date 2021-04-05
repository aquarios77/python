# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:08:09 2021

@author: antons.sincovs
"""
import time

# fibonnacci calculation with iteration
def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec( n - 2)

# fibonacci calclation with recursion
def fib_iter(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        n1 = 0
        n2 = 1
        fib = 0
        for _ in range(2,n+1):
            fib = n1 + n2
            n1 , n2 = n2 , fib
        return fib

# settting Fibonacci number
n = 20

# timing with recursion
pk1 = time.perf_counter()    
print(fib_rec(n))
pk2 = time.perf_counter()
print(pk2 - pk1, "recursion time")

# timing with iteration
pk3 = time.perf_counter()  
print (fib_iter(n))
pk4 = time.perf_counter()
print(pk4 - pk3, "iteration time")

# overall result comparison
print("Iteration is",round((pk2 - pk1)/(pk4 - pk3),2), "times faster than recursion")
