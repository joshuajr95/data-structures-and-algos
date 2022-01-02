'''
File: heap.py
Author: Joshua Jacobs-Rebhun
Date: December 30, 2021

This file defines the heap class with its associated methods and
also the heapsort algorithm.
'''


class MaxHeap:


    # get the left child index of the current index
    def leftChildIndex(self, index):
        return index*2 + 1


    # get the left child of the current index
    def leftChild(self, index):

        if self.leftChildIndex(index) >= len(self.array):
            return None
        else:
            return self.array[self.leftChildIndex(index)]
    

    # get the right child index of the current index
    def rightChildIndex(self, index):
        return index*2 + 2
    
    
    # get the right child of the current index
    def rightChild(self, index):

        if self.rightChildIndex(index) >= len(self.array):
            return None
        else:
            return self.array[self.rightChildIndex(index)]
    

    # fixes one instance of the max heap property
    def maxHeapify(self, index):

        # check if there are no children
        if self.leftChild(index) is None:
            return
        
        # check if there is no right child. If there is a right child
        # there will be a left child, so no need to check for left child
        elif self.rightChild(index) is None:
            if self.leftChild(index) > self.array[index]:
                temp = self.array[index]
                self.array[index] = self.leftChild(index)
                self.array[self.leftChildIndex(index)] = temp

                self.maxHeapify(self.leftChildIndex(index))

        
        # if the left and right child are greater, then take the max of the two
        elif self.leftChild(index) > self.array[index] and self.rightChild(index) > self.array[index]:
            
            heapifyIndex = 0

            if self.leftChild(index) > self.rightChild(index):
                heapifyIndex = self.leftChildIndex(index)
            else:
                heapifyIndex = self.rightChildIndex(index)
            
            temp = self.array[index]
            self.array[index] = self.array[heapifyIndex]
            self.array[heapifyIndex] = temp

            self.maxHeapify(heapifyIndex)
        

        # if the left child is greater then use the left child
        elif self.leftChild(index) > self.array[index]:
            temp = self.array[index]
            self.array[index] = self.leftChild(index)
            self.array[self.leftChildIndex(index)] = temp
            self.maxHeapify(self.leftChildIndex(index))


        # if the right child is greater then use the right child
        elif self.rightChild(index) > self.array[index]:
            temp = self.array[index]
            self.array[index] = self.rightChild(index)
            self.array[self.rightChildIndex(index)] = temp
            self.maxHeapify(self.rightChildIndex(index))


        # if neither left nor right child are greater, return immediately
        else:
            return


    # builds a max heap from an array
    def buildMaxHeap(self):
        
        for i in range(len(self.array)//2, -1, -1):
            self.maxHeapify(i)
    

    # gets the max element
    def getMax(self):
        return self.array[0]
    

    
    

    # checks the rep invariant of the maxHeap data structure
    def verifyMaxHeap(self, index):

        # if the left child does not exist, then the right child will also not
        # exist and in this case the node is a leaf node, so it is a maxHeap
        # by definition
        if self.leftChild(index) is None:
            return True
        
        # if the right child does not exist, check the left child for max heap property
        elif self.rightChild(index) is None:
            return self.leftChild(index) <= self.array[index]
        
        elif self.leftChild(index) > self.array[index] or self.rightChild(index) > self.array[index]:
            return False
        
        else:
            isLeftSubtreeMaxHeap = self.verifyMaxHeap(self.leftChildIndex(index))
            isRightSubtreeMaxHeap = self.verifyMaxHeap(self.rightChildIndex(index))

            return isLeftSubtreeMaxHeap and isRightSubtreeMaxHeap
    

    # gets the max element and removes it from the heap
    def extractMax(self):
        
        # check to see if array is empty
        if len(self.array) == 0:
            return None

        lastIndex = len(self.array)-1
        heapMax = self.array[0]
        self.array[0] = self.array[lastIndex]
        self.array[lastIndex] = heapMax
        heapMax = self.array.pop(lastIndex)
        self.maxHeapify(0)

        return heapMax


    ''' default constructor '''
    def __init__(self):
        self.array = []

    
    ''' constructor converts array to heap '''
    def __init__(self, array):
        self.array = array.copy()
        self.buildMaxHeap()

        if not self.verifyMaxHeap(0):
            raise Exception("Could not build heap. Rep invariant violated.")
    


def heapSort(array, reverse=False):

    sortHeap = MaxHeap(array)
    sortedArray = []
    heapMax = sortHeap.extractMax()
    while heapMax is not None:
        
        # if sort list in reverse, just append
        if reverse:
            sortedArray.append(heapMax)
        
        # otherwise, append at the beginning
        else:
            sortedArray.insert(0, heapMax)
        
        heapMax = sortHeap.extractMax()
    
    return sortedArray
