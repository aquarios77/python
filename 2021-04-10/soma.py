# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:19:31 2021

@author: antons.sincovs
"""
from prece import Prece

class Soma:
    # constructor initializing name and volume
    def __init__(self , somaName='Default Bag' , somaVolume=1):
         self.name = somaName
         self.volume = somaVolume
         self.saturs = []
    
    # method returns object's name
    def ka_mani_sauc(self):
        return self.name
    
    # method returns is_full status
    def vai_pilna(self):
        if len(self.saturs) < self.volume:
            return False
        else:
            return True
     
    # method returns is_empty status
    def vai_tuksa(self):
        if len(self.saturs) == 0:
            return True
        else:
            return False
         
    # method inserts an object of type <Prece> into object <Soma>
    def ielikt(self , lieta):
        if isinstance(lieta, Prece): # checking if the argument passed is of type <Prece>
            if not self.vai_pilna(): # checking if oject <Soma> is not full
                self.saturs.append(lieta) # put an object <Prece> into object <Soma>
                return True
            else:
               # raise Exception("Sorry, but the Bag \"", self.ka_mani_sauc() , " is full!") # raise an exception if object <Soma> is full
                return False
        else:
           raise Exception("Sorry, but you have to pass an object of type <Prece>") # raise an exception if the argument passed is of type <Prece>
           return False
       
    # method pops an object of type <Prece> from object <Soma>
    def iznemt(self):
        if not self.vai_tuksa(): # checking if oject <Soma> is not empty
            return self.saturs.pop() # popping the last object of type <Prece> from object <Soma>
        else:
            return None # if object <Soma> is empty
        
    # method removes all objects of type <Prece> from the <Soma> object
    def iztukshot(self):
        if not self.vai_tuksa(): # checking if oject <Soma> is already not empty
           self.saturs.clear() # clearing the list of type <Prece> objects in object <Soma>
          
    # return an object of type <Prece> with "i" index    
    def __getitem__(self, i):
        if (abs(i) <= len(self.saturs) - 1): # checking if the index argument passed is in current object's range , abs() - because index can be negative counting from the list's end
             return self.saturs[i]
        else:
            raise Exception("Sorry, but the index: ", i, " you specified is out of objects Bag \"", self.ka_mani_sauc() , " range!") # raise an exception if the index is out of current object's range
    
    # return an object of type <Prece> with "i" index    
    def __setitem__(self , i , lieta):
        if isinstance(lieta, Prece): # checking if the argument passed is of type <Prece>
            if (abs(i) <= len(self.saturs) - 1): # checking if the index argument passed is in current object's range , abs() - because index can be negative counting from the list's end
                self.saturs[i] = lieta
            else:
                raise Exception("Sorry, but the index: ", i, " you specified is out of objects Bag \"", self.ka_mani_sauc() , " range!") # raise an exception if the index is out of current object's range
        else:
           raise Exception("Sorry, but you have to pass an object of type <Prece>") # raise an exception if the argument passed is of type <Prece>
          
    # return the sum of all <Prece> object prices put into <Soma>
    def summa(self):
        if self.vai_tuksa(): # checking if the <Soma> is not empty
            return 0.0
        else:
            return sum([float(prece.preces_cena()) for prece in self.saturs]) # int() in case the user created <Prece> objects with non-numeric price
    
    def __str__(self):
        my_list = []
        for prece in self.saturs:
            my_list.append(str(prece))
        return self.name + ':' + ','.join(my_list)
    
    def __repr__(self):
        return '(Name:' + self.name + ', Vol:' + str(self.volume) + ')'
    
    def bag_swap(self, other_bag):
        if isinstance(other_bag, Soma):
            self.saturs , other_bag.saturs = other_bag.saturs , self.saturs
        else:
            raise Exception("Sorry, but you have to pass an object of type <Soma>") # raise an exception if the argument passed is of type <Soma>
    