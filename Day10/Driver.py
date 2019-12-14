from DataFixture import DataFixture as DataFixture
import math
from decimal import *


#https://adventofcode.com/2019/day/10
class Driver:

    getcontext().prec = 5
    pi = Decimal.from_float(math.pi)*Decimal(1)
    piHalf = Decimal.from_float(math.pi/2)*Decimal(1)
    piQuarter = Decimal.from_float(math.pi/4)*Decimal(1)
    negPi = Decimal.from_float(-math.pi)*Decimal(1)
    negPiHalf = Decimal.from_float(-math.pi/2)*Decimal(1)
    negPiQuarter = Decimal.from_float(-math.pi/4)*Decimal(1)

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

    def TestSortKeys(self):
        data = [
            ((0,-1), Driver.negPiHalf,                  8),
            ((1,-1), Driver.negPiQuarter,               7),
            ((1,0),  Decimal(0),                        6),
            ((1,1),  Driver.piQuarter,                  5),
            ((0,1),  Driver.piHalf,                     4),
            ((-1,1), Decimal(3)*Driver.piQuarter,       3),
            ((-1,0), Driver.pi,                         2),
            ((-1,-1),Decimal(3)*Driver.negPiQuarter,    1)
        ]
        for direction, angle, sortKey in data:
            assert(angle == Decimal.from_float(math.atan2(direction[1],direction[0]))*Decimal(1))
            result = self.GetSortKeyForClockwise(angle,direction)
            assert(result == sortKey)
        
    def GetSortKeyForClockwise(self,angle,direction):
        # Have to deal with non cartesian coords (upper left!), yet atan2(), which we are using for angles
        # works with cartesian. Also have to get the sorting of angles to give us a clockwise sort
        #
        # following shows directions in puzzle order and shows how those map to cartesian atan2
        #
        # direction 0,-1 (up,q1) => q3 in atan2 [-pi/2, -pi)
        # direction 1,-1 (up,right,q1) => q2 in atan2 [0, -pi/2)])
        # direction 1,0 (right, q2) => q2 in atan2 [0, -pi/2)
        # direction 1,1 (right,down,q2) => q1 in atan2 [pi/2, 0)
        # direction 0,1 (down,q3) => q1 in atan2 [pi/2, 0)
        # direction -1,1 (left,down,q3) => q4 in atan2 [pi, pi/2)
        # direction -1,0 (left,q4) => q4 in atan2 [pi, pi/2)
        # direction -1,-1 (left,up,q4) => q3 in atan2 [-pi/2, -pi)
        if (Driver.negPiHalf == angle):  # direction 0,-1
            sortKey = 8
        elif (0 > angle > Driver.negPiHalf): # direction 1,-1
            sortKey = 7
        elif (0 == angle): # direction 1,0
            sortKey = 6
        elif (Driver.piHalf > angle > 0): # direction 1,1
            sortKey = 5
        elif (Driver.piHalf == angle): # direction 0,1
            sortKey = 4
        elif (Driver.pi > angle > Driver.piHalf): #direction -1,1
            sortKey = 3
        elif (Driver.pi == angle): #direction -1,0
            sortKey = 2
        elif (Driver.negPiHalf > angle > Driver.negPi):
            sortKey = 1
        return sortKey

    def CalculatePointInfo(self, point1, point2):
        x1,y1 = point1
        x2,y2 = point2
        direction = (1 if x2 - x1 > 0 else -1 if x2 - x1 < 0 else 0, 1 if y2 - y1 > 0 else -1 if y2 - y1 < 0 else 0)

        vector = (x2 - x1, y2 - y1)
        #nonCartesianVector = vector
        #vector = self.ConvertVectorToCartesian(vector)
        #if (point1 == (29,28)):
        #    print(f"Vector {nonCartesianVector} converted to {vector}")

        angle = Decimal.from_float(math.atan2(vector[1],vector[0]))*Decimal(1)

        if (x1 != x2):
            distance = Decimal.from_float(math.sqrt(vector[0]**2 + vector[1]**2))*Decimal(1)
        else:
            distance = Decimal(abs(vector[1]))
       
        sortKey = self.GetSortKeyForClockwise(angle,direction)
        return (angle,distance,direction,vector,(point1,point2),sortKey)

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

    def GetClockWiseListOfAngles(self,otherAsteroids):
        output = []
        anglesBySortKey = {}
        for k in otherAsteroids.keys():
            sortKey = otherAsteroids[k][0][5]
            if (sortKey not in anglesBySortKey.keys()):
                anglesBySortKey[sortKey] = []
            anglesBySortKey[sortKey].append(k)
        for clockWiseStep in sorted(anglesBySortKey.keys(),reverse=True):
            angleList = sorted(map(lambda x: (x,clockWiseStep),list(set(anglesBySortKey[clockWiseStep]))),reverse=True)
            output.extend(angleList)
        return output

    def ZapAsteroids(self, otherAsteroids):

        zapCount = 0
        zappedAsteroidInfo = None
        while len(otherAsteroids) > 0:
            clockwiseList = self.GetClockWiseListOfAngles(otherAsteroids)
            for angle,clockWiseStep in clockwiseList:
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

getcontext().prec = 5
d = Driver()
d.DoTests()
numberOfAsteroidsInSight,candidate,otherDict = d.FindBestCandidate(DataFixture.mainData)
print(f"Best asteroid found {candidate}, with {numberOfAsteroidsInSight} asteroids detected compared to expected.")
d.TestSortKeys()
d.ZapAsteroids(otherDict)