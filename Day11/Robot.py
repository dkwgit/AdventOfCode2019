class Robot:
    def __init__(self,computer):
        self._computer = computer
        self._currentPosition = (0,0)
        self._currentDirection = (0,1)
        self._tilesCovered = []
        self._coveredTiles = {}

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
        self._computer.AddInput(value)
        return self._computer.GetHighestOutput()
    
    def GetNextTurn(self):
        return self._computer.GetHighestOutput()

    def GetColorOfCurrentPosition(self):
        if (self._currentPosition not in self._coveredTiles.keys()):
            return 0
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

    def Run(self):
        while(self._computer._state != 0):
            color = self.GetColorToPaintSquare(self.GetColorOfCurrentPosition())
            self.PaintColorOfCurrentPosition(color)
            turn = self.GetNextTurn()
            self.ChangeDirection(turn)
            self.Move()
            print(f"{color}, {turn}")