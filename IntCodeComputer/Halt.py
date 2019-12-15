from Operation import Operation as Operation

class Halt(Operation):

    def __init__(self, computer, programLocation):
        return
    
    def RunOpCode(self):
        return None

    def Execute(self):
        return None

    def SetWidth(self):
        return 1

    def SetWriteOnLastParameter(self):
        return False

    def SetMoveProgramIndex(self):
        return False

    def SetParameterCount(self):
        return 0