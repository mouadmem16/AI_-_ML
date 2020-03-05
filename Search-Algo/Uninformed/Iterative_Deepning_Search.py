import Depth_Limited_Search as LimitDFS

#############################################################
def DFSIterLimited(graph, node, goal):
    if(goal not in graph or node not in graph): return []
    path = []
    level = 1
    queue = [node]
    levelGraph = 0
    levelGraph = Length(graph, queue, levelGraph)
    while node not in path or level < levelGraph:
        paths = LimitDFS.DFSLimited(graph, node, level)
        path = LimitDFS.getSolution(paths, node, goal)
        level += 1
    return(path)
#############################################################
def Length(graph, queue, lvl):
    if len(queue) == 0: 
        return lvl
    TmpQueue = [x for x in queue]
    queue.clear()
    for n in TmpQueue:
        for i in graph[n]: 
            queue.append(i)
    lvl += 1
    return Length(graph, queue, lvl)
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
goal = "7"
level = 1
path = DFSIterLimited(Graph, start, goal)
print(path)