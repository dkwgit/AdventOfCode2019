from abc import ABC, abstractmethod
import sys
from enum import Enum

inputData = inputData = [
    3,225,                  #0
    1,225,6,6,              #2
    1100,1,238,225,         #6
    104,0,                  #10
    1002,36,25,224,         #12
    1001,224,-2100,224,     #16
    4,224,                  #20
    1002,223,8,223,         #22
    101,1,224,224,          #26
    1,223,224,223,          #30
    1102,31,84,225,         #34
    1102,29,77,225,         #38
    1,176,188,224,          #42
    101,-42,224,224,        #46
    4,224,                  #50
    102,8,223,223,
    101,3,224,224,
    1,223,224,223,
    2,196,183,224,
    1001,224,-990,224,
    4,224,
    1002,223,8,223,
    101,7,224,224,
    1,224,223,223,
    102,14,40,224,
    101,-1078,224,224,
    4,224,
    1002,223,8,223,
    1001,224,2,224,
    1,224,223,223,
    1001,180,64,224,
    101,-128,224,224,
    4,224,
    102,8,223,223,
    101,3,224,224,
    1,223,224,223,
    1102,24,17,224,
    1001,224,-408,224,
    4,224,
    1002,223,8,223,
    101,2,224,224,
    1,223,224,223,
    1101,9,66,224,
    1001,224,-75,224,
    4,224,
    1002,223,8,223,
    1001,224,6,224,
    1,223,224,223,
    1102,18,33,225,
    1101,57,64,225,
    1102,45,11,225,
    1101,45,9,225,
    1101,11,34,225,
    1102,59,22,225,
    101,89,191,224,
    1001,224,-100,224,
    4,224,
    1002,223,8,223,
    1001,224,1,224,
    1,223,224,223,
    4,223,
    99,
    0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,359,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,404,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,677,226,224,1002,223,2,223,1005,224,464,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,524,101,1,223,223,1007,677,226,224,102,2,223,223,1005,224,539,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,554,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,569,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,614,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,629,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,644,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,659,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]

class ParameterTypeEnum(Enum):
    POSITIONAL = 0
    IMMEDIATE = 1

class Parameter:

    def __init__(self,computer,location,type,writeLocationParameter=False):
        self._computer = computer
        self._location = location
        self._type = type
        self._writeLocationParameter = writeLocationParameter

    def GetValue(self):
        if (ParameterTypeEnum(self._type) == ParameterTypeEnum.IMMEDIATE or self._writeLocationParameter == True):
            return self._computer.GetLocation(self._location)
        else:
            return self._computer.GetLocation(self._computer.GetLocation(self._location))

class Operation(ABC):

    def __init__(self,computer,programLocation):
        self._computer = computer
        self._programLocation = programLocation
        self.Configure()

    def Configure(self):
        self._width = self.SetWidth()
        self._writeOnLastParameter = self.SetWriteOnLastParameter()
        self._parameterCount = self.SetParameterCount()
        self._parameterModeString = ''
        self._moveProgramIndex = self.SetMoveProgramIndex()
        self._opCode = -1
        self._parameters = []
        self.SetOpCodeInfo()
        self.SetParameters()
        
    def SetOpCodeInfo(self):
        rawOpCode = str(self._computer.GetLocation(self._programLocation))
        if (len(rawOpCode)<=2):
            self._opCode = int(rawOpCode)
            rawOpCode = ''
        else:
            self._opCode = int(rawOpCode[-2:])  #the two rightmost are the opcode
            rawOpCode = rawOpCode[0:len(rawOpCode)-2] #the left remainder is the parameter info
            self._parameterModeString = rawOpCode[::-1] #parameter info is reversed when we receive
        numParameters = len(self._parameterModeString) #number found so far
        while (numParameters < self._parameterCount):
            self._parameterModeString = self._parameterModeString + '0' #pad with zeroes
            numParameters = numParameters + 1
    
    def SetParameters(self):
        i = 0
        while(i < self._parameterCount):
            writeLocationParameter = True if i + 1 == self._parameterCount and self._writeOnLastParameter == True else False
            parameter = Parameter(self._computer,
                self._programLocation + 1 + i,
                int(self._parameterModeString[i]),
                writeLocationParameter)
            self._parameters.append(parameter)
            i = i + 1

    def RunOpCode(self):
        self.Execute()
        if (self._moveProgramIndex == True):
            self._computer.Move(self._width)
        pass

    @abstractmethod
    def Execute(self):
        pass

    @abstractmethod
    def SetWidth(self):
        pass

    @abstractmethod
    def SetWriteOnLastParameter(self):
        pass

    @abstractmethod
    def SetMoveProgramIndex(self):
        pass

    @abstractmethod
    def SetParameterCount(self):
        pass

