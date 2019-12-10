from Operation import Operation as Operation

class Addition(Operation):

    def __init__(self,computer, programLocation):
        super().__init__(computer, programLocation)

    def Execute(self):
        a = self._parameters[0].GetValue()
        b = self._parameters[1].GetValue()
        value = a + b
        writeLocation = self._parameters[2].GetValue()
        self._computer.WriteLocation(writeLocation,value)
        return None

    def SetWidth(self):
        return 4

    def SetWriteOnLastParameter(self):
        return True

    def SetMoveProgramIndex(self):
        return True

    def SetParameterCount(self):
        return 3