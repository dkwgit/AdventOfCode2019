from Operation import Operation as Operation

class Input(Operation):
    def __init__(self, computer, programLocation, testInput):
        self.testInput = testInput
        super().__init__(computer, programLocation)

    def Execute(self):
        if (self.testInput is None):
            value = int(input("Input a value: "))
        else:
            value = self.testInput
        writeLocation = self._parameters[0].GetValue()
        self._computer.WriteLocation(writeLocation,value)
        return None

    def SetWidth(self):
        return 2

    def SetWriteOnLastParameter(self):
        return True

    def SetMoveProgramIndex(self):
        return True

    def SetParameterCount(self):
        return 1