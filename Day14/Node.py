class Node:

    def __init__(self, tree, name, producedFromBranch, sentTowardRoot):
        self._tree = tree
        self._name = name
        self._producedFromBranch = producedFromBranch
        self._sentTowardRoot = sentTowardRoot
        self._branches = []
        self._root = None

    def IsRoot(self):
        return True if self._root is None else False

    def IsBranch(self):
        return True if self._root is not None else False

    def IsLeaf(self):
        return True if len(self._branches) == 0 else False

    def AddBranch(self,node):
        self._branches.append(node)
        node._root = self

    def GetRoot(self):
        return self._root

    def GetName(self):
        return self._name

    def Visit(self):
        self._tree.ReportVisit(self)