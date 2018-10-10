# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:32:13 2018

@author: Tirtha
"""

import random

def partition(A,l,r):
    p=A[l]
    i=l+1
    for j in range(l+1,r):
        if A[j]<=p:
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
            i+=1
    temp=A[i-1]
    A[i-1]=A[l]
    A[l]=temp
    print("Modified list:",A)
    print("Pivot pos",i)
    return (i)

def QuickSortInPlace(lst,low,high):
    #count_op=0
    length=high-low
    # Base case: Nothing to do
    if length<=1:
        pass
    elif length==2:
        if (lst[0]>=lst[1]):
            temp=lst[0]
            lst[0]=lst[1]
            lst[1]=temp
    # Recursive case
    else:
        # Partition the array and get back the pivot position
        pivot_pos=partition(lst,low,high)
        # Quicksort on the left half of the pivot
        QuickSortInPlace(lst,low,pivot_pos-1)
        # Quicksort on the right half of the pivot
        QuickSortInPlace(lst,pivot_pos,high)

# Test code
##=============
N_test=15
test_lst=[]
for i in range(N_test):
    test_lst.append(random.randint(0,100))

print("Original list:",test_lst)
QuickSortInPlace(test_lst,0,15)
print("Sorted list:  ",test_lst)