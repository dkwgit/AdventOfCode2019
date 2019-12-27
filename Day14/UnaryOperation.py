from Node import Node as Node

class UnaryOperation(Node):

    def __init__(self, tree, name, producedFromBranch, sentTowardRoot, token):
            super().__init__(tree, name, producedFromBranch, sentTowardRoot, token)

    def Produce(self):
        assert(len(self._branches)==1)
        super().Produce()