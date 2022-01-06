'''
File: BST.py
Author: Joshua Jacobs-Rebhun
Date: January 1, 2022

This file implements a binary search tree data structure.
'''


class Node:

    # default constructor creates empty node
    def __init__(self):
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.value = None
    

    # constructor creates node with value but no children
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.parent = None
    

    # constructor creates node with value and children
    def __init__(self, value, parent, leftChild, rightChild):
        self.value = value
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
    

    # copy constructor creates new node that is copy of old node
    def __init__(self, node):
        self.value = node.value
        self.parent = node.parent
        self.leftChild = node.leftChild
        self.rightChild = node.rightChild
    

    def __str__(self):
        return "Value: " + str(self.value)
    

    def getLeftChild(self):
        return self.leftChild
    

    def getRightChild(self):
        return self.rightChild
    
    def isRoot(self):
        return self.parent is None
    
    def isLeaf(self):
        return self.getRightChild() is None and self.getLeftChild() is None


    def isLeftChild(self):

        if self.parent is None:
            return False
        else:
            parentLeftChild = self.parent.getLeftChild()
            
            return parentLeftChild is self
    

    def isRightChild(self):
        
        if self.parent is None:
            return False
        else:
            parentRightChild = self.parent.getRightChild()
            
            return parentRightChild is self
    


