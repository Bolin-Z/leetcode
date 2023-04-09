"""graph.py directed graph structure
"""
from _collections_abc import dict_keys

__all__ = ["Graph"]

class Vertex:
    def __init__(self, key, distance=0, predecessor=None, color="white") -> None:
        self.id = key
        self.connectedTo:dict[Vertex, object] = {}
        self.__distance = distance
        self.__predecessor = predecessor
        self.__color = color
    
    def addNeighbor(self, nbr, weight = 0) -> None:
        self.connectedTo[nbr] = weight
    
    def __str__(self) -> str:
        return str(self.id) + ' connectedTo: ' + str([x for x in self.connectedTo])
    
    def getConnections(self) -> dict_keys:
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    @property
    def distance(self):
        return self.__distance
    
    @distance.setter
    def distance(self, newdata):
        self.__distance = newdata
    
    @property
    def predecessor(self):
        return self.__predecessor
    
    @predecessor.setter
    def predecessor(self, newdata:"Vertex2"):
        self.__predecessor = newdata
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, newdata):
        self.__color = newdata

class Graph:
    def __init__(self) -> None:
        self.vertList:dict[object, Vertex] = {}
        self.numVertices = 0

    def addVertex(self, key) -> Vertex:
        self.numVertices = self.numVertices +  1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n) -> Vertex | None:
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    
    def getVertices(self) -> dict_keys[object, Vertex]:
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())

class DFSGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.time = 0
    
    def dfs(self):
        for aVertex in self:
            aVertex.color = "white"
            aVertex.predecessor = -1
        for aVertex in self:
            if aVertex.color == "white":
                self.dfsvisit(aVertex)
    
    def dfsvisit(self, startVertex:Vertex):
        startVertex.color = "gray"
        self.time += 1
        startVertex.discovery = self.time
        for nextVertex in startVertex.getConnections():
            if nextVertex.color == "white":
                nextVertex.predecessor = startVertex
                self.dfsvisit(nextVertex)
        startVertex.color = "black"
        self.time += 1
        startVertex.finish = self.time