#!/usr/bin/python3

'''
Tests the heap data structure and the heapsort algorithm.
'''

import os
import sys

current_dir = os.path.dirname(__file__)
test_file_dir = os.path.join(current_dir, '..', 'heap')
sys.path.append(test_file_dir)

from heap import MaxHeap
from heap import heapSort


def testHeap(list):

    myHeap = MaxHeap(list)

    isValid = myHeap.verifyMaxHeap(0)

    print (isValid)

    print(myHeap.array)


if __name__ == "__main__":

    myList = [2, 3, 4, 5, 1, 6, 7, 3, 9, 8, 7, 2, 8]
    myList2 = [1, 2]

    

    #testHeap(myList)

    sortedList = heapSort(myList2)
    reverseSortedList = heapSort(myList2, reverse=True)

    print(sortedList)
    print(reverseSortedList)
