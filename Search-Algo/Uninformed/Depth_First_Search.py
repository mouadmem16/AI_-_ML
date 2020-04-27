

#############################################################
def DFS(graph, node):
    stack = [node]
    pred = {}
    visited = {}
    cost = {}
    for x in Graph: visited[x] = False
    for x in Graph: cost[x] = 0

    while stack:
        node = stack[-1]
        if visited[node] == False: visited[node] = True
        remove_from_stack = True
        for next in graph[node]:
            if visited[next] == False:
                stack.extend(next)
                remove_from_stack = False
                pred[next]=node
                break
        if remove_from_stack:
            stack.pop()
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
goal = "5"
path = DFS(Graph, start)
print(getSolution(path, start, goal))