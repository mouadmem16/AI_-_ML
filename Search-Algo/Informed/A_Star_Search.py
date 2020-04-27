class CustumSet(set):
    def __getitem__(self, id):
        for elt in list(self):
            if elt.id == id:
                return elt
    
    def __contains__(self, id):
        for elt in list(self):
            if elt.id == id:
                return True
        return False

# neighbours = [{"kjznsa", 2}, ... ]
class Element(object):
    def __init__(self, id, Gcost = 0, parent = None ,neighbours = None):
        self.id = id
        self.Gcost = Gcost
        self.Fcost = Gcost + 2 #Hcost depends on the problem
        self.parent = parent
        if neighbours != None:
            self.neighbours = neighbours
        else: 
            self.neighbours = {}

    def __eq__(self, other):
        return self.id == other.id
    
    def __eq__(self, other):
        return self.id == other

    def __hash__(self):
        return hash(self.id)

    def __lt__(self, other):
        return self.Fcost < other.Fcost

    def __str__(self):
        return self.id
    
    def __repr__(self):
        return self.id

def A_Star(Graph, start, goal):
    OPEN = CustumSet()
    CLOSED = CustumSet()
    OPEN.add(Graph[start])

    while OPEN != {}:
        current = min(OPEN)
        OPEN.remove(current)
        CLOSED.add(current)

        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(start)
            return path
            
        for neighbour, weight in current.neighbours.items():
            if neighbour not in CLOSED and neighbour != None:
                try:
                    node = OPEN[neighbour]
                    if current.Fcost + weight < node.Fcost:
                        node.Fcost = current.Fcost + weight
                        node.parent = current
                except AttributeError:
                    OPEN.add(Element(neighbour, current.Gcost + weight, current, Graph[neighbour].neighbours))

GRAHE = CustumSet()
GRAHE.add(Element("aaa", neighbours={"aba":2, "aca": 3, "aia": 0}))
GRAHE.add(Element("aba", neighbours={"ada":3, "aea": 4}))
GRAHE.add(Element("aca", neighbours={"afa":5, "aja": 6, "aha": 1}))
GRAHE.add(Element("ada"))
GRAHE.add(Element("aea"))
GRAHE.add(Element("afa"))
GRAHE.add(Element("aja"))
GRAHE.add(Element("aha"))
GRAHE.add(Element("aia", neighbours={"aja":2}))

print(A_Star(GRAHE, "aaa", "aja"))