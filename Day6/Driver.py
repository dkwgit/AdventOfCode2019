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
print(f"Number of orbits in main data set {count}")

sys.exit()