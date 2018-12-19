# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:02:13 2017

@author: Sebastian
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    sum_ = 0
    
    if len(listA) == len(listB):
        n = len(listA)
        for i in range(n):
            sum_ += listA[i]*listB[i]
            
    return sum_
    
listA = [1, 2, 3] 
listB = [4, 5, 6]

print(dotProduct(listA, listB))