class BinarySearchTree:
    
    # default constructor creates empty BST
    def __init__(self):
        self.root = None
    
    # create a new BST with node containing value as root
    def __init(self, value):
        self.root = Node(value)
    

    # checks the rep invariant of the data structure
    def __checkRep(self, node):
        pass
    

    # private insert method implements the actual insertion of nodes.
    # public insert method is simply a wrapper method that provides a nice
    # interface for the user
    def __insert(self, value, node):
        
        if value <= node.value:
            if node.getLeftChild() is not None:
                self.__insert(value, node.getLeftChild())
            else:
                nodeToInsert = Node(value)
                nodeToInsert.parent = node
                node.leftChild = nodeToInsert
        
        else:
            if node.getRightChild() in not None:
                self.__insert(value, node.getRightChild())
            else:
                nodeToInsert = Node(value)
                nodeToInsert.parent = node
                node.rightChild = nodeToInsert

    # insert a value into the tree
    def insert(self, value):
        
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert(value, self.root)
    

    # private get method gets the desired value recursively. This method
    # actually implements the functionality and the public get method simply
    # provides a user-friendly interface
    def __get(self, value, node):
        
        if value == node.value:
            return node
        
        elif value < node.value:
            if node.getLeftChild() is not None:
                return self.__get(value, node.getLeftChild())
            else:
                return None
        
        else:
            if node.getRightChild() is not None:
                return self.__get(value, node.getRightChild())
            else:
                return None

    # get a value from the tree
    def get(self, value):
        
        if self.root is None:
            return None
        else:
            return self.__get(value, self.root)
    

    # private get largest recursively finds largest value
    def __max(self, node, returnNode=False):
        if node.getRightChild() is None:
            if returnNode:
                return node
            else:
                return node.value
        else:
            return self.__max(node.getRightChild(), returnNode)

    # get the largest value
    def max(self, returnNode=False):
        
        if self.root is None:
            return None
        
        else:
            return self.__max(self.root, returnNode)
    

    # private get smallest method recursively finds the smallest element
    def __min(self, node, returnNode=False):
        if node.getLeftChild() is None:
            if returnNode:
                return node
            else:
                return node.value
        else:
            return self.__min(node.getLeftChild(), returnNode)

    # get the smallest value
    def min(self, returnNode=False):
        
        if self.root is None:
            return None
        
        else:
            return self.__min(self.root, returnNode)
        

    # implements the recursion for getting next larger element
    def __getOneLarger(self, node):
        
        if node.isRoot():
            return None
        elif node.isLeftChild():
            return node.parent.value
        else:
            return self.__getOneLarger(node.parent)

    # get the value of the next largest element in the tree
    def getOneLarger(self, value):

        # find the node in the tree
        node = self.get(value)

        # if node not found, then raise error
        if node is None:
            raise Exception("Value not in tree.")
        

        if node.getRightChild() is not None:
            return self.__min(node.getRightChild())
        else:
            return __getOneLarger(node)
    

    # implements the recursion for getting the next smaller element
    def __getOneSmaller(self, node):
        
        if node.isRoot():
            return None
        elif node.isRightChild():
            return node.parent.value
        else:
            return self.__getOneSmaller(node.parent)

    # gets the next smallest element in the tree
    def getOneSmaller(self, value):
        
        node = self.get(value)

        if node is None:
            raise Exception("Value not in tree")
        
        if node.getLeftChild() is not None:
            return self.__max(node.getLeftChild())
        else:
            return self.__getOneSmaller(node)


    
    # public remove method provides user-friendly interface
    def delete(self, value):
        
        node = self.get(value)

        if node is None:
            raise Exception("Value not in tree.")
        

        if node.isLeaf():
            if node.isLeftChild():
                node.parent.leftChild = None
                node.parent = None
            elif node.isRightChild():
                node.parent.rightChild = None
                node.parent = None
            elif node is self.root:
                self.root = None
            else:
                raise Exception("Oops! Something went wrong!")
            
            return node.value
        
        elif node.getLeftChild() is None:
            if node.isLeftChild():
                node.parent.leftChild = node.getRightChild()
                node.getRightChild().parent = node.parent
                node.parent = None
                node.rightChild = None
            elif node.isRightChild():
                node.parent.rightChild = node.getRightChild()
                node.getRightChild().parent = node.parent
                node.parent = None
                node.rightChild = None
            elif node is self.root:
                self.root = node.getRightChild()
                node.getRightChild().parent = None
                node.rightChild = None
            else:
                raise Exception("Oops! Something went wrong!")
            
            return node.value
        
        elif node.getRightChild() is None:
            if node.isLeftChild():
                node.parent.leftChild = node.getLeftChild()
                node.getLeftChild().parent = node.parent
                node.parent = None
                node.leftChild = None
            elif node.isRightChild():
                node.parent.rightChild = node.getLeftChild()
                node.getLeftChild().parent = node.parent
                node.parent = None
                node.leftChild = None
            elif node is self.root:
                self.root = node.getLeftChild()
                node.getLeftChild().parent = None
                node.leftChild = None
            else:
                raise Exception("Oops! Something went wrong!")
            
            return node.value
        
        else:
            nodeToReplace = self.__max(node.getLeftChild(), True)
            nodeVal = node.value
            node.value = nodeToReplace.value
            
            if nodeToReplace.isLeftChild():
                if nodeToReplace.isLeaf():
                    nodeToReplace.parent.leftChild = None
                    nodeToReplace.parent = None
                else:
                    nodeToReplace.parent.leftChild = nodeToReplace.getLeftChild()
                    nodeToReplace.getLeftChild().parent = nodeToReplace.parent
                    nodeToReplace.leftChild = None
                    nodeToReplace.parent = None
            
            else:
                if nodeToReplace.isLeaf():
                    nodeToReplace.parent.rightChild = None
                    nodeToReplace.parent = None
                else:
                    nodeToReplace.parent.rightChild = nodeToReplace.getLeftChild()
                    nodeToReplace.getLeftChild().parent = nodeToReplace.parent
                    nodeToReplace.parent = None
                    nodeToReplace.leftChild = None
            

            return nodeVal
    

    def __traverse(node, nodeFunction, traverseOrder):

        if traverseOrder == 'inorder':
            if node.isLeaf():
                nodeFunction(node)
            elif node.getLeftChild() is None:
                nodeFunction(node)
                self.__traverse(node.getRightChild(), nodeFunction, traverseOrder)
            elif node.getRightChild() is None:
                self.__traverse(node.getLeftChild(), nodeFunction, traverseOrder)
                nodeFunction(node)
            else:
                self.__traverse(node.getLeftChild(), nodeFunction, traverseOrder)
                nodeFunction(node)
                self.__traverse(node.getRightChild(), nodeFunction, traverseOrder)

        elif traverseOrder == 'preorder':
            if node.isLeaf():
                nodeFunction(node)
            elif node.getLeftChild() is None:
                nodeFunction(node)
                self.__traverse(node.getRightChild(), nodeFunction, traverseOrder)
            elif node.getRightChild() is None:
                nodeFunction(node)
                self.__traverse(node.getLeftChild(), nodeFunction, traverseOrder)
            else:
                nodeFunction(node)
                self.__traverse(node.getLeftChild(), nodeFunction, traverseOrder)
                self.__traverse(node.getRightChild(), nodeFunction, traverseOrder)
        
        elif traverseOrder == 'postorder':
            if node.isLeaf():
                nodeFunction(node)
            elif node.getLeftChild() is None:
                self.__traverse(node.getRightChild(), nodeFunction, traverseOrder)
                nodeFunction(node)
            elif node.getRightChild() is None:
                self.__traverse(node.getLeftChild(), nodeFunction, traverseOrder)
                nodeFunction(node)
            else:
                self.__traverse(node.getLeftChild(), nodeFunction, traverseOrder)
                self.__traverse(node.getRightChild(), nodeFunction, traverseOrder)
                nodeFunction(node)

        else:
            raise Exception("Not a valid order of traversal. Options are: inorder, preorder, and postorder.")


    def traverse(nodeFunction=print, traverseOrder='inorder'):
        self.__traverse(self.root, nodeFunction, traverseOrder)
        
        



def bstSort(list):

    def insertElems(node):
        sortedList.append(node.value)
    
    myTree = BinarySearchTree()
    sortedList = []

    for element in list:
        myTree.insert(element)
    

    myTree.traverse(insertElems, 'inorder')

    return sortedList



            

                

        
    
    

    

    