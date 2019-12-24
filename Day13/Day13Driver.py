import os
import sys
import pygame
sys.path.append(os.path.abspath('../IntCodeComputer'))

import itertools
from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture
from Game import Game as Game

class Day13Driver:

    def __init__(self):
        pass

    def SetupGameAndRun(self):
        
        computer = Computer()
        program = DataFixture.mainDay13.copy()
        program[0] = 2 #put in two quarters
        computer.LoadProgram(program)
        outputData = []

        #We do one run-through with computer to answer Day13-1 and also to get dimensions of "screen"
        continueRun = True
        inputEvent = False
        while (continueRun and inputEvent == False):
            result,continueRun,inputEvent = computer.RunToNextIO()
            if (inputEvent == False and result is not None):
                outputData.append(result)
        val = iter(outputData)
        blockCount = 0
        triplets = []
        for x,y,char in zip(val,val,val):
            if (char == 2):
                blockCount = blockCount + 1
            triplets.append(((x,y),char))
        #Day 13-1 answer
        print(f"Block count {blockCount}")

        #Get screen dimensions
        minX = min(triplets, key = lambda x: x[0][0])[0][0]
        minY = min(triplets, key = lambda x: x[0][1])[0][1]
        maxX = max(triplets, key = lambda x: x[0][0])[0][0]
        maxY = max(triplets, key = lambda x: x[0][1])[0][1]

        # Create the game with the dimensions and run it
        # Note: when the game is being played, there are two spurious bytes of input for an empty score at this point, hence the :-2: array slice
        game = Game(computer,(minX,minY),(maxX,maxY),outputData[:-2:])
        game.MainLoop()

d = Day13Driver()
d.SetupGameAndRun()