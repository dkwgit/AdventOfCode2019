from Operation import Operation as Operation

class Addition(Operation):

    def __init__(self,computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex):
        super().__init__(computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex)

    def Execute(self):
        a = self._parameters[0].GetValue()
        b = self._parameters[1].GetValue()
        value = a + b
        writeLocation = self._parameters[2].GetValue()
        self._computer.WriteLocation(writeLocation,value)
        return None