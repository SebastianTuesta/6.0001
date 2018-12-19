# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:40:16 2017

@author: Sebastian
"""

s = input("s: ")

times = 0

for i in range(0,len(s)):
    if s[i] == 'b':
        if s[i:i+3] == 'bob':
            times += 1


print("Number of times bob occurs is: {}".format(times))