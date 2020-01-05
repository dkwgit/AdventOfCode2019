from Explorer import Explorer

class Traveler(Explorer):

    def __init__(self, universe, generation, pos, maze, lastPathTaken, keyOrder, keys, edge, destinationVertex, lengthToTravel):
        super(universe, generation, pos, maze, lastPathTaken, keyOrder, keys)
        self._edge = edge
        self._destinationVertex = destinationVertex
        self._lengthToTravel = lengthToTravel

    def Evaluate(self):
        return None

    def SetupForNextGeneration(self):
        self._pos = self._destinationVertex._pos
        if (self._destinationVertex == self._edge._vertexB):
            self._lastPathTaken = self._edge._path
        else:
            self._lastPathTaken = self._edge._path.copy().reverse()
        if (self._lengthToTravel == 0):
            super().SetupForNextGeneration()
        else:
            traveler = Traveler(self._universe, self._generation + 1, self._destinationVertex, self._maze, self._lastPathTaken, self._keyOrder, self._keys, self._edge, self._destinationVertex, self._lengthToTravel - 1)
            self._universe.AddWorldsForEvaluation([traveler])
