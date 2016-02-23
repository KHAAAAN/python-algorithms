class Node:
    def __init__(self, value):
        self.value = value

class ExpNode(Node):
    def __init__(self, value):
        Node.__init__(self, value) 

class NumNode(ExpNode):
    def __init__(self, value):
        ExpNode.__init__(self, value)
        self.type = 'num'

class OpNode(ExpNode):
    def __init__(self, value):
        ExpNode.__init__(self, value)
        self.type = 'op'

class BinaryTree:
    def __init__(self):
        self.root = Node()
        self.left = None
        self.right = None

class ExpressionTree(BinaryTree):
    def __init__(self):
        self.root = ExpNode()
        self.left = None
        self.right = None

    
        
