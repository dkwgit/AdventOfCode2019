import sys
import numpy as np
import itertools
from concurrent import futures
import threading

class FFT:

    def __init__(self, basePattern, message, offset=0):
        self._offset = offset
        self._basePattern = np.array(basePattern,np.int32)
        self._currentMessage = np.array(message,np.int32)
        self._lenMessage = len(self._currentMessage)
        print(f"Message length for offset at {offset} is {self._lenMessage}")
                
        self._phaseCounter = 0
        self._messageHistory = [ self._currentMessage ]

        self._messageLengthZeroArrayTemplate = np.zeros(self._lenMessage, np.int64)
        
    def Transform(self, index, iterations):
        #Unused: my attempt at providing the transform array.  It was slower than using itertools
        start = iterations - 1
        if (index < start):
            return 0
        divisor = iterations * 4
        remainder = index % divisor
        if (remainder >= start and remainder < start + iterations):
            return 1
        if (remainder >= start + iterations  and remainder < start + 2 * iterations):
            return 0
        if (remainder >= start + 2 * iterations and remainder < start + 3 * iterations):
            return -1
        if (remainder >= start + 3 * iterations or  remainder < start):
            return 0

    def GetTransformArray(self,index):
        offset = self._offset
        transformArray = np.copy(self._messageLengthZeroArrayTemplate, np.int16)
        baseMultiplied = itertools.chain(itertools.chain.from_iterable(itertools.repeat(x, index+offset+1) for x in self._basePattern[1:]), itertools.cycle(itertools.chain.from_iterable(itertools.repeat(x, index+offset+1) for x in self._basePattern)))
        for b in range(index, self._lenMessage):
            transformArray[b] = next(baseMultiplied) 
        return transformArray

    def DoPhase(self):
        print(f"On phase {self._phaseCounter + 1}")
        newMessage = np.copy(self._messageLengthZeroArrayTemplate, np.int16)
        
        
        def DoPhaseWhenAllOnes(s):
            for x in s:
                summed = abs(np.sum(self._currentMessage[x:]))
                newMessage[x] = summed % 10

        def DoPhaseNormally(s):
            for x in s:
                transformArray = self.GetTransformArray(x)
                mult = np.multiply(self._currentMessage,transformArray)
                summed = abs(np.sum(mult))
                newMessage[x] = summed % 10


        with futures.ThreadPoolExecutor(max_workers=8) as ex:
            allIndices = [x for x in range(0, self._lenMessage)]
            slices = [allIndices[x:x+100] for x in range(0, self._lenMessage,100)]
            for x in range(0,len(slices)):
                if (self._offset > self._lenMessage):
                    ex.submit(DoPhaseWhenAllOnes, slices[x])
                else:
                    ex.submit(DoPhaseNormally, slices[x])
                
                val = slices[x][-1] + 1
                if (val % 5000 == 0):
                    print(f"\t{self._phaseCounter}: Submitted high index of {val}")            

        self._currentMessage = newMessage
        self._messageHistory.append(self._currentMessage)
        self._phaseCounter = self._phaseCounter + 1
        return (self._phaseCounter,self._messageHistory[-1])

    def ConvertListToString(dataArray):
        return "".join(list(map(lambda x: str(x),dataArray)))

    def ConvertStringToIntArray(s):
        return list(map(lambda x: int(x), list(s)))