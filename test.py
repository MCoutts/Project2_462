from pycharmProjBinarySearch import BST, MergeTrees
from binarySort import BT


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


################
##TEST FOR BST##
################

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
print ("Before deleting node \n",listBST3.inOrderTrav())
listBST3.deleteNode(listBST3, 2)
print ("After deleting node \n",listBST3.inOrderTrav())
print("\n\n\n\n")
print (listBST3.inOrderTrav())

#listBST2.addBST(listBST3)
print("listBST2: \n", listBST3.inOrderTrav())
print("listBST3: \n", listBST3.inOrderTrav())
print("~~~~~~~~~~~~~~~~~~~~~~~\n")
mergedTree = MergeTrees(listBST2, listBST3)

print("Combined: \n", mergedTree.inOrderTrav())
# print("Tree combination: ", )
