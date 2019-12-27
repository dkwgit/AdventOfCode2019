from Node import Node as Node

class TerminalOperation(Node):

    def __init__(self, tree, name, producedFromBranch, sentTowardRoot, token):
            super().__init__(tree, name, producedFromBranch, sentTowardRoot, token)

    def Produce(self):
        assert(len(self._branches)==0)
        super().Produce()