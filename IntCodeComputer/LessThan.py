from Operation import Operation as Operation

class LessThan(Operation):

    def __init__(self, computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex):
        super().__init__( computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex)

    def Execute(self):
        a = self._parameters[0].GetValue()
        b = self._parameters[1].GetValue()
        if (a < b):
            self._computer.WriteLocation(self._parameters[2].GetValue(),1)
        else:
            self._computer.WriteLocation(self._parameters[2].GetValue(),0)
        return None