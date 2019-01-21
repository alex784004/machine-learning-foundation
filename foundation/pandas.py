# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:47:37 2019

@author: kumar
"""
import pandas as pd
x=pd.read_csv('Book1.csv')
x.columns=['a','b','c']
y=pd.read_csv('Book1.csv',header=None)

print(x)
print(y)
 
a=x.describe()
print(a)
a.to_csv('Book1.csv')
print(x.columns)
print(x.head())
print(x.tail())
import matplotlib.pyplot as plt
plt.plot(x['a'].values,x['b'].values)
plt.show()