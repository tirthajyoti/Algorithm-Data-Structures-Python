# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:17:46 2018

@author: Tirtha
"""

import random

def Rselect(my_list,n):
    length=len(my_list)
    if length==1:
        return my_list[0]
    else:
        low=[]
        high=[]
        p_idx = random.randint(1,length-1)
        pivot = my_list[p_idx]
        #print("Pivot chosen",pivot)
        if pivot==max(my_list):
            high.append(pivot)
            my_list.remove(pivot)
            low=my_list
        else:
            for ele in my_list:
                if ele<=pivot:
                    low.append(ele)
                else:
                    high.append(ele)
        #low=low+equal
        #print("Low list",low)
        #print("High list",high)
        if n<=len(low):
            #print("Recursing on {} with order {}".format(low,n))
            return Rselect(low,n)
        else:
            #print("Recursing on {} with order {}".format(high,n-len(low)))
            return Rselect(high,n-len(low))

             
# Test code for single case with fixed order statistic
##=============
"""
N_test=7
test_lst=[]
for i in range(N_test):
    test_lst.append(random.randint(0,100))
#n= random.randint(1,6)
n=3
print("Original list:",test_lst)
print("Order statistic sought",n)
print("")

result = Rselect(test_lst,n)
test_lst.sort()
#element = test_lst[result-1]
print("{}-th order statistic is {}".format(n,result))

print("Sorted list",test_lst)

"""
## Test code with 100 cases with random order statistic
N=1000
check = []
# Create a test array of 20 integers
for i in range(N):
    N_test=20
    test_lst=[]
    for i in range(N_test):
        test_lst.append(random.randint(0,100))
    # Picking a random test input for order statistic
    n= random.randint(0,19)
    result = Rselect(test_lst,n)
    # Call Python's built-in sort method on the test array
    test_lst.sort()
    # Check if the sorted array's n-1-th element is the n-th order statistic returned by our program
    check.append(test_lst[n-1]==result)
# Print the sum total of truth values in the check array
print(sum(check))