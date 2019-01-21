# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:28:04 2019

@author: kumar
"""

import numpy as np
x=np.arange(-10,10,0.1)
print(x)

print(np.amax(x))
print(np.amin(x))
print(np.sum(x))
print(np.average(x))
print(np.std(x))
print(np.var(x))
##
a=np.array([1,2,3,4,5])
print(a)
print(type(a))
print(a.shape)
print(a.size)
##
a=np.array([[1,2,3],[3,4,5]])
print(a)
print(type(a))
print(a.shape)
print(a.size)
print(np.amax(a))
print(np.amax(a,axis=0))#columnwise maximum value
print(np.amax(a,axis=1))#rowise maximum value
