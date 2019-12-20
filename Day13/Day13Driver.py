import os
import sys
import pygame
sys.path.append(os.path.abspath('../IntCodeComputer'))

import itertools
from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture

class Day13Driver:

    table = {
        0: '\u0020', #empty
        1: '\u2588', #wall
        2: '\u2592', #block
        3: '\u2582', #horizontal paddle
        4: '\u006A'  #ball
    }
    def __init__(self):
        self._output = []
        self._triplets = []


    def Run(self):
        c = Computer()
        c.LoadProgram(DataFixture.mainDay13)
        continueRun = True
        while (continueRun):
            result,continueRun = c.RunToNextOutput()
            if (result is not None):
                self._output.append(result)
        val = iter(self._output)
        blockCount = 0
        for x,y,char in zip(val,val,val):
            if (char == 2):
                blockCount = blockCount + 1
            self._triplets.append(((x,y),Day13Driver.table[char]))
        print(f"Block count {blockCount}")
        minX = min(self._triplets, key = lambda x: x[0][0])[0][0]
        minY = min(self._triplets, key = lambda x: x[0][1])[0][1]
        maxX = max(self._triplets, key = lambda x: x[0][0])[0][0]
        maxY = max(self._triplets, key = lambda x: x[0][1])[0][1]
        lines = []
        index = 0
        for row in range(maxY+1):
            line = ''
            for col in range(maxX+1):
                ((x,y),char) = self._triplets[index]
                assert(x==col)
                assert(y==row)
                line = line + char + '\n'
                index = index + 1
            line = line + '\n'
            lines.append(line)
         
        pygame.init()         
        white = (255, 255, 255) 
        green = (0, 255, 0) 
        blue = (0, 0, 128) 
        black = (0, 0, 0)
        
        # assigning values to X and Y variable 
        X = 600
        Y = 600
        
        # create the display surface object 
        # of specific dimension..e(X, Y). 
        display_surface = pygame.display.set_mode((X, Y )) 
        
        # set the pygame window name 
        pygame.display.set_caption('Show Text') 
        
        # create a font object. 
        # 1st parameter is the font file 
        # which is present in pygame. 
        # 2nd parameter is size of the font 
        font = pygame.font.Font('freesansbold.ttf', 16) 
        
         
        textHeight = None
        # infinite loop 
        while True : 
    
            
            writeLocationY = 0
            for line in range(maxY):  
                # create a text suface object, 
                # on which text is drawn on it. 
                text = font.render(lines[line], True, black, white)
                textRect = text.get_rect()  
                if (textHeight is None):
                    textHeight = (textRect[3]+1/2)
                textRect.center = (X // 2,  (writeLocationY + (textHeight// 2)))
                writeLocationY = writeLocationY + textHeight
          

            # completely fill the surface object 
            # with white color 
            display_surface.fill(black) 
        
            # copying the text surface object 
            # to the display surface object  
            # at the center coordinate. 
            display_surface.blit(text, textRect) 

            # iterate over the list of Event objects 
            # that was returned by pygame.event.get() method. 
            for event in pygame.event.get() : 
        
                # if event object type is QUIT 
                # then quitting the pygame 
                # and program both. 
                if event.type == pygame.QUIT : 
        
                    # deactivates the pygame library 
                    pygame.quit() 
        
                    # quit the program. 
                    quit() 
        
                # Draws the surface object to the screen.   
                pygame.display.update()  

d = Day13Driver()
d.Run()