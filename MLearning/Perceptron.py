import pandas as pd
import os
import matplotlib.pyplot as plt
import math
from collections import Counter
import numpy as np

class Perceptron(object):
    weights = []

    def __init__(self, inpt, weights, output, alfa):
        self.inpt = inpt
        self.output = output
        self.alfa = alfa
        Perceptron.weights = weights

    # Somme of production
    def SOP(self):
        # Bias (to move decison boundry)
        somme = self.weights[0] 
        for i in range(1, len(self.inpt)):
            somme += self.inpt[i] * self.weights[i]
        return somme 

    # the activation function
    def ACT(self, sop):
        # {0, 1}
        def Threshold():
            if sop > 0 :
                return self.output[0]
            else:
                return self.output[1]
        
        # [-infini, +infini]
        def Rampe():
            return sop
        return Threshold()

    # the period can be train or test 
    def Verify(self, out, iter, period="train"):
        sop = self.SOP()
        act = self.ACT(sop)
        if act == out or iter <= 0: 
            print(Perceptron.weights)
            return act
      
        def method1():
            Perceptron.weights[0] = Perceptron.weights[0] + 0.5 * self.alfa * math.pow( out - act, 2 )
            for i in range(1, len(Perceptron.weights)):
                # function of correction weights 
                Perceptron.weights[i] = Perceptron.weights[i] + 0.5 * self.alfa * math.pow( out - act, 2 )
      
        def method2():
            Perceptron.weights[0] = Perceptron.weights[0] - self.alfa * ( out - sop )
            for i in range(1, len(Perceptron.weights)):
                # function of correction weights 
                Perceptron.weights[i] = Perceptron.weights[i] - self.alfa * ( out - sop ) * self.inpt[i-1]

        if period == "train":
            method2()
            # repeat Verify till get the right answer
            iter -= 1
            return self.Verify(out, iter)



# alfa(learning rate) between 0(slower but quite result) and 1(faster)
alfa = 0.0001

# the importance of the data (weights)
weights = [-1.2, 1.0009, 1] 

# how the output is represented
output = [1, 2]

# number of iterations in verify for correcting
iter = 10

# Our data
train =pd.read_csv("synth_train.txt", sep='\t')
test=pd.read_csv("synth_test.txt", sep='\t')
Xtrain=train[['x1','x2']].values
Ytrain=train.iloc[:,0].values
Xtest=test[['x1', 'x2']].values
Ytest=test.iloc[:,0].values

XTrainC1 = []
XTrainC2 = []
for i in range(len(Xtrain)):
    if Ytrain[i] == 2:
        XTrainC1.append(Xtrain[i].tolist())
    else: XTrainC2.append(Xtrain[i].tolist()) 
XTrainC1 = np.array(XTrainC1)
XTrainC2 = np.array(XTrainC2)

# the Training period hehe
for i in range(len(Ytrain)):
    x = [Xtrain[i,0], Xtrain[i,1]]
    objPerc = Perceptron(x, weights, output, alfa)
    validate = objPerc.Verify(Ytrain[i], iter)



XTestC1 = []
XTestC2 = []
XTestC3 = []
for i in range(len(Xtest)):
    x = [Xtest[i,0], Xtest[i,1]]
    objPerc = Perceptron(x, weights, output, alfa)
    validate = objPerc.Verify(Ytest[i], iter, "test")
    if Ytest[i] == validate:
        if validate == 1: XTestC2.append(Xtest[i].tolist()) 
        else: XTestC1.append(Xtest[i].tolist())
    else : XTestC3.append(Xtest[i].tolist()) 
XTestC1 = np.array(XTestC1)
XTestC2 = np.array(XTestC2)
XTestC3 = np.array(XTestC3)

plt.scatter(XTestC1[:,0], XTestC1[:,1], c="green", label='class1')
plt.scatter(XTestC2[:,0], XTestC2[:,1], c="red", label="class2")
plt.scatter(XTestC3[:,0], XTestC3[:,1], c="blue", label="class3")

plt.legend()
plt.show()