from DataFixture import *
from MoonTimeSeries import MoonTimeSeries as MoonTimeSeries

class Day12Driver:

    def TestCalculateNextInSeries(self):
        mts = MoonTimeSeries()
        testData = DataFixture.startInfo
        testList = []
        for index,data in testData:
            testList.append(data)
        resultList = [DataFixture.startInfo[0][1]]
        index = 1
        for item in mts.GetIterator(DataFixture.startInfo[0][1],10):
            print(f"Test {index}: result from time series is same as test data")
            resultList.append(item)
            testItem = testList[index]
            if (testItem != item):
                print(f"Test: {testItem}")
                print(f"Actual {item}")
            assert(testItem == item)
            index = index + 1

d = Day12Driver()
d.TestCalculateNextInSeries()


    