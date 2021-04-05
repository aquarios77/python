# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:27:38 2021

@author: antons.sincovs
"""
import time

# lkd calculation with recursion
def lkd_rec(num1 , num2):
    if num2 == 0:
        return num1
    else:
        return lkd_rec(num2 , num1 % num2)

# lkd calculation with forced loop iteration
def lkd_force(num1 , num2):
    lkd = 1
    for i in range(1,max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            lkd = i
    return lkd

# lkd calculation with forced loop iteration
def lkd_iter(num1 , num2):
    while num1 != 0 and num2 !=0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2

def mkd(num1 , num2):
    return abs(num1 * num2 ) / lkd_iter(num1 , num2)


# setting n1 and n2
n1 = 120
n2 = 180

# timing with recursion
pk1 = time.perf_counter()  
print(lkd_rec(n1, n2))
pk2 = time.perf_counter()
p_rec = pk2 - pk1
print(p_rec, "recursion time")

# timing with iteration
pk3 = time.perf_counter()
print(lkd_force(n1, n2))
pk4 = time.perf_counter()
p_fiter = pk4 - pk3
print(p_fiter, "force iteration time")

# timing with iteration
pk5 = time.perf_counter()
print(lkd_iter(n1, n2))
pk6 = time.perf_counter()
p_eiter = pk6 - pk5
print(p_eiter, "Euclid iteration time")

# overall result comparison
print("Euclidean iteration is ",round(p_fiter/(p_eiter),2), "times faster than force iteration and" ,round(p_rec/(p_eiter),2) , "times faster than recursion")

print("MKD = ", mkd(n1, n2))



