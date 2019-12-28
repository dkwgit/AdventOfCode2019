import numpy as np
import itertools

class FFT:

    def __init__(self, basePattern, message):
        self._lenMessage = len(message)
        self._basePattern = np.array(basePattern,np.int64)
        lenBasePattern = len(self._basePattern)
        self._currentMessage = np.array(message,np.int64)
        transformArray = np.zeros((self._lenMessage,self._lenMessage))

        for a in range(0,self._lenMessage):
            baseMultiplied = itertools.cycle(itertools.chain.from_iterable(itertools.repeat(x, a+1) for x in self._basePattern))
            for skip in range(0,a+1):
                next(baseMultiplied)
            for b in range(a, self._lenMessage):
                transformArray[a,b] = next(baseMultiplied)
                
        self._transformArray = transformArray
        self._phaseCounter = 0
        self._messageHistory = [ self._currentMessage ]
        

    def DoPhase(self):

        newMessage = []

        for a in range(0,self._lenMessage):
            mult = np.multiply(self._currentMessage,self._transformArray[a])
            newMessage.append(int(list(str(int(sum(mult))))[-1]))

        self._currentMessage = np.array(newMessage,np.int64)
        self._messageHistory.append(self._currentMessage)
        self._phaseCounter = self._phaseCounter + 1
        return (self._phaseCounter,self._messageHistory[-1])

    def ConvertListToString(dataArray):
        return "".join(list(map(lambda x: str(x),dataArray)))

    def ConvertStringToIntArray(s):
        return list(map(lambda x: int(x), list(s)))