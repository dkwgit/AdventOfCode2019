from DataFixture import *
from MoonTimeSeries import MoonTimeSeries as MoonTimeSeries
import math
import numpy as np
import sys
from decimal import Decimal

class Day12Driver:

    def ConvertToNumpy(self, input):
        pos = np.array([
            [input[0].moonPosition.x,input[0].moonPosition.y,input[0].moonPosition.z],
            [input[1].moonPosition.x,input[1].moonPosition.y,input[1].moonPosition.z],
            [input[2].moonPosition.x,input[2].moonPosition.y,input[2].moonPosition.z],
            [input[3].moonPosition.x,input[3].moonPosition.y,input[3].moonPosition.z],
        ])
        vel = np.array([
            [input[0].moonVelocity.x,input[0].moonVelocity.y,input[0].moonVelocity.z],
            [input[1].moonVelocity.x,input[1].moonVelocity.y,input[1].moonVelocity.z],
            [input[2].moonVelocity.x,input[2].moonVelocity.y,input[2].moonVelocity.z],
            [input[3].moonVelocity.x,input[3].moonVelocity.y,input[3].moonVelocity.z],
        ])
        return np.array((pos,vel))

    def TestCalculateNextInSeries(self,testName,testData,iterations):
        print(f"Running test {testName}")
        mts = MoonTimeSeries()
        testList = []
        indexes = []
        for itemNumber,data in testData:
            testList.append((itemNumber,self.ConvertToNumpy(data)))
            indexes.append(itemNumber)
        row0 = testList[0][1]
        resultList = [(0,row0)]
        index = 1
        for item in mts.GetIterator(row0,iterations):
            resultList.append((index,item))
            if (index in indexes):
                print(f"\nSub test {index}: result from time series is same as test data")
                discard, testItem = [subtest for subtest in testList if subtest[0] == index][0]
                if (not np.array_equal(testItem,item)):
                    print(f"Test: {testItem}")
                    print(f"Actual {item}")
                    assert(np.array_equal(testItem,item))
            index = index + 1

    def GetHashForSystem(self, system):
        stringVersion= np.array_str(system,max_line_width=1024)
        return str(hash(stringVersion))


    def CalculateEnergyOfSystem(self, system):
        rows = np.shape(system[0])[0]
        systemEnergy = 0
        for r in range(rows):
            potentialEnergy = np.sum(np.abs(system[0][r]))
            kineticEnergy = np.sum(np.abs(system[1][r]))
            systemEnergy = systemEnergy + (potentialEnergy * kineticEnergy)
        return systemEnergy

    def CalculateEnergyForSeries(self,iterations,data):
        mts = MoonTimeSeries()
        lastItem = None
        for index,item in enumerate(mts.GetIterator(data,iterations)):
            lastItem = item
        totalEnergyOfSystem = self.CalculateEnergyOfSystem(lastItem)
        print(f"Total energy of system after {iterations} iterations: {totalEnergyOfSystem}")
        return (totalEnergyOfSystem, lastItem)

    def FindFirstRepeat(self,data,iterationsToTry):
        startState = data.copy()
        startStateX =  np.array((startState[0,:,0],startState[1,:,0]))
        startStateY =  np.array((startState[0,:,1],startState[1,:,1]))
        startStateZ =  np.array((startState[0,:,2],startState[1,:,2]))
        xMatch = None
        yMatch = None
        zMatch = None
        #hashes = {}
        mts = MoonTimeSeries()
        #h = self.GetHashForSystem(data)
        #hashes[h] = 0
        step = 1
        for index,item in enumerate(mts.GetIterator(data,iterationsToTry)):
            if (step % 100000 == 0):
                print(f"On step {step}")
            if (xMatch == None):
                if (np.array_equal(startStateX, np.array((item[0,:,0],item[1,:,0])))):
                    xMatch = step
            if (yMatch == None):
                if (np.array_equal(startStateY, np.array((item[0,:,1],item[1,:,1])))):
                    yMatch = step
            if (zMatch == None):
                if (np.array_equal(startStateZ, np.array((item[0,:,2],item[1,:,2])))):
                    zMatch = step
            if (xMatch is not None and yMatch is not None and zMatch is not None):
                #Got to go Decimal--the value overflowed
                x = Decimal(xMatch) 
                y = Decimal(yMatch)
                z = Decimal(zMatch)
                lcmArray = [x,y,z]
                lcmVal = np.lcm.reduce(lcmArray)
                print(f"At step {step} found a least common multiple for x,y,z matches: ",lcmVal)
                print(f"Match for x,y,z were achieved at steps {xMatch},{yMatch},{zMatch}")
                return
            #h = self.GetHashForSystem(item)
            #if step != 1 and h in hashes.keys():
            #   print(f"Same state occurs at step {step}!")
            #   return
            #hashes[h] = step
            step = step + 1
   
d = Day12Driver()
d.TestCalculateNextInSeries('Test: First test data from puzzle',DataFixture.testSeries1.copy(),10)
d.TestCalculateNextInSeries('Test: Energy series from puzzle',DataFixture.energySeries.copy(),100)

index,testData = DataFixture.testSeries1[0]
testData = d.ConvertToNumpy(testData)
d.CalculateEnergyForSeries(10,testData.copy()) #179
d.CalculateEnergyForSeries(1000,testData.copy()) #183

index,energySeries = DataFixture.energySeries[0]
energySeries = d.ConvertToNumpy(energySeries.copy())
d.CalculateEnergyForSeries(100,energySeries.copy()) #1940

index,day12Series = DataFixture.day12Series[0]
day12Series = d.ConvertToNumpy(day12Series.copy())
d.CalculateEnergyForSeries(1000,day12Series.copy()) #6849
d.FindFirstRepeat(testData.copy(),3000) #2772
d.FindFirstRepeat(day12Series.copy(), 10000000) #2000000000)



    