"""
Name:Matthew Coutts
Class: CMSPC 462 - FA 2020
Project 2 - Create a BT and a BST and implement functions
Date: October 15th, 2020
"""


import time  ##first we import the time function

# BSTtime = []  # this will hold our time for the function BST
# BT_Time = [] # this will hold our time for the function BT

class BST:
    # this is our constructor
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

    # insert func to insert the data according to it's amount
    def buildSTree(self, data):
        if data == self.data:
            return

        # if the data inserted is less than cur value itll
        # go into the left node
        if data < self.data:
            if self.left:
                self.left.buildSTree(data)
            else:
                self.left = BST(data)

        # if the data is greater than the value
        # of the current node then it goes right
        else:
            if self.right:
                self.right.buildSTree(data)
            else:
                self.right = BST(data)

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

    def findMinNode(self):
        if self.left is None:
            return self.data
        return self.left.findMinNode()

    def findMaxNode(self):
        if self.right is None:
            return self.data
        return self.right.findMaxNode()

    def deleteNode(self, current, value):
        if current == None: 
            return current
        elif value < current.data: 
            current.left = self.deleteNode(current.left,value)
        elif value > current.data: 
            current.right = self.deleteNode(current.right,value)
        else:
            if current.left == None and current.right == None:
                current = None # case 0
            elif current.left == None: 
                return current.right # case 1r
            elif current.right == None: 
                return current.left # case 1l
            else:  # case 2
                temp = self.min(current.right)
                current.data = temp
                current.right = self.deleteNode(current.right, temp)
        return current

    def PrintTree(self): ##print to see what values are in the tree
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    # def addBST(self, tree2):
    #     for e in tree2:
    #         self.buildSTree(e)
    #     return tree2

def MergeTrees(t1, t2): 
    if (not t1):  
        return t2  
    if (not t2): 
        return t1  
    t1.data += t2.data  
    t1.left = MergeTrees(t1.left, t2.left)  
    t1.right = MergeTrees(t1.right, t2.right)  
    return t1 