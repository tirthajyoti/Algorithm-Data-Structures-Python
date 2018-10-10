# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:26:21 2018

@author: Tirtha
"""
import random

def quicksort(lst):
    #count_op=0
    smaller=[]
    equal=[]
    bigger=[]
    if len(lst)==0 or len(lst)==1:
        return (lst)
    else:
        pivot=lst[0]
        for n in lst:
            if n<pivot:
                smaller.append(n)
            elif n==pivot:
                equal.append(n)
            else:
                bigger.append(n)
        return (quicksort(smaller)+equal+quicksort(bigger))

N_test=10
test_lst=[]
for i in range(N_test):
    test_lst.append(random.randint(0,100))

print("Original list:",test_lst)
print("Sorted list:",quicksort(test_lst))