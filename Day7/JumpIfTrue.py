from Operation import Operation as Operation

class JumpIfTrue(Operation):

    def __init__(self, computer, programLocation):
        super().__init__(computer, programLocation)

    def Execute(self):
        condition = self._parameters[0].GetValue()
        if (condition > 0 or condition < 0):
            newProgramIndex = self._parameters[1].GetValue()
            self._computer.MoveAbsolute(newProgramIndex)
        else:
            self._moveProgramIndex = True
        return None

    def SetWidth(self):
        return 3

    def SetWriteOnLastParameter(self):
        return False

    def SetMoveProgramIndex(self):
        return False

    def SetParameterCount(self):
        return 2