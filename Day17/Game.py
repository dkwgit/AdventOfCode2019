import pygame
from pygame import surfarray
import numpy as np
from enum import Enum
from TextScreen import TextScreen
import itertools
import random

class BT(Enum): 
    Empty = 0
    Wall = 1
    Block = 2
    Paddle = 3
    Ball = 4
    Up = 5
    Down = 6
    Left = 7
    Right = 8
    Junction = 9
    BadRobot = 10
    GreenEmpty = 11

class Game:

    blockSize = 25
    inputBlockSize = 5  #I coded some of the blocks in 5x5, which have to be exploded to blocksize
    scalingFactor = blockSize//inputBlockSize

    table = {
        BT.Empty:       np.array([
                            [0,0,0,0,0],
                            [0,0,0,0,0],
                            [0,0,0,0,0],
                            [0,0,0,0,0],
                            [0,0,0,0,0]]), #empty
        BT.Wall:        np.array([
                            [1,1,1,1,1],
                            [1,1,1,1,1],
                            [1,1,1,1,1],
                            [1,1,1,1,1],
                            [1,1,1,1,1]]), #wall
        BT.Block:       np.array([
                            [1,0,1,0,1],
                            [0,1,0,1,0],
                            [1,0,1,0,1],
                            [0,1,0,1,0],
                            [1,0,1,0,1]]), #block
        BT.Paddle:      np.array([
                            [0,0,1,1,0],
                            [0,0,1,1,0],
                            [0,0,1,1,0],
                            [0,0,1,1,0],
                            [0,0,1,1,0]]), # horizontal paddle
        BT.Ball:        np.array([
                            [0,0,0,0,0],
                            [0,1,1,1,0],
                            [0,1,1,1,0],
                            [0,1,1,1,0],
                            [0,0,0,0,0]]),
        BT.Right:       np.array([
                            [0,0,1,0,0],
                            [0,1,1,1,0],
                            [0,0,1,0,0],
                            [0,0,1,0,0],
                            [0,0,1,0,0]]),
        BT.Left:        np.array([
                            [0,0,1,0,0],
                            [0,0,1,0,0],
                            [0,0,1,0,0],
                            [0,1,1,1,0],
                            [0,0,1,0,0]]),
        BT.Up:          np.array([
                            [0,0,0,0,0],
                            [0,1,0,0,0],
                            [1,1,1,1,1],
                            [0,1,0,0,0],
                            [0,0,0,0,0]]),
        BT.Down:        np.array([
                            [0,0,0,0,0],
                            [0,0,0,1,0],
                            [1,1,1,1,1],
                            [0,0,0,1,0],
                            [0,0,0,0,0]]),
        BT.Junction:     np.array([
                            [0,0,1,0,0],
                            [0,1,1,1,0],
                            [1,1,1,1,1],
                            [0,1,1,1,0],
                            [0,0,1,0,0]]),
        BT.BadRobot:     np.array([
                            [1,0,0,0,1],
                            [0,1,0,1,0],
                            [0,0,1,0,0],
                            [0,1,0,1,0],
                            [1,0,0,0,1]])
    }

    def SetDirection(self,val):
        self._direction = val
        self._started = True

    def __init__(self,computer):
        self._screen = {}
        self._started = False
        self._screenHeight = 1275
        self._screenWidth = 1275
        self._origin = (self._screenHeight // 2, self._screenWidth // 2)
        self._robot = self._origin
        self._started = False
        self._computer = computer
        self._surface = None
        self._pixels = None
        self._direction = 0
        self._textScreen = TextScreen()
        for k in Game.table.keys():
            if (k in [BT.Up,BT.Down,BT.Left,BT.Right,BT.Ball]):
                r,g,b,a = pygame.colordict.THECOLORS.get('yellow2')
                color = r << 16 | g << 8 | b
            elif( k == BT.BadRobot):
                r,g,b,a = pygame.colordict.THECOLORS.get('indianred3')
                color = r << 16 | g << 8 | b
            elif( k == BT.Junction):
                r,g,b,a = pygame.colordict.THECOLORS.get('cornflowerblue')
                color = r << 16 | g << 8 | b
            else:
                color = 0xFFFFFF
            a = np.zeros((Game.blockSize,Game.blockSize),np.uint32)
            item = Game.table[k]
            for y in range(0,Game.inputBlockSize):
                for x in range(0,Game.inputBlockSize):
                    if item[y][x]== 1:
                        a[
                            y*Game.scalingFactor:y*Game.scalingFactor+Game.scalingFactor,
                            x*Game.scalingFactor:x*Game.scalingFactor+Game.scalingFactor
                        ] = color
            if (k==BT.Up): #Fill in sides of arrow, so it looks smooth
                a[9,1] = a[9,2] = a[9,3] = a[9,4] = a[8,2] = a[8,3] = a[8,4] = a[7,3] = a[7,4] = a[6,4] = color
                a[15,1] = a[15,2] = a[15,3] = a[15,4] = a[16,2] = a[16,3] = a[16,4] = a[17,3] = a[17,4] = a[18,4] = color
            if (k==BT.Down): #Fill in sides of arrow, so it looks smooth
                a[9,23] = a[9,22] = a[9,21] = a[9,20] = a[8,22] = a[8,21] = a[8,20] = a[7,21] = a[7,20] = a[6,20] = color
                a[15,23] = a[15,22] = a[15,21] = a[15,20] = a[16,22] = a[16,21] = a[16,20] = a[17,21] = a[17,20] = a[18,20] = color
            if (k==BT.Right): #Fill in sides of arrow, so it looks smooth
                a[4,6] = a[4,7] = a[4,8] = a[4,9] = a[3,7] = a[3,8] = a[3,9] = a[2,8] = a[2,9] = a[1,9] = color
                a[4,18] = a[4,17] = a[4,16] = a[4,15] = a[3,17] = a[3,16] = a[3,15] = a[2,16] = a[2,15] = a[1,15] = color
            if (k==BT.Left): #Fill in sides of arrow, so it looks smooth
                a[20,6] = a[20,7] = a[20,8] = a[20,9] = a[21,7] = a[21,8] = a[21,9] = a[22,8] = a[22,9] = a[23,9] = color
                a[20,18] = a[20,17] = a[20,16] = a[20,15] = a[21,17] = a[21,16] = a[21,15] = a[22,16] = a[22,15] = a[23,15] = color
            Game.table[BT(k)] = a
        if (BT.GreenEmpty not in Game.table.keys()):
            block = Game.table[BT.Empty].copy()
            block.fill(0x00FF00)
            Game.table[BT.GreenEmpty] = block

        pygame.init()         
        self._surface = pygame.Surface((self._screenWidth,self._screenHeight))
        #we'll us a window that is scaled smaller than the actual game surface, to get everything on a 1080 height screen.
        self._window = pygame.display.set_mode((1000, 1000))
        self._surface.fill((0,0,0))
        self._pixels = surfarray.pixels2d(self._surface)
        #self.UpdateDisplay(-1)  #From Day15, leaving it in for now
    
    def LoadScreenData(self, data):
        for (pos,blockType) in data:
            self.SetBlockTypeToScreen(pos,BT(blockType))
            self._screen[pos] = blockType

    def SaveScreenData(self):
        filepath = 'Maze.txt'
        screenValues = []
        for k in self._screen.keys():
            screenValues.append((k,self._screen[k]))
        print(screenValues, file=open(filepath, 'w'))

    #From day 15, leaving it in for now.
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

    def ChangeBlockType(self, pos, newBlockType):
        self.SetBlockTypeToScreen(pos, newBlockType)

    def ChangeColorOfBlock(self, pos, color):
        block = Game.table[self._screen[pos]]
        for y in range(0,Game.blockSize):
            for x in range(0,Game.blockSize):
                if block[y][x] != 0:
                    block[y][x] = color
        self.SetBlockToScreen(pos, block)

    #From day 15, leaving it in for now.  Can be use for thinkgs like viewwing blocks,
    #for example by sending a -1
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
            #changesd to view blocks on day 17
            y,x = self._robot
            self.SetBlockTypeToScreen(self._robot,BT.Up)
            self.SetBlockTypeToScreen((y+25,x),BT.Down)
            self.SetBlockTypeToScreen((y+50,x),BT.Left)
            self.SetBlockTypeToScreen((y+75,x),BT.Right)
            self.SetBlockTypeToScreen((y+100,x),BT.Junction)
            self.SetBlockTypeToScreen((y+125,x),BT.BadRobot)
            self.SetBlockTypeToScreen((y+150,x),BT.Ball)
        if (result == 0):
            self.SetBlockTypeToScreen((y,x),BT.Wall)
        if (result == 1):
            if (self._origin == self._robot):
                blockType = BT.Paddle
            else:
                blockType = BT.Empty
            self.SetBlockTypeToScreen(self._robot,blockType)
            blockType = BT.Ball
            self.SetBlockTypeToScreen((y,x),blockType)
            self._robot = (y,x)
        if (result == 2):
            self.SetBlockTypeToScreen(self._robot,BT.Empty)
            self.SetBlockTypeToScreen((y,x),BT.Block)
            self._robot = (y,x)

    def SetBlockToScreen(self, pos, block, batchMode = False):
        blockYLength = block.shape[0]
        blockXLength = block.shape[1]
        screenStartY = pos[0] 
        screenEndY = pos[0]  + blockYLength
        screenStartX = pos[1]
        screenEndX = pos[1] + blockXLength
        self._pixels[screenStartX:screenEndX,screenStartY:screenEndY] = block

        if (batchMode == False):
            self.BlitAndSendToWindow()
        
        self.ProcessGameEvents()

    def SetBlockTypeToScreen(self, pos, blockType, batchMode = False):
        self._screen[pos] = blockType
        block = Game.table[blockType]
        self.SetBlockToScreen(pos, block, batchMode)

    def BlitAndSendToWindow(self):
        surfarray.blit_array(self._surface, self._pixels)
        self._window.blit(pygame.transform.scale(self._surface, self._window.get_rect().size), (0, 0))
        pygame.display.update()

    def ProcessOutput(self,result):
        self.UpdateDisplay(result)
        self._direction = 0
        self._started = False

    def DrawTextScreenToGameScreen(self):
        self._textScreen._lines = [x for x in self._textScreen._lines if len(x) > 0]
        maxY = len(self._textScreen._lines)
        maxX = max(map(lambda x : len(x), self._textScreen._lines))

        for y in range(0, maxY):
            line = list(self._textScreen._lines[y])
            for x in range(0,maxX):
                ch = line[x]
                blockType = None
                if (ch == "."):
                    continue
                if (ch == "#"):
                    blockType = BT.Wall
                if (ch == "^"):
                    blockType = BT.Up
                if (ch == ">"):
                    blockType = BT.Right
                if (ch == "<"):
                    blockType = BT.Left
                if (ch == "v"):
                    blockType = BT.Down
                if (ch == "X"):
                    blockType = BT.BadRobot
                self.SetBlockTypeToScreen((y*Game.blockSize,x*Game.blockSize),blockType,True)
        self.BlitAndSendToWindow()

    def SearchForJunctions(self):
        #I used colors to visually show progress while searching the scaffold for junctions. Start walking tiles, marking them with a color.
        #
        #We can think of one color as one worker, walking according to an algorithm
        #
        #At each tile, check for number of adjacents, and record that number in analyzed tiles.  Anything with a number of adjacents > 2 is a junction
        #Walk the adjacents. Continue current color on first one, pick new colors for the other ones.
        #
        #If we encounter no new tiles, that color dead ends.
        #when we encounter no new tiles at all, we've walked the whole structure and can check for tiles that had > 2 ajacents. Those are the junctions.

        #Got this list from http://www.two4u.com/color/medium-txt.html, took out white and black
        colors = [
            0XFF0000,0X00FF00,0X0000FF,0XFF00FF,0X00FFFF,0XFFFF00,0X70DB93,0X5C3317,0X9F5F9F,0XB5A642,0XD9D919,0XA62A2A,0X8C7853,0XA67D3D,0X5F9F9F,
            0XD98719,0XB87333,0XFF7F00,0X42426F,0X5C4033,0X2F4F2F,0X4A766E,0X4F4F2F,0X9932CD,0X871F78,0X6B238E,0X2F4F4F,0X97694F,0X7093DB,0X855E42,0X545454,
            0X856363,0XD19275,0X8E2323,0XF5CCB0,0X238E23,0XCD7F32,0XDBDB70,0XC0C0C0,0X527F76,0X93DB70,0X215E21,0X4E2F2F,0X9F9F5F,0XC0D9D9,0XA8A8A8,0X8F8FBD,
            0XE9C2A6,0X32CD32,0XE47833,0X8E236B,0X32CD99,0X3232CD,0X6B8E23,0XEAEAAE,0X9370DB,0X426F42,0X7F00FF,0X7FFF00,0X70DBDB,0XDB7093,0XA68064,0X2F2F4F,
            0X23238E,0X4D4DFF,0XFF6EC7,0X00009C,0XEBC79E,0XCFB53B,0XFF7F00,0XFF2400,0XDB70DB,0X8FBC8F,0XBC8F8F,0XEAADEA,0XD9D9F3,0X5959AB,0X6F4242,0X8C1717,
            0X238E68,0X6B4226,0X8E6B23,0XE6E8FA,0X3299CC,0X007FFF,0XFF1CAE,0X00FF7F,0X236B8E,0X38B0DE,0XDB9370,0XD8BFD8,0XADEAEA,0X5C4033,0XCDCDCD,0X4F2F4F,
            0XCC3299,0XD8D8BF,0X99CC32
        ]

        analyzedTiles = {}

        scaffoldTiles = { key:value for key,value in self._screen.items() if value == BT.Wall }
        #robot is the starting position.
        robot = [ key for key,value in self._screen.items() if value in [BT.Up, BT.Down, BT.Left, BT.Right]][0]

        def GetAdjacentTiles(pos):
            #Given a tile position, how many other relevant tiles are immediately adjacent.
            y,x = pos
            initial = []
            initial.append((y-Game.blockSize, x))
            initial.append((y+Game.blockSize, x))
            initial.append((y, x-Game.blockSize))
            initial.append((y, x+Game.blockSize))
            return [item for item in initial if item in scaffoldTiles.keys()]

        def AnalyzeTile(tile, color):
            assert(tile not in analyzedTiles.keys())

            self.ChangeColorOfBlock(tile,color)
            adjacents = GetAdjacentTiles(tile)
            analyzedTiles[tile] = len(adjacents) #current tile is now analyzed, we record the number of adjacents

            nextToAnalyze = [x for x in adjacents if x not in analyzedTiles.keys()]
            return (tile, color, nextToAnalyze)

        finished = []  # "workers" that have finished
        workers = {}   # current "workers"

        def DoAnalysis():
            while (True):
                if (len(workers)==0):
                    #No more exploring needed
                    break
                for (color,(count,tile,discard2)) in workers.copy().items():

                    if (tile in analyzedTiles.keys()):
                        #Other workers might have beat us to a candidate tile, if so, this worker is done.
                        worker = workers[color]
                        finished.append(worker)
                        del workers[color]
                        continue

                    discard1, discard2, nextToAnalyze = AnalyzeTile(tile, color)

                    if (len(nextToAnalyze)==0):
                        #This worker is done, having no more candidate tiles to analyze
                        worker = workers[color]
                        finished.append(worker)
                        del workers[color]
                        continue

                    for idx,t in enumerate(nextToAnalyze):
                        if (idx == 0):
                            # keep going with current color, for the first one in the list
                            workers[color] = (count+1,t,color)
                        else:
                            # for each additional one on the list, start a new worker, with a random color
                            newColor = colors.pop(random.randint(0,len(colors)-1))
                            workers[newColor] = (1,t,newColor)
                            
                pygame.time.delay(100)  # helps follow the visualization

        #pick a random color to start with.  The random color picking minimizes likelihood of adjacent colors looking alike,
        #making the visualization easier to track with
        color = colors.pop(random.randint(0,len(colors)-1)) 
        workers[color] = (1,robot,color)
        DoAnalysis()
        
        junctions = [k for k,v in analyzedTiles.items() if v > 2]
        print(f"Junctions found: {len(junctions)}")
        
        #plot the junctions back to the text screen, which we got from the IntComputer (plot from pygame screen back to text screen).
        #this gets coordinates in terms of text screen, for answering Day17-1 calibration question
        junctionsOnTextScreen = []
        for j in junctions:
            self.ChangeBlockType(j, BT.Junction) #show the found junctions
            junctionsOnTextScreen.append(self.TranslateToTextScreen(j))

        calibration = sum(map(lambda pos: pos[0]*pos[1],junctionsOnTextScreen))
        print(f"Calibration number, the answer for Day17-1: {calibration}")  #6680

    def TranslateToTextScreen(self,pos):
        y,x = pos
        return (y//Game.blockSize,x//Game.blockSize)

    def ProcessGameEvents(self):
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
                elif (event.key == pygame.K_u):  #self.UpdateDisplay was left over from Day 15.  I rigged 'u' to it to see some new blocks
                    self.UpdateDisplay(-1)
                elif (event.key == pygame.K_f): #f does the fill with oxygen on the Day 15 maze
                    self.FillWithOxygen()
                elif (event.key == pygame.K_SPACE): #starts the current Computer program (displays the scaffold, etc.)
                    self._started = True if self._started == False else False
            
            if event.type == pygame.QUIT: 
                pygame.quit() 
                quit() 

    def MainLoop(self):
        while(True):
            pygame.display.update()

            self.ProcessGameEvents()
  
            if (self._started):
                # Run the computer code up to next output result, accumulating results in the text screen
                result = None
                (result,continueRun,inputNext) = self._computer.RunToNextIO()
                if (result is not None):
                    self._textScreen.AddToLine(result)

                nextOpCode = self._computer.PeekAtOpCodeValue()
                if (nextOpCode == 99):
                    self._started = False
                    self._computer.DoNext()
                    
                    #after we are done accumulating results onto the text screen, draw it to the game screen
                    self.DrawTextScreenToGameScreen()
                    #do the visualized search for junctions
                    self.SearchForJunctions()
            
            
