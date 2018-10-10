# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 23:26:32 2017
@author: Tirthajyoti Sarkar
Simple Insertion sort with counter for total number of operations (shifting and iterating)
Accepts user input on minimum and maximum bound of the array and the size of the array
"""
import random

def insertion_sort(array):
    counter = 0
    # Iterate over the array starting from 2nd element i.e. index 1
    for index in range(1,len(array)):
        # Set current value and index
        currentvalue = array[index]
        position = index
        # Keep shifting the elements to insert the next unsorted element in the proper position 
        while position>0 and array[position-1]>currentvalue:
            array[position]=array[position-1]
            position = position-1
            array[position]=currentvalue
            counter+=1
            # Print current state of array for troubleshooting
            #print(array)
    return (array,counter)

# User inputs for generating the random arrays                
mini = int(input("Enter the minimum bound:"))
maxi = int(input("Enter the maximum bound:"))
num = int(input("Enter the size:"))

# Create random array based on user-specified minimum/maximum bounds and number of elements
a= []
for i in range(num):
    a.append(random.randint(mini,maxi))

print("\nInitial array:",a)

# Get the sorted array back along with the count of # of operations it took to sort
sorted_array,n_op=insertion_sort(a)
print("Sorted array: {}\nTook {} operations".format(sorted_array,n_op))