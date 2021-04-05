# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:20:19 2021

@author: antons.sincovs
"""
import time
import random

def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for v in range(i + 1, len(my_list)):
            if my_list[i] > my_list[v]:
                my_list[i] , my_list[v] = my_list[v] , my_list[i]
    return my_list

def r_li_create(num_of_el, li):
    for i in range(num_of_el):
        li.append(random.randint(1,num_of_el))
    return li



r_li_10 = []
r_li_100 = []
r_li_1000 = []
r_li_10000 = []

r_li_create(10, r_li_10)
r_li_create(100, r_li_100)
r_li_create(1000, r_li_1000)
r_li_create(10000, r_li_10000)

# ================== 10 =======================================================================================================
# timing with bubble
pk1 = time.perf_counter()  
bubble_sort(r_li_10)
pk2 = time.perf_counter()
p_bubble = pk2 - pk1
print(p_bubble, "bubble sort time")

# timing with built-in
pk3 = time.perf_counter()
sorted(r_li_10)
pk4 = time.perf_counter()
p_py = pk4 - pk3
print(p_py, "Python buil-in sort time")

# overall result comparison
print("Built-in Python sorting function is",round(p_bubble/p_py,2), "times faster than bubble sort for list of", len(r_li_10))

# ================== 100 =======================================================================================================

# timing with bubble
pk1 = time.perf_counter()  
bubble_sort(r_li_100)
pk2 = time.perf_counter()
p_bubble = pk2 - pk1
print(p_bubble, "bubble sort time")

# timing with built-in
pk3 = time.perf_counter()
sorted(r_li_100)
pk4 = time.perf_counter()
p_py = pk4 - pk3
print(p_py, "Python buil-in sort time")

# overall result comparison
print("Built-in Python sorting function is",round(p_bubble/p_py,2), "times faster than bubble sort for list of", len(r_li_100))

# ================== 1000 =======================================================================================================
# timing with bubble
pk1 = time.perf_counter()  
bubble_sort(r_li_1000)
pk2 = time.perf_counter()
p_bubble = pk2 - pk1
print(p_bubble, "bubble sort time")
# timing with built-in
pk3 = time.perf_counter()
sorted(r_li_1000)
pk4 = time.perf_counter()
p_py = pk4 - pk3
print(p_py, "Python buil-in sort time")

# overall result comparison
print("Built-in Python sorting function is",round(p_bubble/p_py,2), "times faster than bubble sort for list of", len(r_li_1000))

# ================== 10000 =======================================================================================================
# timing with bubble
pk1 = time.perf_counter()  
bubble_sort(r_li_10000)
pk2 = time.perf_counter()
p_bubble = pk2 - pk1
print(p_bubble, "bubble sort time")
# timing with built-in
pk3 = time.perf_counter()
sorted(r_li_10000)
pk4 = time.perf_counter()
p_py = pk4 - pk3
print(p_py, "Python buil-in sort time")

# overall result comparison
print("Built-in Python sorting function is",round(p_bubble/p_py,2), "times faster than bubble sort for list of", len(r_li_10000))