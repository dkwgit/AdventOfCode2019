from DataFixture import *
from MoonTimeSeries import MoonTimeSeries as MoonTimeSeries
import math

class Day12Driver:

    def TestCalculateNextInSeries(self,testName,testData,iterations):
        print(f"Running test {testName}")
        mts = MoonTimeSeries()
        testList = []
        indexes = []
        for itemNumber,data in testData:
            testList.append((itemNumber,data))
            indexes.append(itemNumber)
        resultList = [(0,testData[0][1])]
        index = 1
        for item in mts.GetIterator(testData[0][1],iterations):
            resultList.append((index,item))
            if (index in indexes):
                print(f"\nSub test {index}: result from time series is same as test data")
                discard, testItem = [subtest for subtest in testList if subtest[0] == index][0]
                for rowActual, rowTest in zip(item,testItem):
                    if (rowActual != rowTest):
                        print(f"Test: {rowTest}")
                        print(f"Actual {rowActual}")
                    assert(rowActual == rowTest)
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
d.TestCalculateNextInSeries('Test: First test data from puzzle',DataFixture.testSeries1,10)
d.TestCalculateNextInSeries('Test: Energy series from puzzle',DataFixture.energySeries,100)
index,testData = DataFixture.testSeries1[0]
d.CalculateEnergyForSeries(10,testData) #179
d.CalculateEnergyForSeries(1000,testData) #183
index,energySeries = DataFixture.energySeries[0]
d.CalculateEnergyForSeries(100,energySeries) #1940  --100 is fine
d.CalculateEnergyForSeries(1000,energySeries) #14645 --but 1000 is somehow wrong!


    