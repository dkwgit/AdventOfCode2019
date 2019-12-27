import os
import sys
import pygame
sys.path.append(os.path.abspath('../IntCodeComputer'))
from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture
from Game import Game as Game

class Day15Driver:

    def Run(self,data = None):
        computer = Computer()
        program = DataFixture.mainDay15.copy()
        computer.LoadProgram(program)
        game = Game(computer)
        if (data is not None):
            game.LoadMazeData(data)
        game.MainLoop()

    def LoadMazeFromFile(self,filePath):
        with open(filePath,'r') as f:
            mazeText = f.read()
        maze = eval(mazeText)
        return maze
        
#d = Day15Driver()
#d.Run() #I just counted my solution for part #1, it was 252
d = Day15Driver()
maze = d.LoadMazeFromFile('Maze.txt')
d.Run(maze) #This way of running maze will also compute path to origin from oxygen sensor (252 minutes = steps) and will output the whole time takne to fill maze  350