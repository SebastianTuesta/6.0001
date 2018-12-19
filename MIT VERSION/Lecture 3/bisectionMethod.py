# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:03:39 2017

@author: Sebastian
"""

number=float(input("Insert a number: "))

if(number>0 and number<1):
    high=1
    low=0
elif(number>0):
    high=number
    low=0
else:
    high=0
    low=number
i=0
while(True):
    i+=1
    guess=(high+low)/2
    if(abs(guess**3-number)<=0.001):
        break
    elif(guess**3>number):
        high=guess
    elif(guess**3<number):
        low=guess
        
print("Number of iterations: {} and root: {}".format(i,round(guess,3)))