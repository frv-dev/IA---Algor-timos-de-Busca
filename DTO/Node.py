class Node(object):
    def __init__(self, father = None, firstValue = None, secondValue = None, previousNode = None, nextNode = None):
        """
        Script node

        :type father: Node
        :type firstValue: NoneType
        :type secondValue: NoneType
        :type previousNode: Node
        :type nextNode: Node
        """
        self.father = father
        self.firstValue = firstValue
        self.secondValue = secondValue
        self.previousNode = previousNode
        self.nextNode = nextNode