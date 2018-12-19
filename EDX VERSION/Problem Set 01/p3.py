# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:40:53 2017

@author: Sebastian
"""

s = input("s= ")

myList = []
longest_string = ""
for i in range(len(s)):
    if i == 0:
        longest_string+=s[0]
    elif i > 0:
        if s[i] >= s[i-1]:
            longest_string += s[i]
            if i == len(s)-1:
                myList.append(longest_string)
        else:
            myList.append(longest_string)
            longest_string = s[i]

print("Longest substring in alphabetical order is: {}".format(max(myList, key=len)))      