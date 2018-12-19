# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:59:08 2017

@author: Sebastian
"""

# Paste your function here
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    dict = {}
    
    for key in d:
        if d[key] not in dict:
            dict[d[key]] = [key]
        else:
            dict[d[key]].append(key)
            
    for i in dict:
        dict[i].sort()
    
    return dict

d = {1:10, 2:20, 3:30, 4:30}
print(dict_invert(d))