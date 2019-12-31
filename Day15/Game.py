import pygame
from pygame import surfarray
import numpy as np
from enum import Enum

class BT(Enum): 
    Empty = 0
    Wall = 1
    Block = 2
    Paddle = 3
    Ball = 4
    GreenEmpty = 5

class Game:

    blockSize = 16
    inputBlockSize = 4  #I coded the inputs in 5x5, which have to be exploded to blocksize
    scalingFactor = blockSize//inputBlockSize

    table = {
        BT.Empty:       np.array([
                            [0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0],
                            [0,0,0,0]]), #empty
        BT.Wall:        np.array([
                            [1,1,1,1],
                            [1,1,1,1],
                            [1,1,1,1],
                            [1,1,1,1]]), #wall
        BT.Block:       np.array([
                            [0,1,0,1],
                            [1,0,1,0],
                            [0,1,0,1],
                            [1,0,1,0]]), #block
        BT.Paddle:      np.array([
                            [0,1,1,0],
                            [0,1,1,0],
                            [0,1,1,0],
                            [0,1,1,0]]), # horizontal paddle
        BT.Ball:        np.array([
                            [0,0,0,0],
                            [0,1,1,0],
                            [0,1,1,0],
                            [0,0,0,0]]) # ball
    }

    def SetDirection(self,val):
        self._direction = val
        self._started = True

    def __init__(self,computer):
        self._screen = {}
        self._started = False
        self._screenHeight = 1000
        self._screenWidth = 1000
        self._origin = (self._screenHeight // 2, self._screenWidth // 2)
        self._robot = self._origin
        self._started = False
        self._computer = computer
        self._surface = None
        self._pixels = None
        self._direction = 0
        for k in Game.table.keys():
            a = np.zeros((Game.blockSize,Game.blockSize),np.uint32)
            item = Game.table[k]
            for y in range(0,Game.inputBlockSize):
                for x in range(0,Game.inputBlockSize):
                    if item[y][x]== 1:
                        a[
                            y*Game.scalingFactor:y*Game.scalingFactor+Game.scalingFactor,
                            x*Game.scalingFactor:x*Game.scalingFactor+Game.scalingFactor
                        ] = 0XFFFFFF
            Game.table[BT(k)] = a
        if (BT.GreenEmpty not in Game.table.keys()):
            block = Game.table[BT.Empty].copy()
            block.fill(0x00FF00)
            Game.table[BT.GreenEmpty] = block

        pygame.init()         
        self._surface = pygame.display.set_mode((self._screenWidth, self._screenHeight))
        self._surface.fill((128,128,128)) #black
        self._pixels = surfarray.pixels2d(self._surface)
        self.UpdateDisplay(-1)
    
    def LoadScreenData(self, data):
        for (pos,blockType) in data:
            self.SetBlockToScreen(pos,BT(blockType))
            self._screen[pos] = blockType

    def SaveScreenData(self):
        filepath = 'Maze.txt'
        screenValues = []
        for k in self._screen.keys():
            screenValues.append((k,self._screen[k]))
        print(screenValues, file=open(filepath, 'w'))

    def FillWithOxygen(self):
        openSpace = {k:v for (k,v) in self._screen.items() if v == 0 or v ==2 or v == 3}
        fillFrom = [k for (k,v) in self._screen.items() if v ==2]

        def GetBoxToCheck(pos):
            box = []
            y = pos[0] - Game.blockSize
            x = pos[1]
            box.append((y,x))
        
            y = pos[0] + Game.blockSize
            x = pos[1]
            box.append((y,x))
        
            y = pos[0]
            x = pos[1] - Game.blockSize
            box.append((y,x))

            y = pos[0]
            x = pos[1] + Game.blockSize
            box.append((y,x))
            return box

        def Fill(game, pointsToFillFrom, minute):
            nextPointsToFillFrom = []
            for point in pointsToFillFrom:
                del openSpace[point]
                box = GetBoxToCheck(point)
                for pos in box:
                    if (pos in openSpace.keys()):
                        game.ChangeColorOfBlock(pos)
                        if (pos == self._origin):
                            print(f"Path to origin took {minute + 1} minutes")
                        nextPointsToFillFrom.append(pos)

            if (len(openSpace.keys()) > 0):
                Fill(self, nextPointsToFillFrom, minute + 1)
            else:
                print(f"Filled whole space at minute {minute}")
            return
        
        Fill(self,fillFrom,0)

    def ChangeColorOfBlock(self, pos):

        self.SetBlockToScreen(pos,BT.GreenEmpty)
        pygame.display.update()

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                quit() 
        pygame.time.wait(10)


    def UpdateDisplay(self,result):
        if (self._direction == 1):
            y = self._robot[0] - Game.blockSize
            x = self._robot[1]
        elif (self._direction == 2):
            y = self._robot[0] + Game.blockSize
            x = self._robot[1]
        elif (self._direction == 3):
            y = self._robot[0]
            x = self._robot[1] - Game.blockSize
        elif (self._direction == 4):
            y = self._robot[0]
            x = self._robot[1] + Game.blockSize


        if (result == -1):
            self.SetBlockToScreen(self._robot,BT.Paddle)
        if (result == 0):
            self.SetBlockToScreen((y,x),BT.Wall)
        if (result == 1):
            if (self._origin == self._robot):
                blockType = BT.Paddle
            else:
                blockType = BT.Empty
            self.SetBlockToScreen(self._robot,blockType)
            blockType = BT.Ball
            self.SetBlockToScreen((y,x),blockType)
            self._robot = (y,x)
        if (result == 2):
            self.SetBlockToScreen(self._robot,BT.Empty)
            self.SetBlockToScreen((y,x),BT.Block)
            self._robot = (y,x)

        surfarray.blit_array(self._surface, self._pixels)


    def SetBlockToScreen(self, pos, blockType):

        if (blockType != BT.Ball and (pos not in self._screen.keys())):
            self._screen[pos] = blockType
        if (blockType == BT.Ball and (pos not in self._screen.keys())):
            self._screen[pos] = BT.Empty

        block = Game.table[blockType]
        blockYLength = block.shape[0]
        blockXLength = block.shape[1]
        screenStartY = pos[0] 
        screenEndY = pos[0]  + blockYLength
        screenStartX = pos[1]
        screenEndX = pos[1] + blockXLength
        self._pixels[screenStartX:screenEndX,screenStartY:screenEndY] = block

    def ProcessOutput(self,result):
        self.UpdateDisplay(result)
        self._direction = 0
        self._started = False

    def MainLoop(self):
        while(True):
            pygame.display.update()

            for event in pygame.event.get(): 
                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_LEFT):
                        self.SetDirection(3)
                    elif (event.key == pygame.K_RIGHT):
                         self.SetDirection(4)
                    if (event.key == pygame.K_UP):
                        self.SetDirection(1)
                    elif (event.key == pygame.K_DOWN):
                         self.SetDirection(2)
                    elif (event.key == pygame.K_f):
                         self.FillWithOxygen()
                    elif (event.key == pygame.K_SPACE):
                        self._started = True if self._started == False else False
                
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    quit() 
  
            if (self._started):
                nextOpCode = self._computer.PeekAtOpCodeValue()

                result = None
                if(nextOpCode == 3):
                    self._computer.SetInput([self._direction])
                    self._computer.DoNext()
                    (result,continueRun,inputNext) = self._computer.RunToNextIO()
                    if (result is not None):
                        self.ProcessOutput(result)
                    (result,continueRun,inputNext) = self._computer.RunToNextIO()
                    nextOpCode = self._computer.PeekAtOpCodeValue()
                    assert(nextOpCode == 3 or nextOpCode == 99)
                    if (nextOpCode == 99):
                        self._computer.DoNext()
                        pygame.quit() 
                        quit() 
            
            
