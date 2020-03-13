import math
import matplotlib.pyplot as plt
import random

class Node(object):
    def __init__(self, id, valuex, valuey, neighbours):
        self.id = id
        self.valuex = valuex
        self.valuey = valuey
        self.neighbours = neighbours

    def __str__(self):
        return str(self.valuex)

    def __repr__(self):
        return str(self.valuex)+ " " + str(self.valuey)

    def __lt__(self, other):
        return self.valuey < other.valuey    

########################################################
def minim(graph, node):
    res = list()
    for x in node.neighbours:
        y = [graph[x].valuey, graph[x].id]
        res.append(y)
    mini = min(res)
    if len(res) == 0 or mini[0] > node.valuey:
        return node.id
    return mini[1]
########################################################
def maxim(graph, node):
    res = list()
    for x in node.neighbours:
        y = [graph[x].valuey, graph[x].id]
        res.append(y)
    maxi = max(res)
    if len(res) == 0 or maxi[0] < node.valuey:
        return node.id
    return maxi[1]
########################################################
def rangeFct(x, N, Nmax):
    res = []
    for i in range(x, x+N):
        if i >= 0 and i < Nmax: res.append(i)
    return res
########################################################
def Stochastic_Hill_Climbing(graph, start):
    opt = start
    while True:
        opt = minim(graph, graph[opt])
        if opt == start:
            opt = random.randint(0,99)
        else:
            start = opt
    return graph[start]
########################################################

Graph = list()
xx = []
yy = []
for i in range(0, 100):
    x = i-50
    xx.append(x)
    yy.append(math.pow(x, 2))
    Graph.append(Node(i, x, math.pow(x, 2), rangeFct(i, 5, 100)))

print(Stochastic_Hill_Climbing(Graph, 0))


plt.plot(xx, yy)
plt.show()