from DataFixture import DataFixture as DataFixture
from Image import Image as Image

class Driver:

    def GetImage(self):
        columns, rows, rawData = DataFixture.Day7Part1MainData
        image = Image(columns, rows, rawData)
        return image
    
    def GetLayerDigitCounts(self, image):
        counts = []
        for index,layer in enumerate(image.GetLayers()):
            counts.append(list(map(lambda x: (
                1 if int(x) == 0 else 0,
                1 if int(x) == 1 else 0,
                1 if int(x) == 2 else 0,
                int(x)), layer)))
        return counts

d = Driver()
image = d.GetImage()
image.Process()
digitCounts = d.GetLayerDigitCounts(image)
digitSums = []
for index, layer in enumerate(digitCounts):
    zeroes = sum(map(lambda x: x[0], layer))
    ones = sum(map(lambda y: y[1], layer))
    twos = sum(map(lambda z: z[2], layer))
    digitSums.append((zeroes,ones,twos, index))
digitSums.sort()
lowestZeroes = digitSums[0]
print(f"Layer with lowest number of 0s is layer {lowestZeroes[3]}, with {lowestZeroes[0]} 0s. 1s and 2s multipled are {lowestZeroes[1] * lowestZeroes[2]}")
