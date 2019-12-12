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
        if (ParameterTypeEnum(self._type) == ParameterTypeEnum.IMMEDIATE or self._writeLocationParameter == True):
            return self._computer.ReadLocation(self._location)
        else:
            return self._computer.ReadLocation(self._computer.ReadLocation(self._location))