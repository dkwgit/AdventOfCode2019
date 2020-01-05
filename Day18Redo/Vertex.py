import os
import sys
sys.path.append(os.path.abspath('../Mixins'))
from ComparableMixin import ComparableMixin

class Vertex(ComparableMixin):

    def _compkey(self):
        return self._pos

    def __init__(self, graph, pos, name):
        self._graph = graph
        self._pos = pos
        self._name = name
        self._edges = {}

    def _addedge(self, e):
        #should only be called by Graph after graph has check that this edge has the shortest distance between the points
        assert(e._compkey() in self._graph._edges.keys())
        assert(e._vertexA == self or e.vertexB == self)
        self._edges[e._compkey()] = e._distance