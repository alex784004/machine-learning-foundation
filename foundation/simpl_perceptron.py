import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
class perceptron:
    def __init__(self,learning_rate,number_iteration):
        self.learning_rate=learning_rate
        self.number_iteration=number_iteration
    def fit(self,Input,target):
        self.w=np.zeros(1+Input.shape[1])
        for _ in range(self.number_iteration):
            for xi,t in zip(Input,target):
                update=self.learning_rate*(t-self.predict(xi))
                self.w[1:]=update*xi
                self.w[0]=update*1
    def net_input(self,Input):
        return np.dot(Input,self.w[1:])+self.w[0]
    def predict(self,Input):
        return np.where(self.net_input(Input)>=0,1,-1)
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
print('Head part oof data sets...')
print(df.head())
print('Tail part of data sets')
print(df.tail())
print('data set discription...')
print(df.describe())
print('Number of records=',df.shape[0])
print('Number of attrib=',df.shape[1]-1)
a=np.unique(df.iloc[:,4].values)
print('classes=',a)
print('Number of classses=',len(a))
print('Number of records/class')
print(df[4].value_counts())

plt.scatter(df[1],df[2])
plt.show()
data=df.iloc[:,0:2].values
plt.scatter(data[:50,0],data[:50,1],color='red',marker='o',label='iris_setosa')
plt.scatter(data[50:100,0],data[50:100,1],color='green',marker='*',label='Iris-versicolor')
plt.scatter(data[100:150,0],data[100:150,1],color='blue',marker='d',label='Iris-virginica')
plt.legend()
plt.show()


x=df.iloc[0:100,0:2].values
y=df.iloc[0:100,4].values
print(y)
y=np.where(y=='Iris-setosa',1,-1)
print(y)
ppn=perceptron(0.1,10)
ppn.fit(x,y)
Y=ppn.predict([2,2])
if Y==1:
    print('Iris-setosa')
else:
    print('Iris-versicolor')
