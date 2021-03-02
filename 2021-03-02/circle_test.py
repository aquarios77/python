# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:26:18 2021

@author: antons.sincovs

"""

from circle import Circle

c1 = Circle((1,5) , 4)
c2 = Circle()
print(c1)
print(type(c1))

print("c1: " , c1.get_center(), c1.get_radius())
print("c2: " , c2.get_center(), c2.get_radius())

c1.move((10, 11))
c1.grow()

print("c1: " , c1.get_center(), c1.get_radius())

print("c1 area" , c1.get_area() , "circumference: " , c1.get_circumference())
print("c2 area" , c2.get_area() , "circumference: " , c2.get_circumference())
print(str(c1))
print(c1)

print("c1 x:", c1.get_x(), "y:", c1.get_y())

print("Distance between c1 and c2: " , c1.distance(c2))
print("Distance between c1 and (0,0): " , c1.distance())