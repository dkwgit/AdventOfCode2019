import os
import sys
import pygame
sys.path.append(os.path.abspath('../IntCodeComputer'))
from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture
from Game import Game as Game

class Day15Driver:

    def Run(self):
        computer = Computer()
        program = DataFixture.mainDay15.copy()
        computer.LoadProgram(program)
        game = Game(computer)
        game.MainLoop()

d = Day15Driver()
d.Run()