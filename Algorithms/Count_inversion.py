# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:16:36 2018

@author: Tirtha
"""

def merge_count_SplitInv(L1,L2):
    result=[]
    count=0
    # This loop runs till both input lists have non-zero elements in them
    # That means this loop stops when either of the input list runs out of element
    while (len(L1)>0 and len(L2)>0):
        if L1[0]<=L2[0]:
            # Append to the result list
            result.append(L1[0])
            #print("Result:",result)
            # Pop the first element of the list
            L1.pop(0)
        else:
            # Append to the result list
            result.append(L2[0])
            #print("Result:",result)
            # Pop the first element of the list
            L2.pop(0)
            # CRUX OF THE ALGORITHM: When we copy over from L2, we increment 
            #count by the number of elements REMAINING in L1 i.e. length of L1 because
            # the length is dynamically modified by popping the first element out whenever 
            # we copy over from L1
            count+=len(L1)
    # Now checking which input list has run out of element.
    # Whichever list still has element left, append all of them to the result array
    # Note, only one of these if-loops will be executed
    if(len(L1)>0):
        result=result+L1
    if(len(L2)>0):
        result=result+L2
        
    return (result,count)

def sort_count_inversion(my_list):
    length=len(my_list)
    # Base case
    if length==1:
        return (my_list,0)
    # Recursive case
    else:
        l1_sorted,x=sort_count_inversion(my_list[0:int(length/2)])
        l2_sorted,y=sort_count_inversion(my_list[int(length/2):length])
        l_sorted,z=merge_count_SplitInv(l1_sorted,l2_sorted)
        return (l_sorted,(x+y+z))