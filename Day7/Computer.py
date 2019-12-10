from Addition import Addition as Addition
from Multiplication import Multiplication as Multiplication
from Input import Input as Input
from Output import Output as Output
from JumpIfTrue import JumpIfTrue as JumpIfTrue
from JumpIfFalse import JumpIfFalse as JumpIfFalse
from LessThan import LessThan as LessThan
from Equals import Equals as Equals
from Halt import Halt as Halt
import sys

class Computer:

    opCodeTable = {
            1 : lambda computer, programlocation :  Addition(computer,programlocation),
            2 : lambda computer, programlocation :  Multiplication(computer,programlocation),
            3 : lambda computer, programlocation,testInput=None :  Input(computer,programlocation,testInput),
            4 : lambda computer, programlocation :  Output(computer,programlocation),
            5 : lambda computer, programlocation :  JumpIfTrue(computer,programlocation),
            6 : lambda computer, programlocation :  JumpIfFalse(computer,programlocation),
            7 : lambda computer, programlocation :  LessThan(computer,programlocation),
            8 : lambda computer, programlocation :  Equals(computer,programlocation),
            99: lambda computer, programlocation :  Halt(computer,programlocation)
        }

    def __init__(self, programData, programStart=0):
        self._programData = programData.copy()
        self._programIndex = programStart
        self._programLine = 0
        self._output = None
        
    def ReadLocation(self, location):
        return self._programData[location]

    def MoveByOffset(self, amount):
        self._programIndex  = self._programIndex  + amount

    def MoveAbsolute(self, location):
        self._programIndex = location

    def WriteLocation(self, location, value):
        self._programData[location] = value

    def Run(self, testMode = False, testData = None):
        go = True
        while(True == go):
            value = self.ReadLocation(self._programIndex)
            valueAsString = str(value)
            if (len(valueAsString)>2):
                value = int(valueAsString[-2:])
            opCodeConstructor = self.opCodeTable[value]

            if (testMode == False): 
                opCode = opCodeConstructor(self,self._programIndex)
            else:
                if (value == 3):
                    opCode = opCodeConstructor(self,self._programIndex, testData[0])
                else:
                    opCode = opCodeConstructor(self,self._programIndex)

            if (isinstance(opCode, Halt)):
                go = False

            self._output  = opCode.RunOpCode()

            if (testMode == True and value == 4): 
                assert(self._output== testData[1])

            self._programLine = self._programLine + 1