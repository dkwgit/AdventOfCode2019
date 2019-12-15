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

    def RunProgram(self, programData):
        self._programData = programData.copy()
        moreMemory = []
        for idx in range(0,1024):
            moreMemory.append(0)
        self._programData.extend(moreMemory)
        self._programIndex = 0
        self._programLine = 0
        if (self._thread):
            self._thread.start()
        else:
            return self.Run()

    def __init__(self,unattended = False, unattendedInputs = None):
        self._programData = None
        self._programIndex = None
        self._programLine = None
        self._unattended = unattended
        self._unattendedInputs = unattendedInputs
        self._currentUnattendedInput = 0
        self._outputs = []
        self._state = -1
        self._relativeBase = 0
        self._thread = None
        self._threadFunc = None
        self._inputEvent = None
        self._outputEvent = None
        self._relativeBase = 0

    def GetRelativeBase(self):
        return self._relativeBase

    def AdjustRelativeBase(self, val):
        self._relativeBase = self._relativeBase + val

    def AddInput(self, inputValue):
        assert(self._unattended == True)
        self._unattendedInputs.append(inputValue)
        if (self._inputEvent is not None):
            self._inputEvent.set()

    def GetState(self):
        return self._state

    def GetAllOutputs(self):
        return self._outputs

    def GetLastOutput(self):
        assert(self.GetState() == 0)
        return self._outputs[-1]

    def GetHighestOutput(self):
        if (self._outputEvent is not None):
            self._outputEvent.wait()
            self._outputEvent.clear()
        return self._outputs[-1]
    
    def SetOutput(self, value):
        self._outputs.append(value)

    def GetUnattendedInput(self):
        assert(self._unattended == True)
        if (self._unattended == True):
            if (self._currentUnattendedInput == len(self._unattendedInputs) and self._inputEvent != None):
                self._inputEvent.wait()
                self._inputEvent.clear()
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

    def Boot(self,threaded=False):
        if (threaded):
            func =  lambda computer: computer.Run()
            self._threadFunc = func
            self._thread = threading.Thread(target=self._threadFunc, args=(self,))
            self._inputEvent = threading.Event()
            self._outputEvent = threading.Event()
            bootInfo = (self._thread, self._inputEvent, self._outputEvent)
        else:
            bootInfo = (None)
        return bootInfo

    def Run(self):
        self._state = 1
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
                if (self._outputEvent is not None):
                    self._outputEvent.set()

            self._programLine = self._programLine + 1
        self._state = 0
        return self._outputs[-1]