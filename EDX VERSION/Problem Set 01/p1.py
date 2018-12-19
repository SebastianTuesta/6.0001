# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:31:32 2017

@author: Sebastian
"""

s = input("s: ")

VOWEL = 'aeiou'

num_vowel = 0
for i in s:
    if i in VOWEL:
        num_vowel += 1
    
print("Number of vowels: {}".format(num_vowel))