class Addition(Operation):

    def __init__(self,computer, programLocation):
        super().__init__(computer, programLocation)

    def Execute(self):
        a = self._parameters[0].GetValue()
        b = self._parameters[1].GetValue()
        value = a + b
        writeLocation = self._parameters[2].GetValue()
        self._computer.WriteLocation(writeLocation,value)

    def SetWidth(self):
        return 4

    def SetWriteOnLastParameter(self):
        return True

    def SetMoveProgramIndex(self):
        return True

    def SetParameterCount(self):
        return 3

class Multiplication(Operation):

    def __init__(self, computer, programLocation):
        super().__init__(computer, programLocation)

    def Execute(self):
        a = self._parameters[0].GetValue() 
        b = self._parameters[1].GetValue()
        value = a * b
        writeLocation = self._parameters[2].GetValue()
        self._computer.WriteLocation(writeLocation,value)

    def SetWidth(self):
        return 4

    def SetWriteOnLastParameter(self):
        return True

    def SetMoveProgramIndex(self):
        return True

    def SetParameterCount(self):
        return 3

class Input(Operation):
    def __init__(self, computer, programLocation):
        super().__init__(computer, programLocation)

    def Execute(self):
        value = int(input("Input a value: "))
        writeLocation = self._parameters[0].GetValue()
        self._computer.WriteLocation(writeLocation,value)

    def SetWidth(self):
        return 2

    def SetWriteOnLastParameter(self):
        return True

    def SetMoveProgramIndex(self):
        return True

    def SetParameterCount(self):
        return 1

class Output(Operation):

    def __init__(self, computer, programLocation):
        super().__init__(computer, programLocation)

    def Execute(self):
        value = self._parameters[0].GetValue()
        print(f"Value: {value}")

    def SetWidth(self):
        return 2

    def SetWriteOnLastParameter(self):
        return False

    def SetMoveProgramIndex(self):
        return True

    def SetParameterCount(self):
        return 1

class Computer:

    opCodeTable = {
            1 : lambda computer, programlocation :  Addition(computer,programlocation),
            2 : lambda computer, programlocation :  Multiplication(computer,programlocation),
            3 : lambda computer, programlocation :  Input(computer,programlocation),
            4 : lambda computer, programlocation :  Output(computer,programlocation),
            99: lambda computer, programlocation :  sys.exit()
        }

    def __init__(self, programData, programStart):
        self._programData = programData
        self._programIndex = programStart
        self._programLine = 0
        
    def GetLocation(self, location):
        return self._programData[location]

    def Move(self, amount):
        self._programIndex  = self._programIndex  + amount

    def WriteLocation(self, location, value):
        self._programData[location] = value

    def Run(self):
        while(1==1):
            value = self.GetLocation(self._programIndex)
            valueAsString = str(value)
            if (len(valueAsString)>2):
                value = int(valueAsString[-2:])
            func = self.opCodeTable[value]
            opCode = func(self,self._programIndex)
            opCode.RunOpCode()
            self._programLine = self._programLine + 1

c = Computer(inputData.copy(),0)
c.Run()