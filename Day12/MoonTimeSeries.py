from DataFixture import *
from itertools import combinations

class MoonTimeSeries:

    order = ['Io','Europa', 'Ganymede', 'Callisto']

    def GetChange(self, a, b):
        val = None
        if (a<b):
            val = 1
        elif (a>b):
            val = -1
        else:
            val = 0
        return val

    def ApplyGravityToTwoMoons(self, moon1, moon2):
        assert(moon1.moonName != moon2.moonName)
        xChange = self.GetChange(moon1.x, moon2.x)
        yChange = self.GetChange(moon1.y, moon2.y)
        zChange = self.GetChange(moon1.z, moon2.z)
        moon1 = VelocityChange(xChange,yChange,zChange,moon1.moonName)
        moon2 = VelocityChange(xChange * (-1),yChange * (-1),zChange * (-1),moon2.moonName)
        return (moon1, moon2)

    def ApplyGravityToAllMoons(self, positions, velocities):
        pointCombis = combinations(positions,2) #all pairs of moons
        pairVelocityChanges = {}
        for moonName in MoonTimeSeries.order:
            pairVelocityChanges[moonName] = []
        for moon1, moon2 in pointCombis:
            velocityChange1, velocityChange2 = self.ApplyGravityToTwoMoons(moon1, moon2)
            pairVelocityChanges[velocityChange1.moonName].append(velocityChange1)
            pairVelocityChanges[velocityChange2.moonName].append(velocityChange2)
        changes = []
        for moonName in pairVelocityChanges.keys():
            velocityChangeList = pairVelocityChanges[moonName]
            changes.append(VelocityChange(
                sum(map(lambda x: x.x,velocityChangeList)),
                sum(map(lambda x: x.y,velocityChangeList)),
                sum(map(lambda x: x.z,velocityChangeList)),
                moonName
            ))
        newVelocities = []
        for change,velocity in zip(changes,velocities):
            newVelocities.append(self.AddChangeToVelocity(change, velocity))
        return newVelocities

    def AddVelocityToPosition(self, position, velocity):
        return MoonPosition(
            position.x + velocity.x,
            position.y + velocity.y,
            position.z + velocity.z,
            position.moonName
        )

    def AddChangeToVelocity(self, change, velocity):
        return MoonVelocity(
            velocity.x + change.x,
            velocity.y + change.y,
            velocity.z + change.z,
            velocity.moonName
        )

    def ApplyVelocities(self, positions, velocities):
        newPositions = []
        for position,velocity in zip(positions,velocities):
            newPosition = self.AddVelocityToPosition(position,velocity)
            newPositions.append(newPosition)
        return newPositions

    def GetIterator(self, stepData, numberOfSteps):
        for step in range(numberOfSteps):
            nextStepData = []
            positions = list(map(lambda x : x.moonPosition, stepData))
            velocities = list(map(lambda x : x.moonVelocity, stepData))
            newMoonVelocities = self.ApplyGravityToAllMoons(positions,velocities)
            newMoonPositions = self.ApplyVelocities(positions,newMoonVelocities)
            for moonPosition, moonVelocity in zip(newMoonPositions,newMoonVelocities):
                assert(moonPosition.moonName == moonVelocity.moonName)
                nextStepData.append(MoonInfo(moonPosition,moonVelocity,moonPosition.moonName))
            stepData = nextStepData #to properly generate the next in series, this is the new input
            yield(nextStepData)

     