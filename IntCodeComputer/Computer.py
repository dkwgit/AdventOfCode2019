from Addition import Addition as Addition
from Multiplication import Multiplication as Multiplication
from Input import Input as Input
from Output import Output as Output
from JumpIfTrue import JumpIfTrue as JumpIfTrue
from JumpIfFalse import JumpIfFalse as JumpIfFalse
from LessThan import LessThan as LessThan
from Equals import Equals as Equals
from Halt import Halt as Halt
from AdjustRelativeBase import AdjustRelativeBase as AdjustRelativeBase
import sys
import threading

class Computer:

    opCodeTable = {
            1 : lambda computer, programlocation :   Addition(computer,programlocation, 3, True, True),
            2 : lambda computer, programlocation :   Multiplication(computer,programlocation, 3, True, True),
            3 : lambda computer, programlocation :   Input(computer,programlocation, 1, True, True),
            4 : lambda computer, programlocation :   Output(computer,programlocation, 1, False, True),
            5 : lambda computer, programlocation :   JumpIfTrue(computer,programlocation, 2, False, False),
            6 : lambda computer, programlocation :   JumpIfFalse(computer,programlocation, 2, False, False),
            7 : lambda computer, programlocation :   LessThan(computer,programlocation, 3, True, True),
            8 : lambda computer, programlocation :   Equals(computer,programlocation, 3, True, True),
            9 : lambda computer, programlocation :   AdjustRelativeBase(computer,programlocation, 1, False, True),
            99: lambda computer, programlocation :   Halt(computer,programlocation, 1, False, False)
        }

    def GetOriginalProgram(self):
        return self._originalProgramData
        
    def LoadProgram(self, programData):
        self._programData = programData.copy()
        self._originalProgramData = self._programData.copy()
        moreMemory = [0] * 1024*10
        self._programData.extend(moreMemory)
        self._programIndex = 0
        self._programLine = 0
        return self
 
    def __init__(self):
        self._programData = None
        self._programIndex = None
        self._programLine = None
        self._relativeBase = 0
        self._input = None
        self._output = None
        self._halted = None

    def GetRelativeBase(self):
        return self._relativeBase

    def AdjustRelativeBase(self, val):
        self._relativeBase = self._relativeBase + val

    def SetInput(self, val):
        self._input = val

    def GetOutput(self):
        val = self._output
        self._output = None
        return val

    def GetInput(self):
        assert(self._input != None)
        val = self._input.pop(0)
        if (len(self._input) == 0):
            self._input = None
        return val
    
    def SetOutput(self, val):
        assert(self._output == None)
        self._output = val
        return self
        
    def ReadLocation(self, location):
        return self._programData[location]

    def MoveByOffset(self, amount):
        self._programIndex  = self._programIndex  + amount

    def MoveAbsolute(self, location):
        self._programIndex = location

    def WriteLocation(self, location, value):
        self._programData[location] = value

    def PeekAtOpCodeValue(self):
        opCodeValue = self.ReadLocation(self._programIndex)
        valueAsString = str(opCodeValue)
        if (len(valueAsString)>2):
            opCodeValue = int(valueAsString[-2:])
        return opCodeValue

    def GetHalted(self):
        return self._halted is not None and self._halted == True
    
    def RunToNextIO(self):
        continueRun = True
        result = None
        inputNext = False
        while (continueRun and result is None and inputNext == False): 
            oneResult, continueRun, inputNext = self.DoNext()
            if (oneResult is not None):
                result = oneResult
            if (self.PeekAtOpCodeValue() == 99):
                break
        return (result,continueRun,inputNext)

    def GetLine(self):
        continueRun = True
        inputNext = False
        output = []
        oneResult = 0
        while (continueRun and inputNext == False and oneResult != 10):
             oneResult, continueRun, inputNext = self.RunToNextIO()
             assert(inputNext == False)
             assert(continueRun == True)
             print(oneResult)
             output.append(oneResult)
        if (output[-1] == 10):
            output.pop()  #chop trailing newline
        #Rewrite in ascii
        output = "".join(list(map(lambda x: chr(x), output)))
        return output
             
    def SendLine(self):
        continueRun = True
        oneResult = None
        characterAboutToSend = 0
        while (continueRun and characterAboutToSend != 10):
             oneResult, continueRun, inputNext = self.RunToNextIO()
             assert(inputNext == True)
             assert(oneResult is None)
             characterAboutToSend = self._input[0]
             assert(self.PeekAtOpCodeValue() == 3)
             oneResult, continueRun, inputNext = self.DoNext()
        



    def DoNext(self):
        assert(self._halted is None or self._halted == False)
        self._halted = False
        opCodeValue = self.PeekAtOpCodeValue()
        opCodeConstructor = Computer.opCodeTable[opCodeValue]
        opCodeInstance = opCodeConstructor(self,self._programIndex)
        opCodeInstance.RunOpCode()
        returnValue = None
        if (opCodeValue == 4):
            returnValue = self.GetOutput()
        continueRun = True
        if (opCodeValue == 99):
            continueRun = False
            self._halted = True

        self._programLine = self._programLine + 1

        inputNext = False
        opCodeValue = self.PeekAtOpCodeValue()
        if (opCodeValue == 3):
            inputNext = True

        return (returnValue, continueRun, inputNext)
