'''
This file is a test file for the sorting algorithms in sorting/sort.py.
It tests both for correctness, but also for the run-time complexity
of the different algorithms and plots them
'''

import os
import sys

current_dir = os.path.dirname(__file__)
test_file_dir = os.path.join(current_dir, '..', 'sorting')
sys.path.append(test_file_dir)

import sort

import random
import time

from matplotlib import pyplot as plt


'''
Generates a list of random numbers to sort of a given length
'''
def makeList(length):

    # create empty list to fill
    randomList = []

    # append to list up to length
    for i in range(length):
        randomList.append(random.randint(0, 100000))
    
    return randomList


'''
Times the sorting algorithm
'''
def timeSort(list, algorithm):

    if algorithm == sort.merge_sort:
        start_time = time.process_time()
        sorted_list = algorithm(list)
        stop_time = time.process_time()

        return stop_time - start_time
    
    elif algorithm == sort.quicksort:
        start_time = time.process_time()
        algorithm(list, 0, len(list)-1)
        stop_time = time.process_time()

        return stop_time - start_time
    
    elif algorithm == sort.insertion_sort:
        start_time = time.process_time()
        algorithm(list)
        stop_time = time.process_time()

        return stop_time - start_time
    
    else:
        raise Exception("Sorting algorithm not recognized.")


'''
Returns a list of times taken to sort lists of increasing length
with the given sorting algorithm. This can, in turn, be plotted
to give a visual representation of the asymptotic complexity.
'''
def getAsymptoticComplexity(algorithm, lengths):

    times = []

    for length in lengths:

        # creates random list of given length
        time_list = makeList(length)

        # time the sorting algorithm on the given list
        sort_time = timeSort(time_list, algorithm)

        # appends the time to the times list
        times.append(sort_time)
    
    return times


'''
Plots the time curve for the algorithm against the lengths
of the lists used to test the sorting algorithm
'''
def plotTimes(lengths, algorithms):

    alg_times = [[0]*len(lengths)]*len(algorithms)

    for i in range(len(algorithms)):
        times = getAsymptoticComplexity(algorithms[i], lengths)
        
        for j in range(len(lengths)):
            alg_times[i][j] = times[j]

    #alg_times = [getAsymptoticComplexity(algorithm, lengths) for algorithm in algorithms]
    
    print(len(alg_times))
    
    #for i in range(len(alg_times)):
    #    plt.plot(lengths, alg_times[i])
    
    #plt.show()

    return alg_times


if __name__ == "__main__":

    lengths = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    algorithms = [sort.insertion_sort, sort.merge_sort, sort.quicksort]

    times1 = getAsymptoticComplexity(sort.insertion_sort, lengths)
    times2 = getAsymptoticComplexity(sort.merge_sort, lengths)
    times3 = getAsymptoticComplexity(sort.quicksort, lengths)

    plt.plot(lengths, times1, marker='o', color='b', label='insertion sort')
    plt.plot(lengths, times2, marker='s', color='g', label='merge sort')
    plt.plot(lengths, times3, marker='v', color='r', label='quicksort')

    plt.legend()
    plt.show()


        