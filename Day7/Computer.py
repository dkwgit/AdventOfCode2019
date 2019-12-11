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
            1 : lambda computer, programlocation :   Addition(computer,programlocation),
            2 : lambda computer, programlocation :   Multiplication(computer,programlocation),
            3 : lambda computer, programlocation :   Input(computer,programlocation),
            4 : lambda computer, programlocation :   Output(computer,programlocation),
            5 : lambda computer, programlocation :   JumpIfTrue(computer,programlocation),
            6 : lambda computer, programlocation :   JumpIfFalse(computer,programlocation),
            7 : lambda computer, programlocation :   LessThan(computer,programlocation),
            8 : lambda computer, programlocation :   Equals(computer,programlocation),
            99: lambda computer, programlocation :   Halt(computer,programlocation)
        }

    def __init__(self, programData, unattended = False, unattendedInputs = None, programStart=0):
        self._programData = programData.copy()
        self._programIndex = programStart
        self._programLine = 0
        self._unattended = unattended
        self._unattendedInputs = unattendedInputs
        self._currentUnattendedInput = 0
        self._outputs = []

    def GetUnattendedInput(self):
        assert(self._unattended == True)
        if (self._unattended == True):
            assert(self._currentUnattendedInput < len(self._unattendedInputs))
            val = self._unattendedInputs[self._currentUnattendedInput]
            self._currentUnattendedInput = self._currentUnattendedInput + 1
            return val
        else:
            return None
        
    def ReadLocation(self, location):
        return self._programData[location]

    def MoveByOffset(self, amount):
        self._programIndex  = self._programIndex  + amount

    def MoveAbsolute(self, location):
        self._programIndex = location

    def WriteLocation(self, location, value):
        self._programData[location] = value

    def Run(self):
        go = True
        while(True == go):
            opCodeValue = self.ReadLocation(self._programIndex)
            valueAsString = str(opCodeValue)
            if (len(valueAsString)>2):
                opCodeValue = int(valueAsString[-2:])
            opCodeConstructor = self.opCodeTable[opCodeValue]
            opCodeInstance = opCodeConstructor(self,self._programIndex)

            if (isinstance(opCodeInstance, Halt)):
                go = False

            opCodeReturnValue = opCodeInstance.RunOpCode()

            if (isinstance(opCodeInstance, Output)): 
                self._outputs.append(opCodeReturnValue)

            self._programLine = self._programLine + 1
        return self._outputs[-1]