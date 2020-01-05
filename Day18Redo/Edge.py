import os
import sys
sys.path.append(os.path.abspath('../Mixins'))
from ComparableMixin import ComparableMixin

class Edge(ComparableMixin):

    def _compkey(self):
        return (self._vertexA, self._vertexB, self._distance)

    def _graphkey(self):
         # graph keeps shortest known edge between two vertices.  This helps finding that
        return (self._vertexA, self._vertexB)
    
    def __init__(self, graph, vertexA, vertexB, distance, path):
        assert(len(distance)==len(path))
        self._graph = graph
        if (vertexA > vertexB):
            temp = vertexB
            vertexB = vertexA
            vertexA = temp
        self._vertexA = vertexA
        self._vertexB = vertexB
        self._distance = distance
        self._path = path
