from abc import ABC, abstractmethod
from Parameter import Parameter as Parameter

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
        rawOpCode = str(self._computer.ReadLocation(self._programLocation))
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
        val = self.Execute()
        if (self._moveProgramIndex == True):
            self._computer.MoveByOffset(self._width)
        return val

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