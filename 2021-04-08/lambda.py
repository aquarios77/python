# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 18:23:09 2021

@author: antons.sincovs
"""

def lielaks_par_18(x):
    return x>18

s1 = [20 , 5 , 12 , 17 ,18 , 24 , 32]
s2 = filter(lielaks_par_18 , s1)

print(*s2)

s3 = filter(lambda x: x > 18 , s1)

print(*s3)

s4 = [x for x in s1 if x > 18]

print(*s4)

s5 = [x for x in s1 if (lambda x: x > 18)(x)]
print(*s5)

test = lambda x: True if(x > 10 and x < 20) else False
test2 = lambda x: 10 < x < 20
test3 = lambda x: "Der" if (10 < x < 20) else "Neder"
test3 = lambda x: x*3 if(10 < x < 20) else(x*2 if x>30 else x)
print(test(15))
print(test(3))
print(test2(5))
print(test3(7))

v1 = [1 , 3 , 6 , 8]
v2 = [4 , 7 , 9 , 2]

s1 = [x , y for x , y in v1 , v2]

