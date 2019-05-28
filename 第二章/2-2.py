import numpy as np
import random as rdn
class Perceptron():
    def __init__(self):
        self.w = np.zeros((2,))
        self.b = 0
        self.learning_rate = 1
    def train(self,x,y):
        flags = [0]*len(x)
        while True:
            i = rdn.randint(0,len(x)-1)
            if flags[i] == True:
                continue
            if y[i]*(np.dot(x[i],self.w)+self.b) > 0:
                flags[i]=1
                if np.sum(flags)>=len(x):
                    break
            else:
                self.w = self.w + self.learning_rate*y[i]*x[i]
                self.b = self.b + self.learning_rate*y[i]
                flags = [0]*len(x)
    def showwb(self):
        print("w:",self.w,' b:',self.b)
x = [[3,3],[4,3],[1,1]]
y = [1,1,-1]
x_array = np.asarray(x)
y_array = np.asarray(y)
p = Perceptron()
p.train(x_array,y_array)
p.showwb()
