# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:51:14 2017

@author: Sebastian
"""

# Paste your code here
import string

def f(a,b):
    return a+b

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    #YOUR CODE HERE
    word = word.lower()
    
    i = 0
    score = []
    
    for letter in word:
        score.append((string.ascii_lowercase.index(letter) + 1)*i)
        i += 1 

    greater_value = max(score)
    score.remove(greater_value)
    
    second_greater_value = max(score)
    
    
    return f(greater_value, second_greater_value)
    
print(score('adD', f))