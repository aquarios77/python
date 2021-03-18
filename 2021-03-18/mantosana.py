# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:12:53 2021

@author: antons.sincovs
"""

class Person:
    pass

class Student(Person):
    pass

print(issubclass(Student, Person))

p = Person()
s = Student()

print(p)
print(s)

print(type(p))
print(type(s))

print(type(s) == Student , type(s) == Person)

print(isinstance(s, Student) , isinstance(s, Person))

print(isinstance(p, Student) , isinstance(p, Person))