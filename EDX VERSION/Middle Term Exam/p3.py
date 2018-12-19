# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:03:10 2017

@author: Sebastian
"""

def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x*x + b*x + c
   
def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    # Your code here 
    print(evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2))
    
a1, b1, c1, x1, a2, b2, c2, x2 = 0.06, 4.41, 6.46, -3.81, 1.75, 8.49, 0.52, 7.13

twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2)