from Day16DataFixture import Day16DataFixture as df
from FFT import FFT as FFT

class Day16Driver:

    def __init__(self, basePattern, startMessage):
        self._startMessage = startMessage
        self._basePattern = basePattern

    def Run(self):
        fft = FFT(self._basePattern, self._startMessage)
        result = fft.DoPhase()


d = Day16Driver(list(map(lambda x : int(x), df.basePattern)), FFT.ConvertStringToIntArray(df.test1[0]))
d.Run()
