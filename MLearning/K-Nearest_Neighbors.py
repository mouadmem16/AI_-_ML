import pandas as pd
import os
import matplotlib.pyplot as plt
import math
from collections import Counter
import numpy as np

#################################################
def K_NN(x1, x2, k):
    distances = []
    for x in range(len(Xtrain)):
        distances.append([Distance([x1, x2], Xtrain[x]), Ytrain[x]])
    distances.sort()
    neighbors = distances[0:k]
    neighbors = [item[1] for item in neighbors]
    x = Counter(neighbors)
    return list(x.keys())[0]
    
def Distance(x, y):
    return math.sqrt(math.pow(x[0]-y[0], 2)+math.pow(x[1]-y[1], 2))
def DistanceHamitolian(x, y):
    return math.sqrt(math.pow(x[0]-y[0], 2)+math.pow(x[1]-y[1], 2))
#################################################

# print(os.execv("/bin/pwd", ['foo', 'bar']))

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

XTestC1 = []
XTestC2 = []
XTestC3 = []
for i in range(len(Xtest)):
    knn = K_NN(Xtest[i,0], Xtest[i,1], 5)
    if Ytest[i] == knn:
        if knn == 1: XTestC2.append(Xtest[i].tolist()) 
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