from DataFixture import *
from MoonTimeSeries import MoonTimeSeries as MoonTimeSeries
import math
import numpy as np

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

    def FindFirstRepeat(self,db,data,iterationsToTry):
        hashes = {}
        mts = MoonTimeSeries()
        h = self.GetHashForSystem(data)
        #db[h] = "0"
        hashes[h] = 0
        step = 1
        for index,item in enumerate(mts.GetIterator(data,iterationsToTry)):
            h = self.GetHashForSystem(item)
            #h in db.keys()
            if h in hashes.keys():
                print(f"Same state occurs at step {step}!")
                break
            if (step % 1000000 == 0):
                print(f"On step {step}")
                #db["step_"+str(step)] = np.array_str(item,max_line_width=1024)
            #db[h]=str(step)
            hashes[h] = step
            step = step + 1


#db = dbm.open('cache', 'c')       
d = Day12Driver()
#d.TestCalculateNextInSeries('Test: First test data from puzzle',DataFixture.testSeries1,10)
#d.TestCalculateNextInSeries('Test: Energy series from puzzle',DataFixture.energySeries,100)
#index,testData = DataFixture.testSeries1[0]
#testData = d.ConvertToNumpy(testData)
#d.CalculateEnergyForSeries(10,testData) #179
#d.CalculateEnergyForSeries(1000,testData) #289
#index,energySeries = DataFixture.energySeries[0]
#energySeries = d.ConvertToNumpy(energySeries)
#d.CalculateEnergyForSeries(100,energySeries) #1940
index,day12Series = DataFixture.day12Series[0]
day12Series = d.ConvertToNumpy(day12Series)
#d.CalculateEnergyForSeries(1000,day12Series) #6849
db = ''
#d.FindFirstRepeat(db,testData,3000) #2772
#db.close()
#db = dbm.open('cache', 'c') 
d.FindFirstRepeat(db,day12Series,2000000000)
#db.close()


    