import Tree
from DataSource import DataSource as Source
from DataFixture import DataFixture as Fixture
import sys

# Day 6: https://adventofcode.com/2019/day/6

class Driver:
    def __init__(self,inputData):
        self.inputData = inputData
        self.trees = {}
        self.roots = []
    
    def Construct(self):
        for line in self.inputData:
            rootName, branchName = line.split(')')
            if branchName not in self.trees.keys():
                self.trees[branchName] = Tree.Tree(branchName)
            branchTree = self.trees[branchName]
            if rootName not in self.trees.keys():
                self.trees[rootName] = Tree.Tree(rootName)
            rootTree = self.trees[rootName]
            rootTree.insertBranch(branchTree)

        self.roots = self.FindRoots()
        assert(len(self.roots)==1)
        return self.trees[self.roots[0]]

    def FindRoots(self):
        roots = []
        for key in self.trees.keys():
            if (self.trees[key].root is None):
                roots.append(key)
        return roots  

    def FindLastCommonIndex(self, pathA, pathB):
        pathToTrace = pathA if len(pathA) <= len(pathB) else pathB
        otherPath = pathB if pathToTrace == pathA else pathA
        for index, name in enumerate(pathToTrace):
            if (pathA[index] != pathB[index]):
                return index - 1
        return index
            


testDataSource = Source(Fixture.testData)
testDriver = Driver(testDataSource)
testRoot = testDriver.Construct()
orbits = testRoot.CountOrbits(0, 0)
print(f"Number of orbits in test data set {orbits}")
assert(42 == orbits)

dataSource = Source(Fixture.mainData)
driver = Driver(dataSource)
root = driver.Construct()
count = root.CountOrbits(0,0)
print(f"Day 6-1. Number of orbits in main data set: {count}")

pathToSAN = root.GetPathToBranch('SAN',[])
assert(len(pathToSAN) == len(set(pathToSAN))) #test that path has integrity
pathToYOU = root.GetPathToBranch('YOU',[])
assert(len(pathToYOU) == len(set(pathToYOU))) #test that path has integrity
lastCommonIndex = driver.FindLastCommonIndex(pathToSAN, pathToYOU)
indexBeforeSAN = len(pathToSAN) - 2
indexBeforeYOU = len(pathToYOU) - 2
# number of hops from leaf A to common point + number of hops from common point to leaf B - 1 for the point in common
orbitalTransfers = indexBeforeSAN - lastCommonIndex + indexBeforeYOU - lastCommonIndex
print(f"Day 6-2. orbital transfers to get to Santa: {orbitalTransfers}")

sys.exit()