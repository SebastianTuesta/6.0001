# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:58:20 2017

@author: Sebastian
"""

# Paste your code here
def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    #YOUR CODE HERE
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
