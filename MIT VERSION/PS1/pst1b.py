# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 01:34:15 2017

@author: Sebastian
"""

annual_salary = float(input("Insert your annual salary: "))
portion_saved = float(input("Insert the percent of your salary to save,"
                            + "as a decimal: "))
total_cost = float(input("Insert the cost of your dream home: "))
semi_annual_raise = float(input("Insert the semi-annual raise, as decimal: "))


portion_down_payment = 0.25*total_cost
r = 0.04
current_savings = 0
i = 0
while current_savings < portion_down_payment:        
    current_savings += current_savings*r/12 + portion_saved*(annual_salary/12.0)
    i += 1
    if i%6 == 0:
        annual_salary += annual_salary*semi_annual_raise
    
print("Number of months: {}".format(i))
