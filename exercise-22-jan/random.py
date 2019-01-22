# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:19:49 2019

@author: kumar
"""
import numpy as np
x=np.arange(0,10.1,0.1)
print(x)
#x=np.random.randint(-10,10)#randint(minimum,maximum) generating a random integer
w=np.random.randint(-10,10,size=x.size,dtype=np.int16)
print(w)
b=np.random.random()
print(b)
## 
#i=np.dot(w,x)+b
i=(w*x).sum()+b
#for threshold
if i>=0:
    print('1')
else:
    print('0')
##b=np.random.rand()#generating random integer from 0 to 1
##for log sigmoid
out=1/(1+np.exp(-i))
print(out)