import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
class cal():
    def __init__(self,learning_rate,number_iteration):
        self.learning_rate=learning_rate
        self.number_iteration=number_iteration
    def fit(self,Input,target):
        self.w=np.zeroes(1+Input.shape[1])
        for _ in range(self.number_iteration):
            for xi,t in zip(Input,target):
                update=self.learninig_rate*(t-self.predict(xi))
                self.w[1:]=update*xi
                self.w[0]=update*1
    def net_input(self,Input):
        return np.dot(Input,self.w[1:])+self.w[0]
    def predict(self,input1):
        return np.where(self.net_input(Input)>=0,1,-1)

