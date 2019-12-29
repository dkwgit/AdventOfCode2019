import sys
import numpy as np
import itertools
from concurrent import futures
import threading

class FFT:

    def __init__(self, basePattern, message, offset=0):
        self._offset = offset
        self._basePattern = np.array(basePattern,np.int32)
        lenBasePattern = len(self._basePattern)
        self._currentMessage = np.array(message,np.int32)
        self._lenMessage = len(self._currentMessage)
        print(f"Message length for offset at {offset} is {self._lenMessage}")
                
        self._phaseCounter = 0
        self._messageHistory = [ self._currentMessage ]
        self._lastTransformArray = None
        #self._transformArrayCache = np.zeros((self._lenMessage,self._lenMessage),np.int32)
        #for x in range(0, self._lenMessage):
            #self._transformArrayCache[x] = np.array(self.GetTransformArray(x),np.int32)
        
    def Transform(self, index, iterations):
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

    def GetTransformArray3(self,index):
        return self._transformArrayCache[index]

    def GetTransformArray(self,index):
        offset = self._offset
        if (self._lastTransformArray is None or index == 0):
            transformArray = np.zeros((self._lenMessage),np.int32)
            baseMultiplied = itertools.chain(itertools.chain.from_iterable(itertools.repeat(x, index+offset+1) for x in self._basePattern[1:]), itertools.cycle(itertools.chain.from_iterable(itertools.repeat(x, index+offset+1) for x in self._basePattern)))
            for b in range(index, self._lenMessage):
                transformArray[b] = next(baseMultiplied)
        else:
            transformArray = self._lastTransformArray
            transformArray[index - 1] = 0

        self._lastTransformArray = transformArray   
        return transformArray

    def GetTransformArray2(self,index):
        offset = self._offset
        transformArray = np.zeros((self._lenMessage),np.int32)
        for b in range(index, self._lenMessage):
            transformArray[b] = self.Transform(b+offset,index+offset+1)
        return transformArray

    def DoPhase(self):
        print(f"On phase {self._phaseCounter + 1}")
        newMessage = np.zeros(self._lenMessage,np.int32)
        def DoCharactersOfPhase(s):
            for x in s:
                summed = abs(np.sum(self._currentMessage[x:]))
                newMessage[x] = summed % 10

        with futures.ThreadPoolExecutor(max_workers=8) as ex:
            allIndices = [x for x in range(0, self._lenMessage)]
            slices = [allIndices[x:x+100] for x in range(0, self._lenMessage,100)]
            for x in range(0,len(slices)):
                ex.submit(DoCharactersOfPhase, slices[x])
                val = slices[x][-1] + 1
                if (val % 5000 == 0):
                    print(f"\t{self._phaseCounter}: Submitted high index of {val}")
        

                #if (a>0):
                    #sys.exit()
            #transformArray = self.GetTransformArray(a)
            #transformArray2 = self.GetTransformArray2(a)
            #assert(np.array_equal(transformArray,transformArray2))
            #mult = np.multiply(self._currentMessage,transformArray)

            

        self._currentMessage = newMessage
        self._messageHistory.append(self._currentMessage)
        self._phaseCounter = self._phaseCounter + 1
        return (self._phaseCounter,self._messageHistory[-1])

    def ConvertListToString(dataArray):
        return "".join(list(map(lambda x: str(x),dataArray)))

    def ConvertStringToIntArray(s):
        return list(map(lambda x: int(x), list(s)))