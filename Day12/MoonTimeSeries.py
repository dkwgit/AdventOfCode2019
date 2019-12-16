from DataFixture import *
from itertools import combinations

class MoonTimeSeries:

    order = ['Io','Europa', 'Ganymede', 'Callisto']

    def ApplyGravityToTwoMoons(self, moon1, moon2):
        # gravity
        print(f"Combo: {moon1.moonName}, {moon2.moonName}")
        moon1 = MoonPosition(
            moon1.x + (1 if moon1.x < moon2.x else (-1 if moon1.x > moon2.x else 0)),
            moon1.y + (1 if moon1.y < moon2.y else (-1 if moon1.y > moon2.y else 0)),
            moon1.z + (1 if moon1.z < moon2.z else (-1 if moon1.z > moon2.z else 0)),
            moon1.moonName
        )
        moon2 = MoonPosition(
            moon2.x + (1 if moon2.x < moon1.x else (-1 if moon2.x > moon1.x else 0)),
            moon2.y + (1 if moon2.y < moon1.y else (-1 if moon2.y > moon1.y else 0)),
            moon2.z + (1 if moon2.z < moon1.z else (-1 if moon2.z > moon1.z else 0)),
            moon2.moonName
        )
        return (moon1, moon2)
            

    def ApplyGravityToAllMoons(self, positions):
        newPositions = [None] * len(positions)
        pointCombis = combinations(positions,2) #all pairs of moons
        for moon1, moon2 in pointCombis:
            # Get the already altered data for a moon if it exists
            moon1 = next((newPositions[i] for i, x in enumerate(newPositions) if x is not None and x.moonName == moon1.moonName), moon1)
            moon2 = next((newPositions[i] for i, x in enumerate(newPositions) if x is not None and x.moonName == moon2.moonName), moon2)

            moon1, moon2 = self.ApplyGravityToTwoMoons(moon1, moon2)
            newPositions[MoonTimeSeries.order.index(moon1.moonName)] = moon1
            newPositions[MoonTimeSeries.order.index(moon2.moonName)] = moon2
            
        return newPositions

    def ApplyVelocity(self, velocity):
        pass

    def GetIterator(self, stepData, numberOfSteps):
        for step in range(numberOfSteps):
            nextStepData = []
            positions = list(map(lambda x : x.moonPosition, stepData))
            velocities = list(map(lambda x : x.moonVelocity, stepData))
            moonPositions = self.ApplyGravityToAllMoons(positions)
            for moonPosition in moonPositions:
                nextStepData.append(MoonInfo(moonPosition,MoonVelocity(0,0,0,moonPosition.moonName),moonPosition.moonName))
            stepData = nextStepData
            yield(stepData)

     