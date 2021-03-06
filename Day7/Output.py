from Operation import Operation as Operation

class Output(Operation):

    def __init__(self, computer, programLocation):
        super().__init__(computer, programLocation)

    def Execute(self):
        value = self._parameters[0].GetValue()
        if (self._computer._unattended != True):
            print(f"Output instruction value: {value}")
        return value

    def SetWidth(self):
        return 2

    def SetWriteOnLastParameter(self):
        return False

    def SetMoveProgramIndex(self):
        return True

    def SetParameterCount(self):
        return 1