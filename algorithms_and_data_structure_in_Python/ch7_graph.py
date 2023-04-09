from mylib.graph import Graph, Vertex
from mylib.queue import Queue
from mylib.tree import BinaryHeap
from sys import maxsize

def buildGraph(wordFile):
    d:dict[str, list[str]] = {}
    g = Graph()
    with open(wordFile, 'r') as wfile:
        for line in wfile:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.addEdge(word1, word2)
    return g

def bfs(g:Graph, start:Vertex):
    start.distance = 0
    start.predecessor = None
    for v in g:
        v.color = "white"
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.color == "white":
                nbr.color = "gray"
                nbr.distance = currentVert.distance + 1
                nbr.predecessor = currentVert
                vertQueue.enqueue(nbr)
        currentVert.color = "black"

def traverse(y:Vertex):
    x = y
    while x.predecessor:
        print(x.getId())
        x = x.predecessor
    print(x.getId())

class KGraph:
    @staticmethod
    def knightGraph(bdSize):
        ktGraph = Graph()
        for row in range(bdSize):
            for col in range(bdSize):
                nodeId = KGraph.posToNodeId(row, col, bdSize)
                newPositions = KGraph.genLegalMoves(row, col, bdSize)
                for e in newPositions:
                    nid = KGraph.posToNodeId(e[0], e[1], bdSize)
                    ktGraph.addEdge(nodeId, nid)
        return ktGraph

    @staticmethod
    def genLegalMoves(x, y, bdSize):
        newMoves = []
        moveOffsets = [
            (-1,-2), (-1, 2), (-2,-1), (-2, 1),
            ( 1,-2), ( 1, 2), ( 2,-1), ( 2, 1)
        ]
        for i in moveOffsets:
            newX = x + i[0]
            newY = y + i[0]
            if KGraph.legalCoord(newX, bdSize) and KGraph.legalCoord(newY, bdSize):
                newMoves.append((newX, newY))
        return newMoves

    @staticmethod
    def legalCoord(x, bdSize):
        return x >= 0 and x < bdSize

    @staticmethod
    def posToNodeId(row, col, bdSize) -> int:
        return row * bdSize + col
    
    @staticmethod
    def knightTour(n, path:list[Vertex], u:Vertex, limit):
        u.color = 'gray'
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections())
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].color == 'white':
                    done = KGraph.knightGraph(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:
                path.pop()
                u.color = 'white'
        else:
            done = True
        return done
    
    @staticmethod
    def orderByAvail(n:Vertex):
        resList = []
        for v in n.getConnections():
            if v.color == "white":
                c = 0
                for w in v.getConnections():
                    if w == "white":
                        c = c + 1
                resList.append((c, v))
        resList.sort(key = lambda x: x[0])
        return [y[1] for y in resList]

def dijkstra(aGraph:Graph, start:Vertex):
    pq = BinaryHeap()
    start.distance = 0
    pq.buildHeap([(v.dist, v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delFirst()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.distance + currentVert.getWeight(nextVert)
            if newDist < nextVert.distance:
                nextVert.distance = newDist
                nextVert.predecessor = currentVert
                pq.decreaseKey(nextVert, newDist)

def prim(G:Graph, start:Vertex):
    pq = BinaryHeap()
    for v in G:
        v.distance = maxsize
        v.predecessor = None
    start.distance = 0
    pq.buildHeap([(v.distance, v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delFirst()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getWeight(nextVert) + currentVert.distance
            if nextVert in pq and newCost < nextVert.distance:
                nextVert.predecessor = currentVert
                nextVert.distance = newCost
                pq.decreaseKey(nextVert, newCost)

if __name__ == "__main__":
    pass