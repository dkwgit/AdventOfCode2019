class Tree:

    def __init__(self,productBank):
        self._root = None
        self._leaves = []
        self._rootVisitedFunc = None
        self._branchVisitedFunc = None
        self._leafVisitedFunc = None
        self._nodeVisitedFunc = None
        self._productBank = productBank

    def SetRoot(self, root):
        self._root = root

    def AddLeaf(self, node):
        self._leaves.append(node)

    def GetLeaves(self):
        return self._leaves

    def ReportVisit(self, node):
        if (self._nodeVisitedFunc is not None):
            self._nodeVisitedFunc(node)
        if (self._rootVisitedFunc is not None and node.IsRoot()):
            self._rootVisitedFunc(node)
        if (self._branchVisitedFunc is not None and node.IsBranch()):
            self._branchVisitedFunc(node)
        if (self._leafVisitedFunc is not None and node.IsLeaf()):
            self._leafVisitedFunc(node)

    def DoLevel(self, screenWidth, nodes):
        countNodes = len(nodes)
        widthOfNode = screenWidth // countNodes
        levelString = ""
        for n in nodes:
            if (n is not None):
                nodeString = "{}-{}: ({},{})".format(n.GetName(),n._token,n._contributesToRule,n._receivesFromRule)
            else:
                nodeString = "-"
            levelString = levelString + nodeString.center(widthOfNode)
        print(levelString)
        print("")
        print("")

    def PrintTree(self,screenWidth,nodes):
        self.DoLevel(screenWidth, nodes)
        children = []

        for n in nodes:
            if (n is not None and len(n._branches)>0):
                children.extend(n._branches)
            else:
                children.append(None)
        
        if (len([c for c in children if c is not None]) > 0):
            self.PrintTree(screenWidth,children)
        return





