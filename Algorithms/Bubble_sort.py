# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 17:45:47 2017
@author: Tirthajyoti Sarkar
Simple Bubble sort with counter for number of swap operations
Accepts user input on minimum and maximum bound of the array and the size of the array
"""

import random

def bubble_sort(array):
    n = len(array)
    # Set a swap counter to a non-zero value
    swap_counter=-1
    swap_op=0
    # Unitll swap counter hits zero...
    while(swap_counter!=0):
        # Reset the swap counter at the beginnig of each iteration
        swap_counter=0
        # Iterate over the array examining the a pair of data
        for i in range(n-1):
            if(array[i]>array[i+1]):
                temp=array[i]
                array[i]=array[i+1]
                array[i+1]=temp
                # Print for troubleshooting
                #print(sorted_array)
                swap_counter+=1
                swap_op+=1
            else:
                pass
    return (array,swap_op)

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
sorted_array,n_op=bubble_sort(a)
print("Sorted array: {}\nTook {} operations".format(sorted_array,n_op))