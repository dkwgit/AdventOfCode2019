from Day16DataFixture import Day16DataFixture as df
from FFT import FFT as FFT

class Day16Driver:


    def GetFFT(self, basePattern, startMessage):
        basePattern = list(map(lambda x: int(x),basePattern))
        startMessage = FFT.ConvertStringToIntArray(startMessage)
        return FFT(basePattern, startMessage)

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

    def Day16Part1(self,phase,basePattern,startMessage):
        fft = self.GetFFT(basePattern, startMessage)
        for x in range(0,phase):
            (discard, result) = fft.DoPhase()
        print(f"Day 16 part 1 result: {FFT.ConvertListToString(result[0:8])}")



d = Day16Driver()
test1Data = df.test1.copy()
d.TestMultiplePhases(df.basePattern,test1Data[0],test1Data[1:])
for phase,message,expectedResult in [df.test2,df.test3,df.test4]:
    d.TestPhaseNumber(phase,df.basePattern,message,expectedResult)
d.Day16Part1(100,df.basePattern,df.mainDay16)
