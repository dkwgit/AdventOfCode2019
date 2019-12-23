import threading
import pygame
from pygame import surfarray
import numpy as np
import itertools

class Game:

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
                    [0,0,0,1,1],
                    [0,0,0,1,1],
                    [0,0,0,1,1],
                    [0,0,0,1,1],
                    [0,0,0,1,1]]), # horizontal paddle
        '4': np.array([
                    [0,0,0,0,0],
                    [0,1,1,1,0],
                    [0,1,1,1,0],
                    [0,1,1,1,0],
                    [0,0,0,0,0]])
    }
    
    def __init__(self,minBlockTuple,maxBlockTuple):
        self._minBlockX = minBlockTuple[0]
        self._minBlockY = minBlockTuple[1]
        self._maxBlockX = maxBlockTuple[0]
        self._maxBlockY = maxBlockTuple[1]
        self._screenHeight = (self._maxBlockY + 1) * 15
        self._screenWidth = (self._maxBlockX + 1) * 15
        self._white = (255, 255, 255) 
        self._green = (0, 255, 0) 
        self._blue = (0, 0, 128) 
        self._black = (0, 0, 0)
        self._font = None
        self._thread = None
        self._surface = None
        self._pixels = None
        for k in Game.table.keys():
            a = np.zeros((15,15),np.uint32)
            item = Game.table[k]
            for y in range(0,5):
                for x in range(0,5):
                    if item[y][x]== 1:
                        a[y*3:y*3+3,x*3:x*3+3] = 0XFFFFFF
            Game.table[k] = a

        pygame.init()         
        self._surface = pygame.display.set_mode((self._screenWidth, self._screenHeight))
        self._surface.fill(self._black)
        self._pixels = surfarray.pixels2d(self._surface)
        pygame.display.set_caption('Show Text') 

        self._thread = threading.Thread( target=self.MainLoop, args=("pygame Thread",) )

    def UpdateDisplay(self,data):
        val = iter(data)
        for x,y,item in zip(val,val,val):
            self.SetBlockToScreen(x,y,item)
        
        surfarray.blit_array(self._surface, self._pixels)
        if (not self._thread.is_alive()):
            self._thread.start()

    def SetBlockToScreen(self, x, y, blockType):
        block = Game.table[str(blockType)]
        blockYLength = block.shape[0]
        blockXLength = block.shape[1]
        screenStartY = y * blockYLength
        screenEndY = y * blockYLength + blockYLength
        screenStartX = x * blockXLength
        screenEndX = x * blockXLength + blockXLength
        self._pixels[screenStartX:screenEndX,screenStartY:screenEndY] = block

    def MainLoop(self, name):
        while(True):
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    pygame.quit() 
                    quit() 
  
            pygame.display.update()