from DataFixture import DataFixture as DataFixture
from Image import Image as Image

#https://adventofcode.com/2019/day/8/

class Driver:
    def GetImage(self):
        rows, columns, rawData = DataFixture.Day7Part1MainData
        image = Image(rows, columns, rawData)
        return image
    
    def GetDigitCountsByLayer(self, image):
        countable = self.GetDigitCountInfo(image)
        digitCountsByLayer = self.CountDigits(countable)
        return digitCountsByLayer

    def GetDigitCountInfo(self, image):
        #mark 1 for each digit to make it easy to count
        countable = []
        for index,layer in enumerate(image.GetLayers()):
            countable.append(list(map(lambda x: (
                1 if int(x) == 0 else 0,
                1 if int(x) == 1 else 0,
                1 if int(x) == 2 else 0,
                int(x)), layer)))
        return countable
    
    def CountDigits(self, digitCounts):
        digitSums = []
        for layerIndex, layer in enumerate(digitCounts):
            zeroes = sum(map(lambda x: x[0], layer))
            ones = sum(map(lambda y: y[1], layer))
            twos = sum(map(lambda z: z[2], layer))
            digitSums.append((zeroes, ones, twos, layerIndex))
        return digitSums

d = Driver()
image = d.GetImage()
image.Process()

#Day8-1
digitsCountsByLayer = d.GetDigitCountsByLayer(image)
#digits are now in tuples (zeroesCount, onesCount, twosCount, layerIndex)
#sorting sort by count of zeroes since it's first in tuple, so smallest number of zeroes will be at index 0
digitsCountsByLayer.sort()  
lowestZeroesLayer = digitsCountsByLayer[0]
print(f"Day 8-1: Layer with lowest number of 0s is layer {lowestZeroesLayer[3]}, with {lowestZeroesLayer[0]} 0s. 1s and 2s multipled are {lowestZeroesLayer[1] * lowestZeroesLayer[2]}")

#Day8-1
print("\nDay 8-2: Password is")
image.Render()