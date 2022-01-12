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
    def __init__(self, key, value, next=None, prev=None, chainNext=None, chainPrev=None):
        self.key = key
        self.value = value
        self.chainNext = chainNext
        self.chainPrev = chainPrev
    

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

        # possibly change prime range to be larger
        p = sympy.randprime(1000000000, 10000000000)
        
        # a and b are for linear congruence
        a = random.randint(1, p-1)
        b = random.randint(0, p-1)
        
        
        def __hash(key):
            if not (isinstance(key, int) or isinstance(key, float)):
                keyBytes = pickle.dumps(key)
                temp = int.from_bytes(keyBytes, 'little')
                return ((a*temp + b) % p) % size
            else:
                return ((a*int(key) + b) % p) % size
        
        return __hash
    
    
    # size should be a power of 2
    def __init__(self, size=16):
        self.size = size
        self.table = [None] * size
        self.numKeys = 0
        self.hashFunc = self.__getHash(size)

    

    
    

    def __doubleTable(self):
        pass


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
        index = self.hashFunc(key)

        elementToInsert = TableElement(key, value)

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
