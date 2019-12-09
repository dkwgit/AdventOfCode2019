# Day 6: https://adventofcode.com/2019/day/6

class Tree:
    def __init__(self, name):
        self.root = None
        self.isLeaf = True
        self.branches = {}
        self.name = name

    def insertBranch(self, branchTree):
        branchName = branchTree.name
        if (branchName not in self.branches.keys()):
            branchTree.root = self
            self.branches.branchName = branchTree
            self.isLeaf = False