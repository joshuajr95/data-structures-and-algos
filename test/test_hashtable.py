'''
File: test_hashtable.py
Author: Joshua Jacobs-Rebhun
Date: January 11, 2022


This is the test file for the hashtable implementation
'''


import os
import sys

current_dir = os.path.dirname(__file__)
test_file_dir = os.path.join(current_dir, "..", "hash")
sys.path.append(test_file_dir)

from hashtable import HashTable


if __name__ == "__main__":

    myTable = HashTable()

    instring = "hello"

    myTable.add(instring, "there")
    print(myTable.get("hello"))
    mystring = myTable.delete("hello")
    print(mystring)

