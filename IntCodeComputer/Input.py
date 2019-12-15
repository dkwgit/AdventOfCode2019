from Operation import Operation as Operation

class Input(Operation):
    def __init__(self, computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex):
        super().__init__(computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex)

    def Execute(self):
        value = self._computer.GetInput()
        writeLocation = self._parameters[0].GetValue()
        self._computer.WriteLocation(writeLocation,value)
        return None