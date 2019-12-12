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
                angleKey = str(otherInfo[0])+'_'+str(otherInfo[2])
                if (angleKey not in otherDict.keys()):
                    otherDict[angleKey] = [otherInfo]
                else:
                    otherDict[angleKey].append(otherInfo)
            candidates.append((len(otherDict.keys()),candidate))
        candidates.sort(reverse=True)
        return candidates[0]

    def CalculatePointInfo(self, point1, point2):
        x1,y1 = point1
        x2,y2 = point2
        if (x1 != x2):
            slope = (y2 - y1) / (x2 - x1)
            angle = math.atan(slope)
        else:
            angle = math.pi / 2   #90 degrees in radians
        angle = round(angle,6)
        vector = (x2 - x1, y2 - y1)
        direction = (1 if x2 - x1 > 0 else -1 if x2 - x1 < 0 else 0, 1 if y2 - y1 > 0 else -1 if y2 - y1 < 0 else 0)
        if (x1 != x2):
            distance = math.sqrt(vector[0]**2 + vector[1]**2)
        else:
            distance = abs(vector[1])
        distance = round(distance, 4)
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


d = Driver()
d.DoTests()
best = d.FindBestCandidate(DataFixture.mainData)
print(f"Best asteroid found {best[1]}, with {best[0]} asteroids detected compared to expected.")