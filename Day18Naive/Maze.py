import numpy as np
from enum import Enum

class KeyStates(Enum):
    keyWithoutDoorNetYetFound = -1
    keyFound = 0
    keyWithDoorNotYetFound = 1

class Maze:
    
    wall = ord('#')
    empty = ord('.')
    entrance = ord('@')

    def __init__(self, totalY, totalX):
        self._data = np.zeros((totalY,totalX),np.uint8)
        self._totalY = totalY
        self._totalX = totalX
        self._entrance = None
        self._adjacentsCache = {}
        self._lowDoor = ord('A')
        self._highDoor = ord('Z')
        self._lowKey = ord('a')
        self._highKey = ord('z')

    def GetKeyDoorDict(self):
        doorsExist = {}
        doors = {}
        unique = np.unique(self._data)
        for u in unique:
            if self._lowDoor <= u <= self._highDoor:
                doorsExist[u] = 1
            if self._lowKey <= u <= self._highKey:
                if ((u-32) in doorsExist.keys()):
                    doors[u-32] = KeyStates.keyWithDoorNotYetFound
                else:
                    doors[u-32] = KeyStates.keyWithoutDoorNetYetFound
        return doors

    def CheckForNewKey(self, val, doors):
        if (not (self._lowKey <= val <= self._highKey)):
            return False
        if (doors[val-32] == KeyStates.keyWithDoorNotYetFound or doors[val-32] == KeyStates.keyWithoutDoorNetYetFound):
            doors[val-32]=KeyStates.keyFound
            return True
        return False

    def AddPoint(self, pos, ch):
        y,x = pos
        self._data[y][x] = ord(ch)
        if (ch == '@'):
            self._entrance = pos

    def GetAdjacents(self, pos):
        if (pos not in self._adjacentsCache.keys()):
            (y,x) = pos
            adjacents = []
            if (y != 0):
                val = self._data[y-1][x]
                if (val != Maze.wall):
                    adjacents.append(((y-1,x),val))
            if (y + 1 < self._totalY):
                val = self._data[y+1][x]
                if (val != Maze.wall):
                    adjacents.append(((y+1,x),val))
            if (x != 0):
                val = self._data[y][x-1]
                if (val != Maze.wall):
                    adjacents.append(((y,x-1),val))
            if (x + 1 < self._totalX):
                val = self._data[y][x+1]
                if (val != Maze.wall):
                    adjacents.append(((y,x+1),val))
            self._adjacentsCache[pos] = adjacents
        return self._adjacentsCache[pos]

    def GetPossibleMoves(self, pos, doors, lastPathTaken):
        adjacents = self.GetAdjacents(pos)
        
        closedDoors = { adjPos:val for adjPos,val in adjacents if self._lowDoor <= val <= self._highDoor and doors[val] != KeyStates.keyFound}
        
        filteredAdjacents = [(adjPos,val) for adjPos,val in adjacents if adjPos not in closedDoors.keys() and adjPos not in lastPathTaken.keys()]
        return filteredAdjacents        

