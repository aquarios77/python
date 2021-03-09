# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 20:34:38 2021

@author: antons.sincovs
"""

from ndim_vector import ndimVector

v1 = ndimVector((1,3,5))
v2 = ndimVector((1,3,5))
print(str(v1))
print(str(v2))
print(v1.module())
print(v2.module())
print((v1 + v2).module())
print((v1 - v2).module())
print(v1 * 2)
print(2 * v1)
print(v1 * v2)
print(v1 == v2)
print(v1 != v2)