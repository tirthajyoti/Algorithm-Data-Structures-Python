# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 18:44:02 2017
@author: Tirthajyoti Sarkar
Simple Selection sort with counter for total number of operations (finding minimum and swapping)
Accepts user input on minimum and maximum bound of the array and the size of the array
"""
import random

def find_min(array):
    n=len(array)
    r = array[0]
    count=0
    for i in range(1,n):
        count+=1
        if r>array[i]:
            r=array[i]
    return(r,count)

def selection_sort(array):
    n=len(array)
    num_op=0
    # Iterate over the length of the array, pushing smaller values to the left
    for i in range(n):
        # Scan the array from i-th element (where the iterator is currently) to the end for minimum
        m,c_min=find_min(array[i:n])
        # IMPORTANT: Get the index of the minimum element w.r.t. to the main array
        m_index=array[i:n].index(m)+i
        # If the first element of the unsorted portion i.e. i-th element> minimum, then SWAP 
        if (array[i]>m):
            # Print statement for examining minimum and its index, Troubleshooting
            #print("Minimum found {} at position {}. Swapping positions {} and {}".format(m,m_index,i,m_index))
            temp=array[i]
            array[i]=m
            array[m_index]=temp
            num_op+=(c_min+1)
            print(array)            
        else:
            pass
    return (array,num_op)

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
sorted_array,n_op=selection_sort(a)
print("Sorted array: {}\nTook {} operations".format(sorted_array,n_op))