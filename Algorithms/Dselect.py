# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:30:03 2018

@author: Tirtha
"""
import random

def partition(A,p_idx):
    p=A[p_idx]
    #print("Input list to partition with pivot {}: {}".format(p,A))
    # Swap/move pivot to leftmost    
    temp=A[0]
    A[0]=A[p_idx]
    A[p_idx]=temp
    
    l=0
    i=l+1
    r=len(A)
    for j in range(l+1,r):
        if A[j]<=p:
            temp=A[j]
            A[j]=A[i]
            A[i]=temp
            i+=1
    # Now swap the pivot from the 0-th index to its rightful index
    temp=A[i-1]
    A[i-1]=A[l]
    A[l]=temp
    # Print partitioned list and new pivot index for debugging
    #print("Partitioned list:",A)
    #print("New pivot",i-1)
    #print("")
    return (i-1)

def median(A):
    if len(A)==1:
        return A[0]
    elif len(A)==2:
        return A[1]
    else:
        return A[int(len(A)/2)]

def Dselect(my_list,n):
    length=len(my_list)
    # Base case
    if length==1:
        return my_list[0]
    # Recursive case
    else:
        chunk=5
        medians=[]
        A=[]
        for i in range(0, length, chunk):
            A.append(my_list[i:i + chunk])
        #print("A:",A)
        for array in A:
            array.sort()
            medians.append(median(array))
        # Sorts the medians and choose the 'median of the medians' as pivot
        medians.sort()
        #print("Medians sorted:",medians)
        p = Dselect(medians,int(length/10))
        p_idx=my_list.index(p)
        #print("Pivot index and pivots:{}, {}".format(p_idx,p))
        # Partition based on the chosen median of median pivot
        new_pivot = partition(my_list,p_idx)
        # Case to check if the new pivot returned by partition is the n-th order
        # Disabled because it was giving error on some cases and preventing the code to reach the base case
        #if new_pivot==n:
            #print("New pivot equal to sought order")
            #return (my_list[new_pivot-1])
        if new_pivot>=n:
            # Recurse on the left side of the array with unchanged order statistic
            left=my_list[0:new_pivot]
            #print("New pivot {} >= {}. Recursing on {} with order {}".format(new_pivot,n,left,n))
            return Dselect(left,n)
        else:
            # Recurse on the right side of the array with order statistic shrinked
            right=my_list[new_pivot:]
            #print("New pivot {} < {}. Recursing on {} with order changed to {}".format(new_pivot,n,right,n-new_pivot))
            return Dselect(right,n-new_pivot)
            
"""                
# Test code for single case with fixed order statistic
##=============
N_test=20
test_lst=[]
for i in range(N_test):
    test_lst.append(random.randint(0,100))
#n= random.randint(1,6)
n=5
print("Original list:",test_lst)
print("Order statistic sought",n)
print("")

result = Dselect(test_lst,n)
test_lst.sort()
#element = test_lst[result-1]
print("{}-th order statistic is {}".format(n,result))

print("Sorted list",test_lst)
"""

## Test code with 100 cases with random order statistic
N=10000
check = []
# Create a test array of 20 integers
for i in range(N):
    N_test=20
    test_lst=[]
    for i in range(N_test):
        test_lst.append(random.randint(0,100))
    # Picking a random test input for order statistic
    n= random.randint(1,20)
    result = Dselect(test_lst,n)
    # Call Python's built-in sort method on the test array
    test_lst.sort()
    # Check if the sorted array's n-1-th element is the n-th order statistic returned by our program
    check.append(test_lst[n-1]==result)
# Print the sum total of truth values in the check array
print(sum(check))

