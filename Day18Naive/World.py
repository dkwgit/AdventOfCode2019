from Maze import Maze

class World:

    def __init__(self, universe, generation, pos, maze, totalPath, lastPathTaken, keyOrder, doors = None):
        self._universe = universe
        self._generation = generation
        self._pos = pos
        y,x = pos
        self._maze = maze
        self._val = self._maze._data[y][x]
        self._doors = self._maze.GetKeyDoorDict() if doors is None else doors.copy()
        self._totalPath = totalPath
        self._lastPathTaken = lastPathTaken.copy()
        self._keyOrder = keyOrder
        self._universe.CountWorld(self)

    def EvaluateWorld(self):
        if (self._universe._longestKeyString - len(self._keyOrder) > 1):
            return None
        newKey = False
        self._totalPath = "".join([self._totalPath,"_",str(self._pos)])
        if (self._maze._lowKey <= self._val <= self._maze._highKey):
            newKey = self._maze.CheckForNewKey(self._val, self._doors)
            if (newKey):
                self._keyOrder += chr(self._val)
                self._universe.RegisterKeyStringLength(len(self._keyOrder))
                self._lastPathTaken = {}
                if (len(self._keyOrder)==len(self._doors)):
                    return self
        self._lastPathTaken[self._pos] = 1
        moves = self._maze.GetPossibleMoves(self._pos, self._doors, self._lastPathTaken)
        newWorlds = []
        for m in moves:
            w = World(self._universe, self._generation + 1, m[0], self._maze, self._totalPath, self._lastPathTaken, self._keyOrder, self._doors)
            newWorlds.append(w)
        self._universe.AddWorldsForEvaluation(newWorlds)
        return None







    