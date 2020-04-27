
# 1 2
# 1 3
# 1 4 
# 1 2 5
# 1 2 6

#############################################################
def BFS(Graph, s):
    pred = {}
    queue = []
    visited = {}
    cost = {}
    for x in Graph: visited[x] = False
    for x in Graph: cost[x] = 0
    queue.append(s)
    visited[s] = True
    while queue:
        s = queue.pop(0)
        for i in Graph[s]: 
            if visited[i] == False:
                queue.append(i)
                cost[i] = cost[s]+5
                visited[i] = True
                pred[i]=s
    return pred
#############################################################
def getSolution(path, s, g):
    sol = []
    sol.append(g)
    while g != s:
        g = path[g]
        sol.append(g)
    return sol
#############################################################

Graph = {
    "1":["2", "3", "4"],
    "2":["5", "6"],
    "3":["7", "8"],
    "4":[],
    "5":[],
    "6":[],
    "7":[],
    "8":[],
}

start = "1"
goal = "8"
path = BFS(Graph, start)
print(getSolution(path, start, goal))







