# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:53:16 2021

@author: antons.sincovs
"""

class ndimVector:
    def __init__(self, coord):
        self.coord = coord
        
    def module(self):
        return round(( sum(elem**2  for elem in self.coord))**0.5 , 2)
       
    def __add__(self, other):
        if len(other.coord) == len(self.coord):
            summa = []
            self_li = list(self.coord)
            other_li = list(other.coord)
            for i in range(len(self_li)):
                summa.append(self_li[i] + other_li[i])
            return ndimVector(tuple(summa))
      
    def __str__(self):
        s = "n-->"
        for i in range(len(self.coord)):
            s += " dim" + str(i) +":" + str(self.coord[i]) 
        return s + " <--n"
   
    def __sub__(self, other):
       return ndimVector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return ndimVector(self.x * other, self.y * other)
        elif isinstance(other, ndimVector):
            return self.x * other.x + self.y * other.y
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return ndimVector(self.x * other, self.y * other)
        elif isinstance(other, ndimVector):
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
    
    
    
    '''
    def __str__(self):
        return '--> x:' + str(self.x) + ' y:' + str(self.y) + ' <--'
    '''