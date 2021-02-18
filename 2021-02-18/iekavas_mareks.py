# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:58:22 2021

@author: antons.sincovs
"""

s = input('Ievadiet iekavu virkni')
  #s = '({({}[])}[{}]())'
  
temp = ''
if not len(s) % 2:
  while temp != s:
    temp = s
    s = s.replace('{}', '').replace('[]', '').replace('()', '')

if len(s) > 0:
  print('Iekavas nav pareizi sakartotas.')
else:
  print('Iekavas ir pareizi sakartotas.')