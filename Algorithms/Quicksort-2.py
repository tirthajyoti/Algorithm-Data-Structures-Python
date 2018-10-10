# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:00:43 2018

@author: Tirtha
"""
import random
def sort(array, start, end):
    if end > start:
        pivot = array[start]
        middle = start + 1
        for i in range(start+1, end):
            if array[i] > array[middle]:
                tmp = array[i]
                array[i] = array[middle]
                array[middle] = tmp
                middle += 1
    sort(array, start, middle)
    sort(array, middle, end)

N_test=10
test_lst=[]
for i in range(N_test):
    test_lst.append(random.randint(0,100))

print("Original list:",test_lst)
sort(test_lst,0,9)
print("Sorted list:",test_lst)