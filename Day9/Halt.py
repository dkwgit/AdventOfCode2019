from Operation import Operation as Operation

class Halt(Operation):

    def __init__(self, computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex):
        super().__init__(computer, programLocation, parameterCount, writeOnLastParameter, moveProgramIndex)
        return
    
    def RunOpCode(self):
        return None

    def Execute(self):
        return None