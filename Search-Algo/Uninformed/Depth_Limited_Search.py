

#############################################################
def DFSLimited(graph, node, level):
    stack = [node]
    pred = {}
    visited = {}
    cost = {}
    for x in graph: visited[x] = False
    for x in graph: cost[x] = 0
    
    queue = [node]
    def MarkLevels(level):
        if len(queue) == 0: return
        TmpQueue = [x for x in queue]
        queue.clear()
        for n in TmpQueue:
            for i in graph[n]: 
                queue.append(i)
        level -= 1
        if level < 1:
            for child in queue:
                visited[child] = True
        MarkLevels(level)
    
    MarkLevels(level)

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
        try:
            g = path[g]
        except KeyError as identifier:
            break
        sol.append(g)
    return sol
#############################################################

# Graph = {
#     "1":["2", "3", "4"],
#     "2":["5", "6"],
#     "3":["7", "8"],
#     "4":[],
#     "5":[],
#     "6":[],
#     "7":[],
#     "8":[],
# }

# start = "1"
# goal = "4"
# level = 1
# paths = DFSLimited(Graph, start, level)
# path = getSolution(paths, start, goal)
# print(path)