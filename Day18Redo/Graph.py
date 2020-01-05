from Edge import Edge
from Vertex import Vertex

class Graph:

    def __init__(self,numberofVertices):
        self._verticesByPos = {}
        self._verticesByName = {}
        self._edges = {}

    def vertex_exists(name)

    def addvertex(self, pos, name):
        insert = False
        if (name not in self._verticesByName.keys()):
            assert(pos not in self._verticesByPos.keys())
            insert = True
        if (pos not in self._verticesByPos.keys()):
            assert(name not in self._verticesByName.keys())
            insert = True
        if (insert):
            v = Vertex(self, pos, name)
            self._verticesByName[name] = v
            self._verticesByPos[pos] = v

    def addedge(self, graph, vertexA, vertexB, distance, path):
        edge = Edge(self, vertexA, vertexB, distance, path)
        add = False
        if (edge._edgekey not in self._edges.keys()):
            add = True
            self._edges[edge._graphKey()] = edge._distance
        else:
            current = self._edges[edge._graphKey()]
            if (edge < current):
                add = True
                self._edges[edge._graphKey()] = edge._distance
        if (add):
            vertexA._addedge(edge)
            vertexB._addedge(edge)