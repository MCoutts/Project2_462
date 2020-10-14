"""
Name:Matthew Coutts
Class: CMSPC 462 - FA 2020
Project 2 - Create a BT and a BST and implement functions
Date: October 15th, 2020
"""
from big_o import big_o


import time  ##first we import the time function

BSTtime = []  # this will hold our time for the function BST
BT_Time = [] # this will hold our time for the function BT

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

listTree= [ 2, 4, 22, 34, 9, 6, 67, 42, 55, 70, 120, 99, 200]
listBT = BT(6) ## BT will not be created unless data is given as param

for e in listTree: #this puts all the elements in listTree into the tree
    listBT.buildTree(e)
print("Binary Tree \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|||\t\tExample1\t\t|||")
print("Maximum node in BT: \n", listBT.findMaxNode())
print("Minimum node in BT: \n",listBT.findMinNode())
print("Post Order: \n", listBT.postOrderTrav())
print("Pre Order: \n", listBT.preOrderTrav())
print("In Order: \n", listBT.inOrderTrav())

listTree2= [ 5,6,7,8,9,10,22,600,2]
listBT2 = BT(3) ## BT will not be created unless data is given as param

for e in listTree2: #this puts all the elements in listTree into the tree
    listBT2.buildTree(e)
print(" \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|||\t\tExample2\t\t|||")
print("Maximum node in BT: \n", listBT2.findMaxNode())
print("Minimum node in BT: \n",listBT2.findMinNode())
print("Post Order: \n", listBT2.postOrderTrav())
print("Pre Order: \n", listBT2.preOrderTrav())
print("In Order: \n", listBT2.inOrderTrav())

listTree3= [ 10,2,7,8,9,2,3,3,5,6,999]
listBT3 = BT(9) ## BT will not be created unless data is given as param

for e in listTree3: #this puts all the elements in listTree into the tree
    listBT3.buildTree(e)
print(" \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|||\t\tExample3\t\t|||")
print("Maximum node in BT: \n", listBT3.findMaxNode())
print("Minimum node in BT: \n",listBT3.findMinNode())
print("Post Order: \n", listBT3.postOrderTrav())
print("Pre Order: \n", listBT3.preOrderTrav())
print("In Order: \n", listBT3.inOrderTrav())



class BST:
    # this is our constructor
    def __init__(self, data):
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

    def deleteNode(self, data, val):
        if self is None:                                ##none is left and right val
            return self
        if data < self.data:                             #if input is less than current
            self.left = deleteNode(self.left, data)  #go to the left node
        elif (data > self.data):                         #if input is higher, go to right node
            self.right = deleteNode(self.right, data)
        else:
            if self.left is None:
                temp = self.right                       #if left is none then assign temp to right
                self.left = None
                return temp
            elif self.right is None:                    #if right is none, assign temp to left
                temp = self.left
                self.left = None
                return temp

            temp = findMinNode(self.right)          ##node with two children, get the smallest right subtree
            self.data = temp.data                   ##copy the right small subtree
            self.right = deleteNode(self.right, temp.data)  #delete smallest right subtree
        return self

    def PrintTree(self): ##print to see what values are in the tree
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def addBST(self, tree2):
        for e in tree2:
            self.buildSTree(e)
        return tree2

listBST1 = BST(2)
l2 = [6, 4, 22, 9, 6, 42, 34, 55, 70, 99, 67,200,120]
for e in l2:
    listBST1.buildSTree(e)
print("\nBinary Search Tree \n ~~~~~~~~~~~~~~~~~~~~")
print("Post Order: \n", listBST1.postOrderTrav())
print("Pre Order: \n", listBST1.preOrderTrav())
print("In Order: \n", listBST1.inOrderTrav())
print("Max node in BST: \n", listBST1.findMaxNode())
print("Min node in BST: \n", listBST1.findMinNode())

listBST2 = BST(2)
l2 = [6, 4, 22, 9, 6, 42, 34, 55, 70, 99, 67,200,120]
for e in l2:
    listBST2.buildSTree(e)
print("\nBinary Search Tree \n ~~~~~~~~~~~~~~~~~~~~")
print("Post Order: \n", listBST2.postOrderTrav())
print("Pre Order: \n", listBST2.preOrderTrav())
print("In Order: \n", listBST2.inOrderTrav())
print("Max node in BST: \n", listBST2.findMaxNode())
print("Min node in BST: \n", listBST2.findMinNode())

print("~~~~~~~~~~~~~~~~~~~~~~~\n")
print("|||\t\tExample3\t\t|||")
##creating a new tree
deleteTree = [2,3,4,5,6,7]
listBST3 = BST(1)
for e in deleteTree:
    listBST3.buildSTree(e)
print("Maximum node in BT: \n", listBST3.findMaxNode())
print("Minimum node in BT: \n",listBST3.findMinNode())
print("Post Order: \n", listBST3.postOrderTrav())
print("Pre Order: \n", listBST3.preOrderTrav())
print("In Order: \n", listBST3.inOrderTrav())
listBST3.deleteNode(1)
print (listBST3.inOrderTrav())
listBST2.addBST(listBST3)
print("Tree combination: ", )

