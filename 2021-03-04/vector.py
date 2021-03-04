# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:53:16 2021

@author: antons.sincovs
"""

class Vector:
    def __init__(self, x = 0 , y = 0):
        self.x = x
        self.y = y
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x=0):
        self.x = x
   
    def set_y(self, y=0):
        self.y = y
        
    def module(self):
        return round((self.x ** 2 + self.y ** 2)**0.5 , 2)
       
    
    def __add__(self, other):
       return Vector(self.x + other.x, self.y + other.y)
   
    def __sub__(self, other):
       return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y 
        
    def __eq__(self, other):
        return (self.module() == other.module())
    
    def __ne__(self, other):
        return (self.module() != other.module())
    
    def __getitem__(self, k):
       if k == 0:
           return self.x
       else:
           return self.y
        
    '''
    # short rmul version, Python itself understands, that number can be in the left
    # and vector in the right - rmul- right-multiply
    def __rmul__(self,other):
        return Vector.__mul__(self, other)
    '''
    
    
    
    
    def __str__(self):
        return '--> x:' + str(self.x) + ' y:' + str(self.y) + ' <--'