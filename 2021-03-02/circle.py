# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:24:46 2021

@author: antons.sincovs
"""

class Circle:
    def __init__(self, center = (0,0), radius = 4):
        if radius < 0:
            raise ValueError("Negative radius!")
        self.center = center
        self.radius = radius
    
    def get_center(self):
        return self.center
    
    def get_radius(self):
        return self.radius
    
    def move(self, pt):
        self.center = pt
        
    def grow(self , step=1):
        self.radius += step
        
    def shrink(self , step=1):
        if self.radius >= 1:
            self.radius -= step
            
    def get_area(self):
        from math import pi
        return round(pi*self.radius**2 , 2)
    
    def get_circumference(self):
        from math import pi
        return round(2*pi*self.radius , 2)
    
    def __str__(self):
        return '<(' + str(self.center) + '), ' + str(self.radius) + '>'
    
    def get_x(self):
        return self.center[0]
    
    def get_y(self):
        return self.center[1]
    
    def distance(self, other=None):
        if other != None:
            x_dif = abs(self.get_x() - other.get_x())
            y_dif = abs(self.get_y() - other.get_y())
            return round((x_dif**2 + y_dif**2)**0.5 , 2)
        else:
            return round((self.get_x()**2 + self.get_y()**2)**0.5 , 2)
    