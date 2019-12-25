class DoubleDirectionTree:

    def __init__(self):
        self._root = None
        self._leaves = []
        self._rootVisitedFunc = None
        self._branchVisitedFunc = None
        self._leafVisitedFunc = None
        self._nodeVisitedFunc = None

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
