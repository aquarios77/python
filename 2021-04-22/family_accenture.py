# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 18:39:19 2021

@author: antons.sincovs
"""

class Human:
    def __init__(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
dad = Human("Janis")
mom = Human("Marita")
son = Human("Peteris")

family = [dad , mom , son]

for member in family:
    print("Name: {}".format(member.getName()))