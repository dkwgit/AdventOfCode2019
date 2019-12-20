import os
import sys
import pygame
sys.path.append(os.path.abspath('../IntCodeComputer'))

import itertools
from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture
from Game import Game

class Day13Driver:

    def __init__(self):
        self._game = None 
        self._computer = None
        self._output = []

    def FirstRun(self):
        continueRun = True
        while (continueRun):
            result,continueRun = self._computer.RunToNextOutput()
            if (result is not None):
                self._output.append(result)
        val = iter(self._output)
        blockCount = 0
        triplets = []
        for x,y,char in zip(val,val,val):
            if (char == 2):
                blockCount = blockCount + 1
            triplets.append(((x,y),char))
        print(f"Block count {blockCount}")
        minX = min(triplets, key = lambda x: x[0][0])[0][0]
        minY = min(triplets, key = lambda x: x[0][1])[0][1]
        maxX = max(triplets, key = lambda x: x[0][0])[0][0]
        maxY = max(triplets, key = lambda x: x[0][1])[0][1]
        self._game = Game((minX,minY,maxX,maxY))
        self._game.UpdateDisplay(self._output)

    def Run(self):
        self._computer = Computer()
        self._computer.LoadProgram(DataFixture.mainDay13)
        self.FirstRun()

d = Day13Driver()
d.Run()