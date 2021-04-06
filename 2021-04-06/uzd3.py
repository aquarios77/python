# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:19:06 2021

@author: antons.sincovs
"""
import csv

def read_line(file_name, row_num=0):
    counter = 0
    with open(file_name) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if row_num == counter:
                return row
            else:
                counter += 1