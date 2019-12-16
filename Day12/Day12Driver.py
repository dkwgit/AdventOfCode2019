from DataFixture import *
from MoonTimeSeries import MoonTimeSeries as MoonTimeSeries
import math

class Day12Driver:

    def TestCalculateNextInSeries(self):
        mts = MoonTimeSeries()
        testData = DataFixture.testSeries1
        testList = []
        for index,data in testData:
            testList.append(data)
        resultList = [DataFixture.testSeries1[0][1]]
        index = 1
        for item in mts.GetIterator(DataFixture.testSeries1[0][1],10):
            print(f"Test {index}: result from time series is same as test data")
            resultList.append(item)
            testItem = testList[index]
            if (testItem != item):
                print(f"Test: {testItem}")
                print(f"Actual {item}")
            assert(testItem == item)
            index = index + 1

    def CalculateEnergyOfSystem(self, system):
        systemEnergy = 0
        for item in system:
            potentialEnergy = abs(item.moonPosition.x) + abs(item.moonPosition.y) + abs(item.moonPosition.z)
            kineticEnergy = abs(item.moonVelocity.x) + abs(item.moonVelocity.y) + abs(item.moonVelocity.z)
            totalEnergy = potentialEnergy * kineticEnergy
            systemEnergy = systemEnergy + totalEnergy
        return systemEnergy

    def CalculateEnergyForSeries(self,iterations,data):
        index,energySeries = DataFixture.energySeries[0]
        mts = MoonTimeSeries()
        lastItem = None
        for index,item in enumerate(mts.GetIterator(data,iterations)):
            lastItem = item
        totalEnergyOfSystem = self.CalculateEnergyOfSystem(lastItem)
        print(f"Total energy of system after {iterations} iterations: {totalEnergyOfSystem}")
        return (totalEnergyOfSystem, lastItem)
        
d = Day12Driver()
d.TestCalculateNextInSeries()
index,testData = DataFixture.testSeries1[0]
d.CalculateEnergyForSeries(10,testData) #179
d.CalculateEnergyForSeries(1000,testData) #181
index,energySeries = DataFixture.energySeries[0]
d.CalculateEnergyForSeries(100,energySeries) #1940  --100 is fine
d.CalculateEnergyForSeries(1000,energySeries) #14645 --but 1000 is somehow wrong!


    