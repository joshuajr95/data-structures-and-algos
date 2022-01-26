'''
File: hashtable.py
Author: Joshua Jacobs-Rebhun
Date: January 10, 2022

This file implements a hashtable data structure, which can be used to
implement the dictionary ADT or set ADT.
'''

import sympy
import random
import pickle


'''
This class is for the elements of the hashtable. It stores the key-value pairs
and the next element and previous element pointers for purpose of iterating
over the table (i.e. for key, value in dictionary). These are the key, value,
next, and prev variables. The chainNext and chainPrev variables are used for
implementing chaining in the hashtable.
'''
class TableElement:


    # constructor
    def __init__(self, key, value, chainNext=None, chainPrev=None, hashCache=None):
        self.key = key
        self.value = value
        self.chainNext = chainNext
        self.chainPrev = chainPrev
        self.hashCache = hashCache


    def isEndOfChain(self):
        return self.chainNext is None
    
    def isBeginningOfChain(self):
        return self.chainPrev is None
    
    def isLengthOneChain(self):
        return self.isEndOfChain() and self.isBeginningOfChain()
    
    
    




'''
Hash table data structure can be used to implement dictionary or set ADTs. 
This implementation uses chaining to solve collisions.
'''
class HashTable:
    

    # __getHash returns a closure for dynamically altering the hash function
    # as the table changes size
    def __getHash(self, size):
        
        def __hash(key):
            return ((self.a*hash(key) + self.b) % self.p) % size
        
        return __hash
    
    
    # caching the hash value allows for faster table doubling
    def __getHashCache(self, key):
        return (self.a*hash(key) + self.b) %self.p
    
    
    # size should be a power of 2
    def __init__(self, size=16, primeRange=(1000000, 10000000)):
        self.size = size
        self.table = [None] * size
        self.numKeys = 0
        self.p = sympy.randprime(primeRange[0], primeRange[1])
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
        self.hashFunc = self.__getHash(size)
    

    def __doubleTable(self):
        newSize = self.size * 2
        newArray = [None] * newSize

        for i in range(size):
            while self.table[i] is not None:
                currentElement = self.table[i]
                
                if currentElement.isLengthOneChain():
                    self.table[i] = None
                else:
                    currentElement.chainNext.chainPrev = None
                    self.table[i] = currentElement.chainNext
                    currentElement.chainNext = None
                
                if newArray[currentElement.hashCache % newSize] is None:
                    newArray[currentElement.hashCache % newSize] = currentElement
                else:
                    insertAfter = newArray[currentElement.hashCache % newSize]
                    while insertAfter.chainNext is not None:
                        insertAfter = insertAfter.chainNext
                    
                    insertAfter.chainNext = currentElement
                    currentElement.chainPrev = insertAfter
        
        self.table = newArray
        self.size = newSize
        self.hashFunc = self.__getHash(self.size)


    def get(self, key):
        index = self.hashFunc(key)

        returnValue = None

        if self.table[index] is None:
            raise KeyError("Key not in hashtable")
        else:
            element = self.table[index]

            while element.key != key and element.chainNext is not None:
                element = element.chainNext
            
            if element.key == key:
                returnValue = element.value
            else:
                raise KeyError("Key not in hashtable")

        return returnValue
    

    # get rid of possible duplicates
    def add(self, key, value):
        
        if self.size <= self.numKeys:
            self.__doubleTable()

        index = self.hashFunc(key)

        elementToInsert = TableElement(key, value)
        elementToInsert.hashCache = self.__getHashCache(key)

        # if collision, then append table element to end of list
        if self.table[index] is not None:
            node = self.table[index]

            # move through linked list
            while node.key != key and node.chainNext is not None:
                node = node.chainNext
            
            # overwriting existing key-value pair
            if node.key == key:
                node.value = value
            
            # link up new node
            else:
                node.chainNext = elementToInsert
                elementToInsert.chainPrev = node
                self.numKeys += 1

        # if no collision, insert element in desired slot
        else:
            self.table[index] = elementToInsert
            self.numKeys += 1
        

    

    def delete(self, key):
        index = self.hashFunc(key)

        valueToReturn = None

        if self.table[index] is None:
            raise KeyError("Key not in hashtable")
        
        else:
            element = self.table[index]

            while element.key != key and element.chainNext is not None:
                element = element.chainNext
            
            if element.key == key:
                if element.isLengthOneChain():
                    valueToReturn = element.value
                    self.table[index] = None
                    self.numKeys -= 1

                elif element.isEndOfChain():
                    valueToReturn = element.value
                    element.chainPrev.chainNext = None
                    element.chainPrev = None
                    self.numKeys -= 1
                
                elif element.isBeginningOfChain():
                    valueToReturn = element.value
                    self.table[index] = element.chainNext
                    element.chainNext.chainPrev = None
                    element.chainNext = None
                    self.numKeys -= 1
                
                else:
                    valueToReturn = element.value
                    element.chainNext.chainPrev = element.chainPrev
                    element.chainPrev.chainNext = element.chainNext
                    element.chainNext = None
                    element.chainPrev = None
                    self.numKeys -= 1

            else:
                raise KeyError("Key not in hashtable")

        return valueToReturn
    

    def iterate(self):
        kvpairs = []

        for i in range(len(self.table)):
            if self.table[i] is not None:
                element = self.table[i]
                while element is not None:
                    kvtuple = (element.key, element.value)
                    kvpairs.append(kvtuple)
                    element = element.chainNext
        

        return kvpairs

    
    def keys(self):
        keys = []

        for i in range(len(self.table)):
            if self.table[i] is not None:
                element = self.table[i]
                while element is not None:
                    keys.append(element.key)
                    element = element.chainNext
        

        return keys
    

    def values(self):
        values = []

        for i in range(len(self.table)):
            if self.table[i] is not None:
                element = self.table[i]
                while element is not None:
                    values.append(element.value)
                    element = element.chainNext
        

        return values
