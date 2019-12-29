from Day16DataFixture import Day16DataFixture as df
from FFT import FFT as FFT

class Day16Driver:


    def GetFFT(self, basePattern, startMessage, offset=0):
        basePattern = list(map(lambda x: int(x),basePattern))
        startMessage = FFT.ConvertStringToIntArray(startMessage)
        return FFT(basePattern, startMessage, offset)

    def TestMultiplePhases(self,basePattern,startMessage,resultsPerPhase):
        fft = self.GetFFT(basePattern, startMessage)
        for expectedResult in resultsPerPhase:
            counter,result = fft.DoPhase()
            assert(expectedResult==FFT.ConvertListToString(result))

    def TestPhaseNumber(self,phase,basePattern,startMessage,expectedLeft8Characters):
        fft = self.GetFFT(basePattern, startMessage)
        for x in range(0,phase):
            (discard, result) = fft.DoPhase()
        assert(expectedLeft8Characters==FFT.ConvertListToString(result[0:8]))

    def TestPhaseNumberWithOffset(self,phase,basePattern,startMessage,expectedLeft8Characters):
        offset = int(startMessage[:7])
        startMessage = startMessage * 10000
        fft = self.GetFFT(basePattern, startMessage[offset:], offset)
        for x in range(0,phase):
            (discard, result) = fft.DoPhase()
        print(f"Result at phase {phase}: {FFT.ConvertListToString(result[0:8])} while expected is {expectedLeft8Characters}")
        assert(expectedLeft8Characters==FFT.ConvertListToString(result[0:8]))

    def Day16Part1(self,phase,basePattern,startMessage):
        fft = self.GetFFT(basePattern, startMessage)
        for x in range(0,phase):
            (discard, result) = fft.DoPhase()
        print(f"Day 16 part 1 result: {FFT.ConvertListToString(result[0:8])}")

    def Day16Part2(self,phase,basePattern,startMessage):
        offset = int(startMessage[:7])
        startMessage = startMessage * 10000
        fft = self.GetFFT(basePattern, startMessage[offset:], offset)
        for x in range(0,phase):
            (discard, result) = fft.DoPhase()
        print(f"Day 16 part 2 result: {FFT.ConvertListToString(result[0:8])}")

d = Day16Driver()
test1Data = df.test1.copy()
d.TestMultiplePhases(df.basePattern,test1Data[0],test1Data[1:])
for phase,message,expectedResult in [df.test2,df.test3,df.test4]:
    d.TestPhaseNumber(phase,df.basePattern,message,expectedResult)
d.Day16Part1(100,df.basePattern,df.mainDay16)  #67481260
for phase,message,expectedResult in [df.test5,df.test6,df.test7]:
    d.TestPhaseNumberWithOffset(phase,df.basePattern,message,expectedResult)
#d.Day16Part2(100,df.basePattern,df.mainDay16) #42178738
