import threading
import pygame
import numpy as np
import itertools

class Game:

    table = {
        0: np.array([
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]), #empty
        1: np.array([
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1],
                    [1,1,1,1,1]]), #wall
        2: np.array([
                    [1,0,1,0,1],
                    [0,1,0,1,0],
                    [1,0,1,0,1],
                    [0,1,0,1,0],
                    [1,0,1,0,1]]), #block
        3: np.array([
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,1,1,1,1],
                    [1,1,1,1,1]]), # horizontal paddle
        4: np.array([
                    [0,0,0,0,0],
                    [0,1,1,1,0],
                    [0,1,1,1,0],
                    [0,1,1,1,0],
                    [0,0,0,0,0]])
    }
    
    def __init__(self,minMaxText):
        self._minxMaxText = minMaxText
        self._screenHeight = 750
        self._screenWidth = 750
        self._white = (255, 255, 255) 
        self._green = (0, 255, 0) 
        self._blue = (0, 0, 128) 
        self._black = (0, 0, 0)
        self._font = None
        self._thread = None
        self._surface = None
        self._pixelArray = None
        for k in Game.table.keys():
            a = np.zeros((15,15))
            for item in Game.table[k]:
                for y in range(5):
                    for x in range(5):
                        if a[y,x] == 1:
                            a[y,x] = a[y,x+1] = a[y,x+2] = a[y+1,x] = a[y+1,x+1] = a[y+1,x+2] = a[y+2,x] = a[y+2,x+1] = a[y+2,x+2] = 0xFFFFFF
            Game.table[k] = a


        pygame.init()         
        self._surface = pygame.display.set_mode((self._screenWidth, self._screenHeight))
        self._surface.fill(self._black)
        self._pixelArray = pygame.PixelArray(self._surface)
        pygame.display.set_caption('Show Text') 

        self._thread = threading.Thread( target=self.MainLoop() )

    def UpdateDisplay(self,data):
        data
        if (not self._thread.is_alive()):
            self._thread.start()
        #val = iter(data)
        #for x,y,item in zip(val,val,val):



    def MainLoop(self):
        while(True):
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    pygame.quit() 
                    quit() 
  
            pygame.display.update()