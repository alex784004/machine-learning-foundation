# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:43:01 2019

@author: kumar
"""

import numpy as np
x=np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[0,1,0],[1,0,1],[1,1,0],[1,1,1]])
w=np.array([1,-1,-1])
b=np.array([-.5])
n=np.sum(w*x,axis=1)+b
print(n)
out=np.where(n>0,1,0)
print(out)
target=np.array([0,0,0,0,1,1,1,1])
e=target-out
se=np.abs(e).sum()
print('Mean absolute Error=',se/x.shape[0])