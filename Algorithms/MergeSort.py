# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:42:19 2018

@author: Tirtha
"""
def merge(list1,list2):
    """
    Takes two lists and merge them in a sorted list
    """
    # Initialie the empty list
    result=[]
    i=0
    j=0
    # This loop runs till both input lists have non-zero elements in them
    # That means this loop stops when either of the input list runs out of element
    while (len(list1)>0 and len(list2)>0):
        if list1[0]<=list2[0]:
            # Append to the result list
            result.append(list1[0])
            #print("Result:",result)
            # Pop the first element of the list
            list1.pop(0)
            i=i+1
        else:
            # Append to the result list
            result.append(list2[0])
            #print("Result:",result)
            # Pop the first element of the list
            list2.pop(0)
            j+=1
    # Now checking which input list has run out of element.
    # Whichever list still has element left, append all of them to the result array
    # Note, only one of these if-loops will be executed
    if(len(list1)>0):
        result=result+list1
    if(len(list2)>0):
        result=result+list2
    print("Result:",result)
    #print(f"i:{i},j:{j}")
    return (result)

def mergeSort(my_list):
    n = len(my_list)
    # Base case for 1-element array
    if n==1:
        return (my_list)
    # Recursive case: 
        # Divide the array into two halves.
        # Mergesort on the left half
        # Mergesort on the right half
        # Merge two sorted arrays
        # Return the merged result
    else:
        left_half=my_list[0:int(n/2)]
        right_half=my_list[int(n/2):n]
        print("Left half:",left_half)
        print("Right half:",right_half)
        left=mergeSort(left_half)
        right=mergeSort(right_half)
        print(f"Merging {left} and {right}")
        sorted_list=merge(left,right)
        return (sorted_list)