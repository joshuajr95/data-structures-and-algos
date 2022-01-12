'''
File: test_BST.py
Author: Joshua Jacobs-Rebhun
Date: January 8, 2022

Test file for the BST implementation
'''

import os
import sys

current_dir = os.path.dirname(__file__)
test_file_dir = os.path.join(current_dir, '..', 'tree')
sys.path.append(test_file_dir)

from BST import BinarySearchTree, BSTSort, buildBST



def test_BST_sort(list):
    sortedList = BSTSort(list)

    return sortedList


if __name__ == "__main__":
    
    testList = [3, 6, 5, 4, 1, 9, 8, 7, 6, 5, 3, 2, 1]

    myBST = buildBST(testList)

    print("Pre order traversal")
    myBST.traverse(traverseOrder='preorder')
    print("\n\nPost order traversal\n")
    myBST.traverse(traverseOrder='postorder')
    print(myBST.max())
    print(myBST.min())
    print(myBST.getOneSmaller(5))
    print(myBST.getOneLarger(5))

    myBST.delete(7)
    myBST.delete(3)

    myBST.traverse(traverseOrder='preorder')
    
    print(myBST.getOneLarger(4))

    sortedList = test_BST_sort(testList)

    print(sortedList)