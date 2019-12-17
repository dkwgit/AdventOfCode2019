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

    def GetHashForSystem(self, system):
        systemAsString = ''
        for moon in system:
            systemAsString = systemAsString + "{}{}{}_{}{}{}|".format(moon.moonPosition.x,moon.moonPosition.y,moon.moonPosition.z,
            moon.moonVelocity.x,moon.moonVelocity.y,moon.moonVelocity.z)
        return hash(systemAsString)


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

    def FindFirstRepeat(self,data,iterationsToTry):
        hashes = {}
        mts = MoonTimeSeries()
        hashes[self.GetHashForSystem(data)] = 1
        step = 1
        for index,item in enumerate(mts.GetIterator(data,iterationsToTry)):
            h = hash(self.GetHashForSystem(item))
            if h in hashes.keys():
                print(f"Same state occurs at step {step}!")
                break
            if (step % 100000 == 0):
                print(f"On step {step}")
            hashes[h]=1
            data = item
            step = step + 1

        
d = Day12Driver()
d.TestCalculateNextInSeries('Test: First test data from puzzle',DataFixture.testSeries1,10)
d.TestCalculateNextInSeries('Test: Energy series from puzzle',DataFixture.energySeries,100)
index,testData = DataFixture.testSeries1[0]
d.CalculateEnergyForSeries(10,testData) #179
d.CalculateEnergyForSeries(1000,testData) #183
index,energySeries = DataFixture.energySeries[0]
d.CalculateEnergyForSeries(100,energySeries) #1940
index,day12Series = DataFixture.day12Series[0]
d.CalculateEnergyForSeries(1000,day12Series) #6849
d.FindFirstRepeat(testData,10000000) #2772
d.FindFirstRepeat(day12Series,10000000)


    