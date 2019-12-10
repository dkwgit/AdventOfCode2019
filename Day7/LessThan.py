from Operation import Operation as Operation

class LessThan(Operation):

    def __init__(self, computer, programLocation):
        super().__init__(computer, programLocation)

    def Execute(self):
        a = self._parameters[0].GetValue()
        b = self._parameters[1].GetValue()
        if (a < b):
            self._computer.WriteLocation(self._parameters[2].GetValue(),1)
        else:
            self._computer.WriteLocation(self._parameters[2].GetValue(),0)
        return None

    def SetWidth(self):
        return 4

    def SetWriteOnLastParameter(self):
        return True

    def SetMoveProgramIndex(self):
        return True

    def SetParameterCount(self):
        return 3