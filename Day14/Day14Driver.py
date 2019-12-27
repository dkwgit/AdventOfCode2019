from Day14DataFixture import Day14DataFixture as Day14DataFixture
from Node import Node as Node
from Tree import Tree as Tree
from AdditionOperation import AdditionOperation as AdditionOperation
from UnaryOperation import UnaryOperation as UnaryOperation
from TerminalOperation import TerminalOperation as TerminalOperation
import math

class Day14Driver:

    def __init__(self):
        self._products = {}
        self._tree = None
        self._productBank = {}

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
        self._tree = Tree(self._productBank)
        self._tree.SetRoot(self.InsertIntoTree(self._tree,target,None))
        
        def NodeVisitorFunc(node):
            NodeVisitorFunc.productionBank = self._productBank
            nodeName = node.GetName()
            if (nodeName not in NodeVisitorFunc.productionBank.keys()):
                NodeVisitorFunc.productionBank[nodeName] = (0,0,0)

        self._tree._nodeVisitedFunc = NodeVisitorFunc

        #self._tree.PrintTree(200, [self._tree._root])
        self.TraverseOnce(self._tree._root)

        oreNeeded = self.CalculateOre(self._tree)
        print(f"Ore needed for 1 fuel: {oreNeeded}") 

    def TraverseOnce(self,node):
        node.Visit()
        if (len(node._branches)==0):
            return
        for b in node._branches:
            self.TraverseOnce(b)
        return

    def CalculateOre(self,tree):
        tree._root.Produce()
        (onHand,totalProduced,demand) = self._productBank['ORE']
        return totalProduced

    def InsertIntoTree(self,tree,nodeName,sentTowardRoot):
        if (nodeName in self._products.keys()):
            (producedFromBranch, branches) = self._products[nodeName]
        else:
            producedFromBranch = sentTowardRoot
            branches = []
        
        if (sentTowardRoot is None):
            sentTowardRoot = producedFromBranch

        node = None
        if (len(branches)==0):
            token = 'terminal'
            node = TerminalOperation(tree, nodeName, producedFromBranch,sentTowardRoot, token)
        elif (len(branches)==1):
            token = 'unary'
            node = UnaryOperation(tree, nodeName, producedFromBranch,sentTowardRoot, token)
        else:
            token = 'add'
            node = AdditionOperation(tree,nodeName,producedFromBranch,sentTowardRoot, token)

        node = Node(tree,nodeName,producedFromBranch,sentTowardRoot, token)

        if (len(branches)==0):
            tree.AddLeaf(node)

        for b in branches:
            branchNode = self.InsertIntoTree(tree,b[1],b[0])
            node.AddBranch(branchNode)

        return node

d = Day14Driver()
d.Run(Day14DataFixture.test1,'FUEL','ORE')  # should produce 1 FUEL with 31 ORE
d = Day14Driver()
d.Run(Day14DataFixture.test2,'FUEL','ORE')  # 165 ORE
d = Day14Driver()
d.Run(Day14DataFixture.test3,'FUEL','ORE')  # 13312 ORE
d = Day14Driver()
d.Run(Day14DataFixture.test4,'FUEL','ORE')  # 180697 ORE
d = Day14Driver()
d.Run(Day14DataFixture.test5,'FUEL','ORE')  # 2210736 ORE
d = Day14Driver()
d.Run(Day14DataFixture.mainDay14_1,'FUEL','ORE')


