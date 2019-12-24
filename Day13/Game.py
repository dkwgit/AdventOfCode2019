import pygame
from pygame import surfarray
import numpy as np
import itertools

class Game:

    blockSize = 25
    inputBlockSize = 5  #I coded the inputs in 5x5, which have to be exploded to blocksize
    scalingFactor = blockSize//inputBlockSize

    table = {
        '0': np.array([
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]), #empty
        '1': np.array([
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1]]), #wall
        '2': np.array([
                    [1,0,1,0,1],
                    [0,1,0,1,0],
                    [1,0,1,0,1],
                    [0,1,0,1,0],
                    [1,0,1,0,1]]), #block
        '3': np.array([
                    [0,1,1,1,0],
                    [0,1,1,1,0],
                    [0,1,1,1,0],
                    [0,1,1,1,0],
                    [0,1,1,1,0]]), # horizontal paddle
        '4': np.array([
                    [0,0,0,0,0],
                    [0,1,1,1,0],
                    [0,1,1,1,0],
                    [0,1,1,1,0],
                    [0,0,0,0,0]]) # ball
    }


    
    def SetJoyStick(self,val):
        self._joyStick = val

    def GetJoyStick(self):
        val = self._joyStick
        return val

    def __init__(self,computer,minBlockTuple,maxBlockTuple, startData):
        self._positions = {}
        self._started = False
        self._computerOutput = []
        self._scores = []
        self._computer = computer
        self._joyStick = 0
        self._minBlockX = minBlockTuple[0]
        self._minBlockY = minBlockTuple[1]
        self._maxBlockX = maxBlockTuple[0]
        self._maxBlockY = maxBlockTuple[1]
        self._screenHeight = (self._maxBlockY + 1) * Game.blockSize
        self._screenWidth = (self._maxBlockX + 1) * Game.blockSize
        self._font = None
        self._surface = None
        self._pixels = None
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
        self._surface.fill((0,0,0)) #black
        self._pixels = surfarray.pixels2d(self._surface)
        pygame.display.set_caption('Score: 0') 
        self.UpdateDisplay(startData)

    def UpdateDisplay(self,data):
        val = iter(data)
        for x,y,item in zip(val,val,val):
            if (x==-1 and y==0):
                 if (self._started == True):
                     print(f"Score will be set to {item}")
                     if (item > 0):
                         self._scores.append(item)
                 pygame.display.set_caption('Score: ' + str(item)) 
            else:
                if (self._started == True):
                    if (item == 0 and (x,y) in self._positions.keys() and self._positions[(x,y)] == 2):
                        print(f"Block at {x},{y} erased.")
                    if (item == 4):
                        print(f"Ball moves to {x},{y}")
                    self._positions[(x,y)] = item
                else:
                    self._positions[(x,y)] = item
                self.SetBlockToScreen(x,y,item)
        
        surfarray.blit_array(self._surface, self._pixels)

    def SetBlockToScreen(self, x, y, blockType):
        block = Game.table[str(blockType)]
        blockYLength = block.shape[0]
        blockXLength = block.shape[1]
        screenStartY = y * blockYLength
        screenEndY = y * blockYLength + blockYLength
        screenStartX = x * blockXLength
        screenEndX = x * blockXLength + blockXLength
        self._pixels[screenStartX:screenEndX,screenStartY:screenEndY] = block

    def ProcessUpToNextInput(self):
        continueRun = True
        inputEvent = False

        while (continueRun and inputEvent == False) and self._computer.PeekAtOpCodeValue() != 99:
            result,continueRun,inputEvent = self._computer.RunToNextIO()
            if (result is not None):
                self._computerOutput.append(result)
                
        while(len(self._computerOutput)>=3):
            assert(len(self._computerOutput)%3==0)
            data = self._computerOutput.copy()
            self._computerOutput = []
            self.UpdateDisplay(data)

    def MainLoop(self):
        while(True):
            pygame.display.update()

            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT):
                        self.SetJoyStick(-1)
                    elif (event.key == pygame.K_RIGHT):
                         self.SetJoyStick(1)
                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_LEFT):
                        self.SetJoyStick(0)
                    elif (event.key == pygame.K_RIGHT):
                         self.SetJoyStick(0)
                    elif (event.key == pygame.K_SPACE):
                        self._started = True if self._started == False else False
                
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    quit() 
  
            if (self._started):
                nextOpCode = self._computer.PeekAtOpCodeValue()

                while(nextOpCode == 3):
                    self._computer.SetInput([self.GetJoyStick()])
                    self._computer.DoNext()
                    nextOpCode = self._computer.PeekAtOpCodeValue()

                if (nextOpCode != 3 and nextOpCode != 99):
                    self.ProcessUpToNextInput()
                    nextOpCode = self._computer.PeekAtOpCodeValue()

                if (nextOpCode == 99):
                    self._computer.DoNext()
                    print("Game over")
                    print(f"Score series {self._scores}")
                    pygame.quit() 
                    quit() 
            
            pygame.time.wait(1000)
            
            
