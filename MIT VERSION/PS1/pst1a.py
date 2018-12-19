# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 00:21:02 2017

@author: Sebastian
"""

annual_salary = float(input("Insert your annual salary: "))
portion_saved = float(input("Insert the percent of your salary to save," 
                            +" as a decimal: "))
total_cost = float(input("Insert the cost of your dream home: "))

if portion_saved > 1:
    print("Please input a decimal number between 0 and 1")
    
else:    
    month_salary = annual_salary/12.0
    
    portion_down_payment = 0.25*total_cost
    r = 0.04
    current_savings = 0
    i = 0
    
    while current_savings < portion_down_payment:        
        current_savings += current_savings*r/12 + portion_saved*month_salary
        i += 1
        
    print("Number of months: {}".format(i))
