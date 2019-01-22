# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:34:37 2019

@author: kumar
"""
import matplotlib.pyplot as plt
import numpy as np

#sigmoidal fuunction
x=np.arange(-10,10.1,0.1)
y=1/(1+np.exp(-x))
plt.plot(x,y)
plt.show()

#tanh 
x=np.arange(-10,10.1,0.1)
y=2/(1+np.exp(-2*x))-1
plt.plot(x,y)
plt.show()
