class BT:
    #this will be our constructor
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def buildTree(self, data):
        if data == self.data:
            return
        # if the data inserted is less than cur value it'll
        # go into the left node
        if data < self.data:
            if self.left:
                self.left.buildTree(data)
            else:
                self.left = BT(data)
        # if the data is greater than the value
        # of the current node then it goes right
        else:
            if self.right:
                self.right.buildTree(data)
            else:
                self.right = BT(data)

    def findMinNode(self):
        if self.left is None:
            return self.data
        return self.left.findMinNode()

    def findMaxNode(self):
        if self.right is None:
            return self.data
        return self.right.findMaxNode()

        # this will first visit left node
        # then the root node and finally
        # the right node and display them in
        # specific order

    def inOrderTrav(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTrav()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTrav()
        return elements

    ''' 
    First it visits left node, right node, and then 
    root node
    '''

    def postOrderTrav(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTrav()
        if self.right:
            elements += self.right.postOrderTrav()

        elements.append(self.data)
        return elements

    def preOrderTrav(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preOrderTrav()
        if self.right:
            elements += self.right.preOrderTrav()

        return elements