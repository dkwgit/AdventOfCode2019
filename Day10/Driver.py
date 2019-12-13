from DataFixture import DataFixture as DataFixture
import math

#https://adventofcode.com/2019/day/10
class Driver:

    def DoTests(self):
        tests = [
            DataFixture.test1,
            DataFixture.test2,
            DataFixture.test3,
            DataFixture.test4,
            DataFixture.test5
        ]
        for index, t in enumerate(tests):
            mapData, bestLocation, numberDetected = t
            candidate = self.FindBestCandidate(mapData)
            print(f"Test map {index + 1}, candidate asteroid found {candidate[1]}, with {candidate[0]} asteroids detected compared to expected: {bestLocation} with {numberDetected} asteroids detected.")
            assert(candidate[1]==bestLocation)
    
    def FindBestCandidate(self,mapData):
        asteroids = self.ReadMap(mapData.strip())
        candidates = []
        for candidate in asteroids:
            others = list(set(asteroids) - set([candidate]))
            otherDict = {}
            for o in others:
                otherInfo = self.CalculatePointInfo(candidate,o)
                angleKey = str(otherInfo[0]) #+ '_' + str(otherInfo[2])
                if (angleKey not in otherDict.keys()):
                    otherDict[angleKey] = []
                    otherDict[angleKey].append(otherInfo)
            for k in otherDict.keys():
                lineOfAsteroids = otherDict[k]
                lineOfAsteroids.sort(key=lambda x: x[1])
                otherDict[k] = lineOfAsteroids
            candidates.append((len(otherDict.keys()),candidate,otherDict))
        candidates.sort(reverse=True)
        result = (numberOfAsteroidsInSight,candidate,otherDict) = candidates[0][0],candidates[0][1],candidates[0][2]
        return result

    def CalculatePointInfo(self, point1, point2):
        x1,y1 = point1
        x2,y2 = point2
        vector = (x2 - x1, y2 - y1)
        angle = math.atan2(vector[1],vector[0])
        angle = round(angle,5)
        direction = (1 if x2 - x1 > 0 else -1 if x2 - x1 < 0 else 0, 1 if y2 - y1 > 0 else -1 if y2 - y1 < 0 else 0)
        if (x1 != x2):
            distance = math.sqrt(vector[0]**2 + vector[1]**2)
        else:
            distance = abs(vector[1])
        distance = round(distance,5)
        return (angle,distance,direction,vector,(point1,point2))

    def ReadMap(self,mapData):
        x = 0
        y = 0
        asteroids = []
        for line in mapData.split():
            for ch in line:
                if (ch == '#'):
                    asteroids.append((x,y))
                x = x + 1
            x = 0
            y = y + 1
        return asteroids

    def ZapAsteroids(self, otherAsteroids):
        quad3 = lambda x: ((-1) * math.pi / 2) >= x > ((-1) * math.pi)
        quad4 = lambda x: (math.pi) >= x > (math.pi / 2)
        rightHemi = lambda x: (math.pi / 2) >= x > ((-1) * math.pi /  2)

        leftHemi = lambda x: not rightHemi(x)

        zapCount = 0
        zappedAsteroidInfo = None
        while len(otherAsteroids) > 0:
            firstHalfOfList = [i for i in otherAsteroids.keys() if rightHemi(float(i)) == True]
            firstHalfOfList.sort(key = lambda x: float(x), reverse = True)
            quad3List = [i for i in otherAsteroids.keys() if quad3(float(i)) == True]
            quad4List = [i for i in otherAsteroids.keys() if quad4(float(i)) == True]
            quad3List.sort(key = lambda x: float(x), reverse = True)
            quad4List.sort(key = lambda x: float(x), reverse = True)
            clockwiseList = []
            clockwiseList.extend(firstHalfOfList)
            clockwiseList.extend(quad3List)
            clockwiseList.extend(quad4List)
            assert(len(clockwiseList)==len(otherAsteroids))
            assert(
                (set(otherAsteroids.keys()) & set(clockwiseList))==set(otherAsteroids.keys())
            )
            for angle in clockwiseList:
                lineOfAsteroids = otherAsteroids[angle]
                zappedAsteroidInfo = lineOfAsteroids.pop(0)
                if (len(lineOfAsteroids)<=0):
                    del otherAsteroids[angle]
                else:
                    otherAsteroids[angle] = lineOfAsteroids
                zapCount = zapCount + 1
                if (zapCount == 200):
                    point = zappedAsteroidInfo[4][1]
                    print(f"200th asteroid zapped is {point}, with 100x+y = {100*point[0]+point[1]}")

d = Driver()
d.DoTests()
numberOfAsteroidsInSight,candidate,otherDict = d.FindBestCandidate(DataFixture.mainData)
print(f"Best asteroid found {candidate}, with {numberOfAsteroidsInSight} asteroids detected compared to expected.")
d.ZapAsteroids(otherDict)