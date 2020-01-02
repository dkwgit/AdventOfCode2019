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
        self._doors = {}
        self._keys = {}
    
    def Lookup(self,y,x):
        return self._data[y][x]

    def AddPoint(self, pos, ch):
        y,x = pos
        asciiCode = ord(ch)
        self._data[y][x] = asciiCode
        if (ch == '@'):
            self._entrance = pos
        if (self._lowKey <= asciiCode <= self._highKey):
            self._keys[pos] = asciiCode
        if (self._lowDoor <= asciiCode <= self._highDoor):
            self._doors[pos] = asciiCode

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

    def GetPossibleMoves(self, pos, keys, lastPathTaken):
        adjacents = self.GetAdjacents(pos)
        
        closedDoors = { adjPos:val for adjPos,val in adjacents if adjPos in self._doors.keys() and (val+32) not in keys.keys()}
        
        filteredAdjacents = [(adjPos,val) for adjPos,val in adjacents if adjPos not in closedDoors.keys() and adjPos not in lastPathTaken.keys()]
        return filteredAdjacents        

