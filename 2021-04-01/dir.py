# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:53:11 2021

@author: antons.sincovs
"""

import os
from datetime import datetime
print(os.getcwd())
print(os.path.abspath("dir.py"))
print(os.listdir())

scan = os.scandir()
for el in scan:
    print(el)
    
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%F %H:%M')
    return formated_date

with os.scandir() as entries:
    for entry in entries:
        info = entry.stat()
        print("Size:" , info.st_size , "bytes")
        print("Modification date:" , convert_date(info.st_mtime))


import glob, os
os.chdir(".")
for file in glob.glob("*.py"):
    print(file) 