
import os
import sys
import pygame
sys.path.append(os.path.abspath('../IntCodeComputer'))
from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture
from Game import *

class Day17Driver:

    def Run(self,data = None):
        computer = Computer()
        program = DataFixture.mainDay17.copy()
        computer.LoadProgram(program)
        game = Game(computer)
        if (data is not None):
            game.LoadScreenData(data)
        game.MainLoop()


d=Day17Driver()
d.Run()