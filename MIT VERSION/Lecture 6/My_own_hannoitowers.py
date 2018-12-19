# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:17:00 2017

@author: Sebastian
"""

def hannoi_towers(n, fr, to, aux):
    if n>0:
        hannoi_towers(n-1, fr, aux, to)
        print('Move from {} to {}'.format(fr, to))
        hannoi_towers(n-1, aux, to, fr)
    
if __name__ == '__main__':
    n = int(input("Number of pieces in the initial Tower: "))
    fr = input("Tower where from go: ")
    to = input("Tower to where go: ")
    aux = input("Tower used as auxiliar: ")
    
    print()
    print("Moviments")
    print()
    
    hannoi_towers(n, fr, to, aux)