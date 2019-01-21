# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:34:56 2019

@author: kumar
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,10,0.01)
y=x
y1=x**2
plt.figure(1)
plt.subplot(321)
plt.plot(x,y,label='y=x')
plt.subplot(325)
plt.plot(x,y,label='y=x^2')
plt.title('X vs Y')
plt.xlabel('X-->')
plt.ylabel('Y-->')
plt.legend()
plt.show()

