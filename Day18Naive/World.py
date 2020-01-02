from Maze import Maze

class World:

    def __init__(self, universe, generation, pos, maze, totalPath, lastPathTaken, keyOrder, keys = None):
        self._universe = universe
        self._generation = generation
        self._pos = pos
        y,x = pos
        self._maze = maze
        self._val = self._maze.Lookup(y,x)
        self._keys = {} if keys is None else keys.copy()
        self._totalPath = totalPath
        self._lastPathTaken = lastPathTaken.copy()
        self._keyOrder = keyOrder
        self._universe.CountWorld(self)

    def EvaluateWorld(self):
        if (self._universe._longestKeyString - len(self._keyOrder) > 1):
            return None
        self._totalPath += ("_" + str(self._pos[0]) + "/" + str(self._pos[1]))
        if (self._maze._lowKey <= self._val <= self._maze._highKey):
            if (self._val not in self._keys.keys()):
                self._keys[self._val] = 1
                self._keyOrder += chr(self._val)
                self._universe.RegisterKeyStringLength(len(self._keyOrder))
                self._lastPathTaken = {}
                if (len(self._keys)==len(self._maze._keys)):
                    return self
        self._lastPathTaken[self._pos] = 1
        moves = self._maze.GetPossibleMoves(self._pos, self._keys, self._lastPathTaken)
        newWorlds = []
        for m in moves:
            w = World(self._universe, self._generation + 1, m[0], self._maze, self._totalPath, self._lastPathTaken, self._keyOrder, self._keys)
            newWorlds.append(w)
        self._universe.AddWorldsForEvaluation(newWorlds)
        return None







    