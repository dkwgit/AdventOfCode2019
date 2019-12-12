from enum import Enum

class ParameterTypeEnum(Enum):
    POSITIONAL = 0
    IMMEDIATE = 1
    RELATIVE = 2

class Parameter:

    def __init__(self,computer,location,type,writeLocationParameter=False):
        self._computer = computer
        self._location = location
        self._type = type
        self._writeLocationParameter = writeLocationParameter

    def GetValue(self):

        if (ParameterTypeEnum(self._type) == ParameterTypeEnum.IMMEDIATE):
            return self._computer.ReadLocation(self._location)
        if (ParameterTypeEnum(self._type) == ParameterTypeEnum.POSITIONAL):
            address = self._computer.ReadLocation(self._location)
            if (self._writeLocationParameter == True):
                return address
            else:
                return self._computer.ReadLocation(address)
        if (ParameterTypeEnum(self._type) == ParameterTypeEnum.RELATIVE):
            address = self._computer.ReadLocation(self._location) + self._computer.GetRelativeBase()
            if (self._writeLocationParameter == True):
                return address
            else:
                return self._computer.ReadLocation(address)

        