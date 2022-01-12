'''
File: sort.py
Author: Joshua Jacobs-Rebhun
Date: December 29, 2021

This file has a number of sorting algorithms.
'''


'''
Sorts the input list in place in O(n^2) time
'''
def insertion_sort(list):

    for i in range(1, len(list)):
        j = i
        while(j > 0 and list[j] < list[j-1]):
            temp = list[j]
            list[j] = list[j-1]
            list[j-1] = temp
            j -= 1


'''
Helper function for the merge_sort routine. Merges the two sorted
halves of a list into one sorted list
'''
def merge(lower_half, upper_half):

    # create empty list for merging two halves of the list
    mergedList = []

    # i is iterator for lower_half and j is iterator for upper_half
    i = 0
    j = 0

    # merge the two halves together until one half reaches the end
    while i < len(lower_half) and j < len(upper_half):

        if(lower_half[i] < upper_half[j]):
            mergedList.append(lower_half[i])
            i += 1
        
        else:
            mergedList.append(upper_half[j])
            j += 1
    

    # if upper half reached the end first, append the rest of 
    # lower half to the merged array
    while i < len(lower_half):
        mergedList.append(lower_half[i])
        i += 1
    

    # if lower half reached the end first, append the rest of
    # upper half to the merged array
    while j < len(upper_half):
        mergedList.append(upper_half[j])
        j += 1
    
    return mergedList


'''
Merge sort is a divide-and-conquer recursive sorting algorithm.
Does not sort in place.
'''
def merge_sort(list):

    # base case for the recursion
    if(len(list) <= 1):
        return list

    # find the midpoint in the section of the list
    mid = len(list)//2

    # non-base case recursively 
    lower_half = merge_sort(list[:mid])
    upper_half = merge_sort(list[mid:])

    return merge(lower_half, upper_half)


'''
Recursive sorting algorithm that sorts the list in-place. Usually
considered the best sorting algorithm.
'''
def quicksort(list, start, end):

    # base case
    if start >= end:
        return

    
    pivot_index = end

    ############################################################
    # first section partitions the array using the pivot value #
    ############################################################


    i = start
    while i < pivot_index-1:
        if list[i] > list[pivot_index]:

            # swap pivot with pivot-1
            temp = list[pivot_index]
            list[pivot_index] = list[pivot_index-1]
            list[pivot_index-1] = temp

            # swap i with pivot
            temp = list[pivot_index]
            list[pivot_index] = list[i]
            list[i] = temp

            # decrement pivot index
            pivot_index -= 1
        
        else:
            i += 1
    
    # if element just before pivot is greater than pivot, swap the two
    if list[i] > list[pivot_index]:
        temp = list[pivot_index]
        list[pivot_index] = list[i]
        list[i] = temp
        pivot_index -= 1
    
    ###############################################################################
    # this section recursively calls quicksort on two halves of partitioned array #
    ###############################################################################
    quicksort(list, start, pivot_index-1)
    quicksort(list, pivot_index+1, end)


'''
Counting sort is a linear time sorting algorithm that can only be used
for positive integers, or data structures that have a positive integer
field that can be sorted on. All positive integers must be less than
some value k, and the complexity of the algorithm is O(n + k).
'''
def countingSort(list, k, key=lambda x: x):
    
    L = []

    for i in range(k+1):
        L.append([])
    
    
    for j in range(len(list)):
        print("length L: " + str(len(L)))
        print("index: " + str(key(list[j])))
        L[key(list[j])].append(list[j])
    
    output = []
    
    for i in range(k):
        output.extend(L[i])
    
    return output


def radixSort(list, base, digits):

    sorted_list = list

    
    for i in range(digits):
        print("digit " + str(i))
        sorted_list = countingSort(sorted_list, base, lambda x: (x % (base**(i+1)))//(base**i))
        print(sorted_list)
    

    return sorted_list


'''
Wrapper function for the sorting algorithms allows separation between
the user of the function and the implementation. The algorithm parameter
allows the user to specify the type of algorithm to use to sort the list
and defaults to quicksort. The possibilities are quicksort and insertion_sort.
Merge_sort does not work here since it does not sort in place.
'''
def sort(list, algorithm=quicksort):

    if algorithm == quicksort:
        algorithm(list, 0, len(list)-1)

    else:
        algorithm(list)

