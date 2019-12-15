from Operation import Operation as Operation

class Output(Operation):

    def __init__(self, computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex):
        super().__init__(computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex)

    def Execute(self):
        value = self._parameters[0].GetValue()
        return self._computer.SetOutput(value)