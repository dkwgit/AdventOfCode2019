import pygame
from pygame import surfarray
import numpy as np

class Game:

    blockSize = 16
    inputBlockSize = 4  #I coded the inputs in 5x5, which have to be exploded to blocksize
    scalingFactor = blockSize//inputBlockSize

    table = {
        '0': np.array([
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]), #empty
        '1': np.array([
                    [1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1]]), #wall
        '2': np.array([
                    [0,1,0,1],
                    [1,0,1,0],
                    [0,1,0,1],
                    [1,0,1,0]]), #block
        '3': np.array([
                    [0,1,1,0],
                    [0,1,1,0],
                    [0,1,1,0],
                    [0,1,1,0]]), # horizontal paddle
        '4': np.array([
                    [0,0,0,0],
                    [0,1,1,0],
                    [0,1,1,0],
                    [0,0,0,0]]) # ball
    }

    def SetDirection(self,val):
        self._direction = val
        self._started = True

    def __init__(self,computer):
        self._maze = {}
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
            Game.table[k] = a

        pygame.init()         
        self._surface = pygame.display.set_mode((self._screenWidth, self._screenHeight))
        self._surface.fill((128,128,128)) #black
        self._pixels = surfarray.pixels2d(self._surface)
        self.UpdateDisplay(-1)

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
            blockType = 3
            self.SetBlockToScreen(self._robot,blockType)
        if (result == 0):
            blockType = 1
            self.SetBlockToScreen((y,x),blockType)
        if (result == 1):
            if (self._origin == self._robot):
                blockType = 3
            else:
                blockType = 0
            self.SetBlockToScreen(self._robot,blockType)
            blockType = 4
            self.SetBlockToScreen((y,x),blockType)
            self._robot = (y,x)
        if (result == 2):
            blockType = 0
            self.SetBlockToScreen(self._robot,blockType)
            blockType = 2
            self.SetBlockToScreen((y,x),blockType)
            self._robot = (y,x)

        surfarray.blit_array(self._surface, self._pixels)


    def SetBlockToScreen(self, pos, blockType):

        if (blockType != 4 and (pos not in self._maze.keys())):
            self._maze[pos] = blockType
        if (blockType == 4 and (pos not in self._maze.keys())):
            self._maze[pos] = 0

        block = Game.table[str(blockType)]
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
            
            
