from Operation import Operation as Operation

class AdjustRelativeBase(Operation):

    def __init__(self, computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex):
        super().__init__(computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex)

    def Execute(self):
        val = self._parameters[0].GetValue()
        self._computer.AdjustRelativeBase(val)