class Robot:
    def __init__(self,computer):
        self._computer = computer
        self._currentPosition = (0,0)
        self._currentDirection = (0,1)
        self._coveredTiles = {}
        self._moves = 0


        self._rightTurns = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1):(-1,0),
            (-1,0):(0,1)
        }
        self._leftTurns = {
            (0,1): (-1,0),
            (-1,0): (0,-1),
            (0,-1):(1,0),
            (1,0): (0,1)
        }

    def GetColorToPaintSquare(self,value):
        self._computer.SetInput([value])
        continueRun = True
        result = None
        while (continueRun and result is None): 
            oneResult, continueRun, inputNext = self._computer.DoNext()
            if (oneResult is not None):
                result = oneResult
        assert(continueRun)
        return oneResult
    
    def GetNextTurn(self):
        continueRun = True
        result = None
        while (continueRun and result is None): 
            oneResult, continueRun, inputNext = self._computer.DoNext()
            if (oneResult is not None):
                result = oneResult
        assert(continueRun)
        return result

    def GetColorOfCurrentPosition(self):
        if (self._currentPosition not in self._coveredTiles.keys()):
            return self._startColor  #Technially a bug.  I should be saying it's black if unknown and not the start
                                     #but it still worked.
        else:
            return self._coveredTiles[self._currentPosition]

    def PaintColorOfCurrentPosition(self,color):
        self._coveredTiles[self._currentPosition] = color

    def ChangeDirection(self, turn):
        if (turn == 0):
            self._currentDirection = self._leftTurns[self._currentDirection]
        elif(turn == 1):
            self._currentDirection = self._rightTurns[self._currentDirection]
        else:
            assert(0==1)

    def Move(self):
        x,y = self._currentPosition
        if (self._currentDirection == (0,1)):
            y = y + 1
        elif (self._currentDirection == (1,0)):
            x = x + 1
        elif (self._currentDirection == (0,-1)):
            y = y -1
        elif (self._currentDirection == (-1,0)):
            x = x -1
        else:
            assert(0==1)
        self._currentPosition = (x,y)
        self._moves = self._moves + 1

    def Run(self, startColor = 1):
        self._startColor = startColor
        continueRun = True
        inputNext = False
        while(continueRun):
            if (self._computer.PeekAtOpCodeValue()==3):
                color = self.GetColorToPaintSquare(self.GetColorOfCurrentPosition())
                self.PaintColorOfCurrentPosition(color)
                turn = self.GetNextTurn()
                self.ChangeDirection(turn)
                self.Move()
            else:
                oneResult, continueRun, inputNext = self._computer.DoNext() 
        print(f"Covered {len(self._coveredTiles.keys())} tiles") #1932 on Day11-1
        maxX = max(self._coveredTiles.keys(), key=lambda x: x[0])
        minX = min(self._coveredTiles.keys(), key=lambda x: x[0])
        maxY = max(self._coveredTiles.keys(), key=lambda x: x[1])
        minY = min(self._coveredTiles.keys(), key=lambda x: x[1])
        print(f"min x: {minX}; max x {maxX}; min y: {minY}; max y: {maxY}")
        minX = minX[0]
        maxX = maxX[0]
        minY = minY[1]
        maxY = maxY[1]
        # Start drawing a row (line) at maxY height (further rows descending to minY), from minX to maxX across.
        # This means we don't have to do coordinate adjustments.  The last line can be thought of as y=0
        # regardless of actual y value at that point.
        lines= []
        for y in range(maxY,minY-1,-1):
            line = ''
            for x in range(minX,maxX+1):
                point = (x,y)
                if point in self._coveredTiles.keys():
                    color = self._coveredTiles[point]
                else:
                    color = 0
                if (color == 1):
                    char = '*'
                else:
                    char= ' '
                line = line + char
            lines.append(line)
        for ln in lines:
            print(ln)  #Should give EGHKGJER

