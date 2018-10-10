# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:32:13 2018

@author: Tirtha
"""

import random
import math

def partition(A,l,r):
    global count_op
    p=A[l]
    i=l+1
    for j in range(l+1,r):
        if A[j]<=p:
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
            i+=1
            count_op+=4
    temp=A[i-1]
    A[i-1]=A[l]
    A[l]=temp
    print("Modified list:",A)
    #print("Pivot pos",i)
    return (i)

def QuickSortInPlace(lst,low,high):
    global count_op
    length=high-low
    # Base case: Nothing to do
    if length<=1:
        pass
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

"""
count_array=[]
log_array=[]
for i in range(2,102):
    test_lst=[]
    count_op=0
    for k in range(i):
        test_lst.append(random.randint(0,1000))
    QuickSortInPlace(test_lst,0,i)
    count_array.append(count_op)
    log_array.append(5*i*math.log(i,2))
    
print(count_array)

import matplotlib.pyplot as plt
plt.scatter(range(2,102),count_array)
plt.plot(range(2,102),log_array,lw=3,color='red')
plt.grid(True)
plt.show()
"""