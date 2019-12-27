class FFT:

    def __init__(self, basePattern, message):
        self._basePattern = basePattern
        self._currentMessage = message
        self._phaseCounter = 0
        self._messageHistory = [ message ]
        

    def DoPhase(self):

        newMessage = []

        self._messageHistory.append(self.ConvertToString(newMessage))
        self._phaseCounter = self.PhaseCounter + 1
        return (self._phaseCounter,self._messageHistory[-1])

    def ConvertListToString(dataArray):
        return map(lambda x: str(x),dataArray).join('')

    def ConvertStringToIntArray(s):
        return list(map(lambda x: int(x), list(s)))