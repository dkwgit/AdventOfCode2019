import numpy as np
import itertools

class FFT:

    def __init__(self, basePattern, message, offset=0):
        self._offset = offset
        self._basePattern = np.array(basePattern,np.int64)
        lenBasePattern = len(self._basePattern)
        self._currentMessage = np.array(message,np.int64)
        self._lenMessage = len(self._currentMessage)
        print(f"Message length for offset at {offset} is {self._lenMessage}")
                
        self._phaseCounter = 0
        self._messageHistory = [ self._currentMessage ]
        
    def GetTransformArray(self,index):
        offset = self._offset
        transformArray = np.zeros((self._lenMessage),np.int64)
        baseMultiplied = itertools.chain(itertools.chain.from_iterable(itertools.repeat(x, index+offset+1) for x in self._basePattern[1:]), itertools.cycle(itertools.chain.from_iterable(itertools.repeat(x, index+offset+1) for x in self._basePattern)))
        for b in range(index, self._lenMessage):
            transformArray[b] = next(baseMultiplied)
        return transformArray

    def DoPhase(self):
        print(f"On phase {self._phaseCounter}")
        newMessage = []

        for a in range(0,self._lenMessage):
            transformArray = self.GetTransformArray(a)
            mult = np.multiply(self._currentMessage,transformArray)
            summed = abs(np.sum(mult))
            newMessage.append(summed % 10)

        self._currentMessage = np.array(newMessage,np.int64)
        self._messageHistory.append(self._currentMessage)
        self._phaseCounter = self._phaseCounter + 1
        return (self._phaseCounter,self._messageHistory[-1])

    def ConvertListToString(dataArray):
        return "".join(list(map(lambda x: str(x),dataArray)))

    def ConvertStringToIntArray(s):
        return list(map(lambda x: int(x), list(s)))