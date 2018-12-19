# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:01:21 2017

@author: Sebastian
"""

'abcd'

def to_char(sentence):
    sentence_aux =""
    for i in sentence:
        if i in "abcdefghijklmnopqrstuvxyz":
            sentence_aux += i
    return sentence_aux

def is_palindrome(sentence):
    n = len(sentence)
    if n<=1:
        return True
    else:
        if sentence[0] == sentence[n-1]:
            return is_palindrome(sentence[1:n-1])
        else:
            return False
            
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    if is_palindrome(to_char(sentence.lower())):
        print("The sencence is palindrome")
    else:
        print("The sencence is not palindrome")