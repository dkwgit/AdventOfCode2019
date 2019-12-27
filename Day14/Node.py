import math
from abc import ABC, abstractmethod

class Node(ABC):

    def __init__(self, tree, name, producedFromBranch, sentTowardRoot, token):
        self._tree = tree
        self._name = name
        self._receivesFromRule = producedFromBranch
        self._contributesToRule = sentTowardRoot
        self._branches = []
        self._parent = None
        self._token = token

    def IsRoot(self):
        return True if self._parent is None else False

    def IsBranch(self):
        return True if self._parent is not None else False

    def IsLeaf(self):
        return True if len(self._branches) == 0 else False

    def AddBranch(self,node):
        self._branches.append(node)
        node._parent = self

    def GetParent(self):
        return self._parent

    def GetName(self):
        return self._name

    def Visit(self):
        self._tree.ReportVisit(self)

    def Deduct(self):
        #do deduction, from the product bank
        onHand, totalProduced, demand = self._tree._productBank[self.GetName()]
        cycles = demand / self._contributesToRule
        onHand = onHand - (cycles * self._contributesToRule)
        demand = demand - (cycles * self._contributesToRule)
        self._tree._productBank[self.GetName()] = (onHand,totalProduced,demand)

    def Produce(self):
        if (self.NeedToProduce()):
            for b in self._branches:
                b.Produce()
                b.Deduct()
            onHand, totalProduced, demand = self._tree._productBank[self.GetName()]
            while (onHand < demand):
                onHand = onHand + self._receivesFromRule
                totalProduced = totalProduced + self._receivesFromRule
            self._tree._productBank[self.GetName()] = (onHand, totalProduced, demand)

    def GetOnHand(self):
         onHand, discard1, discard2 = self._tree._productBank[self.GetName()]
         return onHand

    def GetDemand(self):
         onHand, discard2, demand = self._tree._productBank[self.GetName()]
         return demand - onHand

    def NeedToProduce(self):
        onHand, totalProduced, demand = self._tree._productBank[self.GetName()]

        #In order to produce enough for the parent
        parentDemand = self._parent.GetDemand() if not self.IsRoot() else 0
        cyclesForParentNeed = 1 if parentDemand == 0 else math.ceil(parentDemand / self._parent._receivesFromRule)
        demand = demand + (cyclesForParentNeed * self._contributesToRule) 
        self._tree._productBank[self.GetName()] =  (onHand, totalProduced, demand)
        if (onHand >= demand):
            return False
        return True



