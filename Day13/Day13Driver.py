import os
import sys
sys.path.append(os.path.abspath('../IntCodeComputer'))

import itertools
from Computer import Computer as Computer
from DataFixture import DataFixture as DataFixture

class Day13Driver:

    table = {
        0: ' ',      #empty
        1: '\u2588', #wall
        2: '\u2592', #block
        3: '\u2582', #horizontal paddle
        4: 'o'       #ball
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
                line = line + char
                index = index + 1
            print(line)

d = Day13Driver()
d.Run()