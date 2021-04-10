# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:24:00 2021

@author: antons.sincovs
"""

class Prece:
    # constructor initializing name and volume
    def __init__(self, preceName='Default Product', precePrice=0.0):
         self.name = preceName
         self.price = precePrice
    
    # method returns object's name
    def preces_nosaukums(self):
        return self.name
    
    # method returns object's price
    def preces_cena(self):
        return self.price
    
    # overriding default str() method
    def __str__(self):
         return '<prece> ' + self.name + ' , ' + str(self.price) + ' </prece>'
     
     # overriding default repr() method
    def __repr__(self):
         return '(' + self.name + ',' + str(self.price) + ')'