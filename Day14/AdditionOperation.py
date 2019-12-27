from Node import Node as Node

class AdditionOperation(Node):

    def __init__(self, tree, name, producedFromBranch, sentTowardRoot, token):
            super().__init__(tree, name, producedFromBranch, sentTowardRoot, token)

    def Produce(self):
        assert(len(self._branches)>=2)
        super().Produce()



