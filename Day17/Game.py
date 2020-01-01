import pygame
from pygame import surfarray
import numpy as np
from enum import Enum
from TextScreen import TextScreen
import itertools
import random
import sys
import os
sys.path.append(os.path.abspath('../IntCodeComputer'))
from Computer import Computer as Computer

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

    rightTurns = { BT.Up: BT.Right, BT.Right: BT.Down, BT.Down: BT.Left, BT.Left: BT.Up } 
    leftTurns =  { BT.Up: BT.Left, BT.Left: BT.Down, BT.Down: BT.Right, BT.Right: BT.Up }

    textScreenToGameScreen = { ".": BT.Empty, "#": BT.Wall, "^": BT.Up, ">": BT.Right, "<": BT.Left, "v": BT.Down, "X": BT.BadRobot, "O": BT.Junction }

    directionsForBlockType = { BT.Up: (-1,0), BT.Down: (1,0), BT.Left: (0,-1), BT.Right: (0,1) }

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
        BT.Left:       np.array([
                            [0,0,1,0,0],
                            [0,1,1,1,0],
                            [0,0,1,0,0],
                            [0,0,1,0,0],
                            [0,0,1,0,0]]),
        BT.Right:        np.array([
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
        self._textScreenDraw = 0

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
            if (k==BT.Left): #Fill in sides of arrow, so it looks smooth
                a[4,6] = a[4,7] = a[4,8] = a[4,9] = a[3,7] = a[3,8] = a[3,9] = a[2,8] = a[2,9] = a[1,9] = color
                a[4,18] = a[4,17] = a[4,16] = a[4,15] = a[3,17] = a[3,16] = a[3,15] = a[2,16] = a[2,15] = a[1,15] = color
            if (k==BT.Right): #Fill in sides of arrow, so it looks smooth
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

    def ChangeBlockType(self, pos, newBlockType, batchMode = False):
        currentBlock = None if pos not in self._screen.keys() else self._screen[pos]
        self.SetBlockTypeToScreen(pos, newBlockType, batchMode = False)
        return currentBlock

    def ChangeColorOfBlock(self, pos, color, batchMode = False):
        block = Game.table[self._screen[pos]].copy()
        for y in range(0,Game.blockSize):
            for x in range(0,Game.blockSize):
                if block[y][x] != 0:
                    block[y][x] = color
        self.SetBlockToScreen(pos, block, batchMode)
        return pos

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
        #if (pos in self._screen.keys() and self._screen[pos]==blockType):
        #    return
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
                blockType = Game.textScreenToGameScreen[ch]
                if (blockType == BT.Empty):
                    continue
                self.SetBlockTypeToScreen((y*Game.blockSize,x*Game.blockSize),blockType,True)
        self.BlitAndSendToWindow()

    def GetAdjacentBlocks(self, pos):
        #Given a block position, what are adjacent N,S,W,E blocks?
        y,x = pos
        adjacents = []
        adjacents.append((y-Game.blockSize, x))
        adjacents.append((y+Game.blockSize, x))
        adjacents.append((y, x-Game.blockSize))
        adjacents.append((y, x+Game.blockSize))
        return adjacents

    def FindRobotBlock(self):
        robotBlocks = [ (key,value) for key,value in self._screen.items() if value in [BT.Up, BT.Down, BT.Left, BT.Right, BT.BadRobot]]
        #should only be in one place, having one of the block value
        assert(len(robotBlocks)==1)
        return robotBlocks[0]

    def GetBlocksOfType(self, blockTypeList):
        return { key:value for key,value in self._screen.items() if value in blockTypeList }

    def GetAdjacentTilesWithFilter(self,pos,filterDict):
        #Given a tile position, how many other relevant tiles are immediately adjacent.
        adjacents = self.GetAdjacentBlocks(pos)
        return [item for item in adjacents if item in filterDict.keys()]

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

        scaffoldTiles = self.GetBlocksOfType([BT.Wall])
        robotPos,robotBlockType = self.FindRobotBlock()

        def AnalyzeTile(tile, color):
            assert(tile not in analyzedTiles.keys())

            if (self._screen[tile]==BT.Wall):
                self.ChangeColorOfBlock(tile,color)
            adjacents = self.GetAdjacentTilesWithFilter(tile,scaffoldTiles)
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
                            
                #pygame.time.delay(25)  # helps follow the visualization

        #pick a random color to start with.  The random color picking minimizes likelihood of adjacent colors looking alike,
        #making the visualization easier to track with
        color = colors.pop(random.randint(0,len(colors)-1)) 
        workers[color] = (1,robotPos,color)
        DoAnalysis()
        
        junctions = [k for k,v in analyzedTiles.items() if v > 2]
        print(f"Junctions found: {len(junctions)}")
        
        #plot the junctions back to the text screen, which we got from the IntComputer (plot from pygame screen back to text screen).
        #this gets coordinates in terms of text screen, for answering Day17-1 calibration question
        junctionsOnTextScreen = []
        for j in junctions:
            self.ChangeBlockType(j, BT.Junction) #show the found junctions
            junctionsOnTextScreen.append(self.TranslateToTextScreen(j))

        for yText,xText in junctionsOnTextScreen:
            oldItem = self._textScreen.SetPoint(yText,xText,"O")
            assert(oldItem == "#")

        calibration = sum(map(lambda pos: pos[0]*pos[1],junctionsOnTextScreen))
        print(f"Calibration number, the answer for Day17-1: {calibration}")  #6680

    def ResetWallsWhite(self):
        discard = [ self.ChangeColorOfBlock(k, 0xFFFFFF,True) for k,v in self.GetBlocksOfType([BT.Wall]).items() ]
        self.BlitAndSendToWindow()

    def MakeScreenEmpty(self):
        for key in self._screen.copy().keys():
            self.ChangeColorOfBlock(key,0x000000,True)
            del self._screen[key]
        self.BlitAndSendToWindow()

    def WalkScaffold(self):
        
        self.SearchForJunctions()
        self.ResetWallsWhite()

        scaffoldTiles = self.GetBlocksOfType([BT.Wall,BT.Junction])
        junctionTiles = self.GetBlocksOfType([BT.Junction])
        walkedHistory = []
        walked = {}

        def GetNextInDirectionByBlockType(blockType):
            assert(blockType in [BT.Up,BT.Down,BT.Left,BT.Right])
            nextStep = Game.directionsForBlockType[blockType]
            return (nextStep,blockType)

        def TakeStep(robotPos, blockType, moveString):
            walkedHistory.append(robotPos)
            if (robotPos not in walked.keys()):
                walked[robotPos] = 0
            walked[robotPos] = walked[robotPos] + 1
            returnValue = None
            adjacents = self.GetAdjacentTilesWithFilter(robotPos, scaffoldTiles)
            adjacents = [a for a in adjacents if ((a not in walked.keys()) or (a in junctionTiles.keys()))]
            if (len(adjacents) == 0):
                return (robotPos,blockType,moveString)
            nextStep,nextBlockType = GetNextInDirectionByBlockType(blockType)
            lengthY,lengthX = nextStep
            stepBlock = (robotPos[0] + lengthY * Game.blockSize, robotPos[1] + lengthX * Game.blockSize)
            if (stepBlock not in adjacents):
                assert(len(adjacents) == 1) #having looked at the scaffold, I don't see intersections at corners
                a = adjacents[0]
                stepBlock = a
                y,x = robotPos
                sy,sx = stepBlock
                turnBlockType = None
                if (sy < y):
                    turnBlockType = BT.Up
                    assert(blockType != BT.Down)
                    moveString = "R," if blockType == BT.Left else "L,"
                if (sy > y):
                    turnBlockType = BT.Down
                    assert(blockType != BT.Up)
                    moveString = "L," if blockType == BT.Left else "R,"
                if (sx < x):
                    turnBlockType = BT.Left
                    assert(blockType != BT.Right)
                    moveString = "L," if blockType == BT.Up else "R,"
                if (sx > x):
                    turnBlockType = BT.Right
                    assert(blockType != BT.Left)
                    moveString = "R," if blockType == BT.Up else "L,"
                assert(turnBlockType is not None)
                assert(moveString != "")
                nextBlockType = turnBlockType
                moveString = moveString + "1"
                returnValue = (stepBlock,nextBlockType,moveString)
            else:
                headString, tailString = moveString[0:-1], moveString[-1]
                stepCountInDirection = str(int(tailString) + 1)
                moveString = headString + stepCountInDirection
                returnValue = (stepBlock,blockType,moveString)
            return returnValue

        moveString = ""
        
        robotPos, nextBlockType = self.FindRobotBlock()
        assert(nextBlockType in [BT.Up,BT.Down,BT.Left,BT.Right])
        returnValues = []
        nextPos = robotPos
        while(True):
            if (nextPos not in junctionTiles.keys()):
                self.ChangeBlockType(nextPos,BT.GreenEmpty)
            else:
                self.ChangeBlockType(nextPos,BT.Junction)
            returnValue = TakeStep(nextPos, nextBlockType, moveString)
            proposedNextPos,nextBlockType,moveString = returnValue
            if (proposedNextPos == nextPos):
                #No more new places to go
                self.ChangeBlockType(nextPos,nextBlockType)
                break
            nextPos = proposedNextPos
            returnValues.append(returnValue)
            self.ChangeBlockType(nextPos,nextBlockType)
            #pygame.time.delay(25)

        def ConsolidateJourneyList(returnValues):
            outputList = []
            currentLetter = returnValues[0][2][0]
            currentNumber = int(returnValues[0][2][2:])
            currentItemInDirection = returnValues[0][2]
            for discard1,discard2,moveString in returnValues:
                newLetter = moveString[0]
                newNumber = int(moveString[2:])
                assert(newNumber != None)
                if (newLetter != currentLetter or newNumber < currentNumber):
                    outputList.append(currentItemInDirection)
                currentLetter = newLetter
                currentNumber = newNumber
                currentItemInDirection = moveString
            outputList.append(currentItemInDirection)
            return outputList

        journeyList = ConsolidateJourneyList(returnValues)
        journeyString = ",".join(journeyList)

        #Writing out the journeystring on paper, 'L8,R10,L8,R8,L12,R8,L8,R10,L8,R8,L8,R10,L8,R10,L8,R10,L8,R8,L12,R8,L8,R10,L12,R8,L12,R8'
        #yieled the following sub-patterns,which when combined in ALL, equal the journeystring.
        A = "L,8,R,10,L,8,R,8"
        B = "L,12,R,8,R,8"
        C = "L,8,R,6,R,6,R,10,L,8"
        ALL = "A,B,A,C,C,A,B,C,B,B"
        ALLCheck = "{},{},{},{},{},{},{},{},{},{}".format(A,B,A,C,C,A,B,C,B,B)
        assert(journeyString==ALLCheck)

        print(f"Scaffold has been walked")

        def WalkAll(steps):
            robotPos,robotBlock = self.FindRobotBlock()
            wallsAndJunctions = { k:v for k,v in self._screen.items() if v == BT.Wall or v == BT.Junction }

            def TurnRobot(turn,robotBlock):
                assert(robotBlock in [BT.Up,BT.Down,BT.Left,BT.Right])
                assert(turn == "R" or turn == "L")
                turnDict = Game.leftTurns if turn == "L" else Game.rightTurns
                return turnDict[robotBlock]
            priorBlockType = BT.Wall
            for turn,distance in steps:
                print(f"Doing step {turn},{distance}")
                robotBlock = TurnRobot(turn,robotBlock)
                self.ChangeBlockType(robotPos, robotBlock)
                pygame.time.delay(10)   
                for d in range(0,int(distance)):
                    self.ChangeBlockType(robotPos, priorBlockType)
                    pygame.time.delay(10)
                    robotY, robotX = robotPos
                    directionY, directionX = Game.directionsForBlockType[robotBlock]
                    robotPos = (robotY + directionY * Game.blockSize, robotX + directionX * Game.blockSize)
                    if (robotPos not in wallsAndJunctions.keys()):
                        robotBlock = BT.BadRobot
                    priorBlockType = self.ChangeBlockType(robotPos, robotBlock)
                    pygame.time.delay(10)
            return

        #Check the result, by walking it
        self.MakeScreenEmpty()
        self.DrawTextScreenToGameScreen()
        steps = ALLCheck.split(',')
        val = iter(steps)
        stepsAsTuples = [ (turn,move) for turn,move in zip(val,val) ]
        WalkAll(stepsAsTuples)

    def TranslateToTextScreen(self,pos):
        y,x = pos
        yText = y // Game.blockSize
        xText = x // Game.blockSize
        return (yText,xText)

    def RestartComputer(self):
        computer = Computer()
        computer.LoadProgram(self._computer.GetOriginalProgram())
        self._computer = computer


    def DoFinalRobotRun(self):
        A = "L,8,R,10,L,8,R,8"
        B = "L,12,R,8,R,8"
        C = "L,8,R,6,R,6,R,10,L,8"
        ALL = "A,B,A,C,C,A,B,C,B,B"

        self._computer._programData[0]=2

        input = [
            ALL,
            A,
            B,
            C,
            'n'
        ]

        def TranslateToAscii(inputList):
            outputInAscii = []
            for i in input:
                asList = list(i)
                for x in asList:
                    outputInAscii.append(ord(x))
                outputInAscii.append(10)
            return outputInAscii

        inputForComputer = TranslateToAscii(input)
        intputForComputerCopy = inputForComputer.copy()

        self.GetTextScreenFromComputerAndDraw()

        self._computer.SetInput(inputForComputer)
        outputLines = []


        for ioCycles in range(0,5):
            line = self._computer.GetLine()
            outputLines.append(line)
            self._computer.SendLine()

        line = self._computer.GetLine()
        assert(len(line)==0)
        while(True):
            self.GetTextScreenFromComputerAndDraw()
        oneResult, continueRun, inputNext = self._computer.RunToNextIO()
        oneResult, continueRun, inputNext = self._computer.RunToNextIO()
        assert(inputNext == False)
        assert(oneResult is not None)
        print(f"Space dust collected {oneResult}")

        nextOpCode = self._computer.PeekAtOpCodeValue()
        
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
                elif (event.key == pygame.K_f): #f does the fill with oxygen on the Day 15 maze
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    self.FillWithOxygen()
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                elif (event.key == pygame.K_j): #j searches for junctions for calibration for Day 17-1
                    #do the visualized search for junctions
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    self.SearchForJunctions()
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                elif (event.key == pygame.K_r): #r restarts the computer.
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    self.DoFinalRobotRun()
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                elif (event.key == pygame.K_u):  #self.UpdateDisplay was left over from Day 15.  I rigged 'u' to it to see some new blocks
                    self.UpdateDisplay(-1)
                elif (event.key == pygame.K_w):
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                    self.WalkScaffold()
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                elif (event.key == pygame.K_SPACE): #starts the current Computer program (displays the scaffold, etc.)
                    oldValue = self._started
                    if (oldValue == False):
                         pygame.mouse.set_cursor(*pygame.cursors.broken_x) #about to run the computer, so display a different mouse cursor
                    self._started = True if self._started == False else False
                   
            
            if event.type == pygame.QUIT: 
                pygame.quit() 
                quit() 

    def GetTextScreenFromComputerAndDraw(self):
        self._textScreenDraw = self._textScreenDraw + 1
        self._textScreen._lines = []
        while (True):
            line = self._computer.GetLine()
            if (len(line.strip())==0):
                break
            self._textScreen.AddLine(line)
        if (self._textScreenDraw % 10 == 0):
            self.DrawTextScreenToGameScreen()

    def MainLoop(self):
        while(True):
            pygame.display.update()

            self.ProcessGameEvents()
  
            if (self._started):
                # Run the computer code up to next output result, accumulating results in the text screen
                self._started = False
                self.GetTextScreenFromComputerAndDraw()
                
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
            
            
