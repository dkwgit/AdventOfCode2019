from DataFixture import *
from itertools import combinations
import numpy as np

class MoonTimeSeries:

    def GetMoonDataWithChangeArray(self, moon):
        return (moon[0],moon[1],np.array([[0,0,0]]))

    def GetChange(self, a, b):
        val = None
        if (a<b):
            val = 1
        elif (a>b):
            val = -1
        else:
            val = 0
        return val

    def ApplyGravityToTwoMoons(self, stepData, moon1Index, moon2Index, changes):
        xChange = self.GetChange(stepData[0][moon1Index][0], stepData[0][moon2Index][0])
        yChange = self.GetChange(stepData[0][moon1Index][1], stepData[0][moon2Index][1])
        zChange = self.GetChange(stepData[0][moon1Index][2], stepData[0][moon2Index][2])
        changes[moon1Index] = np.add(changes[moon1Index],np.array([[xChange,yChange,zChange]]))
        changes[moon2Index] = np.add(changes[moon2Index],np.array([[xChange*-1,yChange*-1,zChange*-1]]))

    def ApplyGravityToAllMoons(self, stepData):
        numMoons = np.shape(stepData[0])[0] #get the positions (1st element tuple, get the 1st axis (number of moons))
        #parallel array for accumulating velocity changes
        changes = np.zeros((4,3))
        pointCombis = combinations(range(numMoons),2) #all pairs of moons
        for moon1Index, moon2Index in pointCombis:
            self.ApplyGravityToTwoMoons(stepData,moon1Index, moon2Index, changes)
        #add the changes to velocity to the velocity component [1]
        stepData[1] = np.add(stepData[1],changes)
        #add the velocity component [1] to the position component [0]
        stepData[0] = np.add(stepData[0],stepData[1])
        return stepData

    def GetIterator(self, stepData, numberOfSteps):
        for step in range(numberOfSteps):
            nextStepData = self.ApplyGravityToAllMoons(stepData)
            stepData = nextStepData #to properly generate the next in series, this is the new input
            yield(nextStepData)

     