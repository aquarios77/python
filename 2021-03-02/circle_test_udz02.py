# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:34:11 2021

@author: antons.sincovs
"""

from circle import Circle
from random import randint

rinku_saraksts = [ Circle((randint(-50,50), randint(-50,50)), randint(1,10)) for _ in range (10)]

closest = None
circle = ""

for rinkis in rinku_saraksts:
    if closest == None:
        closest = rinkis.distance()
    else:
        if rinkis.distance() < closest:
            closest = rinkis.distance()
            circle = str(rinkis)
    print(rinkis , rinkis.distance())

print("Closest: ", closest, "Circle: ", circle)