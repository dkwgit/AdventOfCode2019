from Day14DataFixture import Day14DataFixture as Day14DataFixture
from Node import Node as Node
from DoubleDirectionTree import DoubleDirectionTree as DoubleDirectionTree

class Day14Driver:

    def __init__(self):
        self._products = {}
        self._tree = None
        self._productionBank = {}

    # Get data into form [(10,A),(7,B)] and associates that array with its product, which is keyed into a dict
    def ProcessRawInput(self, rawInput):
        a = rawInput.strip().split("\n")
        for line in a:
            inputs, product = line.split('=>')
            inputs = inputs.strip()
            inputs = inputs.split(",")
            producers = []
            for i in inputs:
                quantity, producer = i.strip().split(" ")
                producers.append((int(quantity.strip()),producer.strip()))
            product = product.strip()
            quantifier,product  = product.split(' ')
            self._products[product.strip()] = (int(quantifier.strip()),producers)

    def Run(self,rawData,target,source):
        self.ProcessRawInput(rawData)
        self._tree = DoubleDirectionTree()
        self._tree.SetRoot(self.InsertIntoTree(self._tree,target,None))
        
        def NodeVisitorFunc(node):
            NodeVisitorFunc.productionBank = self._productionBank
            nodeName = node.GetName()
            if (nodeName not in NodeVisitorFunc.productionBank.keys()):
                NodeVisitorFunc.productionBank[nodeName] = (0,0)

        self._tree._nodeVisitedFunc = NodeVisitorFunc

        oreNeeded = self.CalculateOre(self._tree)
        print(f"Ore needed for 1 fuel: {oreNeeded}")

    def ProduceOrRelyOnBank(self,node):
        parent = node.GetRoot()
        parentOnHand,parentTotalProduced = self._productionBank[parent.GetName()]
        if (parentOnHand < parent._sentTowardRoot):
            onHand, totalProduced =  self._productionBank[node.GetName()]
            self._productionBank[node.GetName()] = (onHand, totalProduced + node._sentTowardRoot)
            self._productionBank[parent.GetName()] = (parentOnHand+parent._producedFromBranch,parentTotalProduced + parent._producedFromBranch)

    def EvaluateParent(self, node):
        currentNode = node.GetRoot()
        if (currentNode.IsRoot()==False):
            onHand, totalProduced =  self._productionBank[currentNode.GetName()]
            self._productionBank[currentNode.GetName()] = (onHand - currentNode._sentTowardRoot,totalProduced)
        if (currentNode.IsRoot()==False and currentNode.GetRoot().IsRoot()==False):
            parentOnHand, parentTotalProduced =  self._productionBank[currentNode.GetRoot().GetName()]
            self._productionBank[currentNode.GetRoot().GetName()] = \
                (parentOnHand + currentNode.GetRoot()._sentTowardRoot, parentTotalProduced +currentNode.GetRoot()._sentTowardRoot)

        if (currentNode.IsRoot() == False):
            self.EvaluateParent(currentNode)
            return
        else:
            return

    def LeavesToRoots(self):
        leaves = self._tree.GetLeaves()
        for leaf in leaves:
            self.ProduceOrRelyOnBank(leaf)
            self.EvaluateParent(leaf)          

    def RootToLeaves(self,node,quantityNeeded):
        node.Visit()
        totalQuantityNeeded = 0
        if (len(node._branches)==0):
            return quantityNeeded
        for b in node._branches:
            totalQuantityNeeded = totalQuantityNeeded + self.RootToLeaves(b, b._producedFromBranch)
        return totalQuantityNeeded

    def CalculateOre(self,tree):
        maxOre = self.RootToLeaves(tree._root, tree._root._producedFromBranch)
        self.LeavesToRoots()
        (onHand,totalProduced) = self._productionBank['ORE']
        return totalProduced

    def InsertIntoTree(self,tree,nodeName,sentTowardRoot):
        if (nodeName in self._products.keys()):
            (producedFromBranch, branches) = self._products[nodeName]
        else:
            producedFromBranch = sentTowardRoot
            branches = []
        
        if (sentTowardRoot is None):
            sentTowardRoot = producedFromBranch

        node = Node(tree,nodeName,producedFromBranch,sentTowardRoot)

        if (len(branches)==0):
            tree.AddLeaf(node)

        for b in branches:
            branchNode = self.InsertIntoTree(tree,b[1],b[0])
            node.AddBranch(branchNode)

        return node

d = Day14Driver()
d.Run(Day14DataFixture.test1,'FUEL','ORE')
