# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:06:17 2019

@author: kumar
"""
ch=input('Enter shape( round/elipse)')
if ch=='round':
    S=1
else:
    S=-1    
ch=input('Enter texture( smooth/rough)')
if ch=='smooth':
    T=1
else:
    T=-1    
ch=int(input('Enter weight( in pound)'))
if ch >= 1:
    w=1
else:
    w=-1    
import numpy as np
I=np.array([S,T,w])
Wt=np.array([0,1,0])
b=0
n=np.dot(Wt,I)+b
if n>0:
    print('apple')
else:
    print('orange')