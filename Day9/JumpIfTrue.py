from Operation import Operation as Operation

class JumpIfTrue(Operation):

    def __init__(self, computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex):
        super().__init__(computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex)

    def Execute(self):
        condition = self._parameters[0].GetValue()
        if (condition > 0 or condition < 0):
            newProgramIndex = self._parameters[1].GetValue()
            self._computer.MoveAbsolute(newProgramIndex)
        else:
            self._moveProgramIndex = True
        return None