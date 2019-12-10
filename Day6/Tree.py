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
            self.branches[branchName] = branchTree
            self.isLeaf = False

    def CountOrbits(self, segmentCount, segmentsToCountBack):
        """
        Counts the total orbits according to orbit checksome method at
        Day 6: https://adventofcode.com/2019/day/6
        
        In essence, if there is a root planet R, and three planets A, which orbits R, and B which orbits A and 
        indirectly R, and C which orbits B and indirectly A and R, the checksum is:
        1 orbit for A around R + 2 orbits for B (around A and R) + 3 orbits for C (around B and A and R).
        Thus from the vantage point of C, the orbit check sum C expresses is 3 + 2 + 1.
        Which is numbger of path segment from C, plus the number of path segments from B plus the number of path
        segment from A to R.

        This approach handles a tree structure with arbitrary branching, away from a root planet orbited 
        directly or indirectly by all others. However, care must be taken not to double count path segments.
        If two or more branches share some amount of path segments before a branching point, only one of the branches
        can be allowed to apply count all the segment combos in its count.  The other paths must only 
        count the segment combos unique to their branch.

        In the below this is accomplished by using the 0th (think left most) branch for 
        full path segment combo counting back to the absolute root planet.  All other branches can only count their
        unique segment combo contributions back to the branching point.
        
        If branchNum == 0, and it's a branch with five path segments to root we count back all segment combos
        (example: 5,4,3,2,1).
        If branchNum == 1, and the branch has six path segments to root, and the divergent branching point was planet 2, 
        since branch 0 already handled 2 and 1 segments in its counts, the we can only count 6,5,4,3, 
        but not 2,1 for branch 1.

        The variable segmentsToCountBack is how we keep track of how far back to a branching point to go on branches.
        segmentsToCountBack = segmentCount for 0th branch, and only as many segments as go back to branching point
        for non 0th branch (segmentsToCountBack == unique segments from branch point AND 
        segmentsToCountBack < segmentCount).
        """
        sum = 0
        if (self.isLeaf != True):
            branchNum = 0
            for branchName in self.branches.keys():
                if (branchNum == 0):
                    sum = sum + self.branches[branchName].CountOrbits(segmentCount + 1, segmentsToCountBack + 1)
                else:
                    sum = sum + self.branches[branchName].CountOrbits(segmentCount + 1, 1)
                branchNum = branchNum + 1
            return sum
        else:
            current = segmentCount
            while current > segmentCount - segmentsToCountBack:
                sum = sum + current
                current = current - 1
            return sum

    def GetPathToBranch(self, name, path):
        path.append(self.name)
        
        if (self.name == name):
            return path
        
        if (self.isLeaf != True):
            for branchName in self.branches.keys():
                path = self.branches[branchName].GetPathToBranch(name,path)
                if (path[-1] != name):
                    path.pop()
            return path
        else:
            return path