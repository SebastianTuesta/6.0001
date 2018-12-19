# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 01:46:51 2017

@author: Sebastian
"""

def getSavings(guess):
    local_Annual_salary = annual_salary
    portion_saved = guess/10000
    current_savings = 0
    for i in range(1, 37, 1):
        current_savings += (current_savings*r/12 
                            + portion_saved*(local_Annual_salary/12.0))
        if i % 6 == 0:
            local_Annual_salary += local_Annual_salary*semi_annual_raise
    return int(current_savings)


def getBestInteres():
    high = 10000
    low = 0
    if getSavings(high) < portion_down_payment:
        print("It is not possible to pay the down payment in three years")
    
    else:
        i = 0
        while True:
            i += 1
            guess = (high+low)//2
            
            saving = getSavings(guess)     
            if abs(saving-portion_down_payment) <= 100:
                 break       
            elif saving < portion_down_payment:
                low = guess
            elif saving > portion_down_payment:
                high = guess
        print("Best savings rate: {}".format(round(guess/10000, 4)))
        print("Steps in bisection search: {}".format(i))
        
        
if __name__ == "__main__":
    annual_salary = float(input("Insert your annual salary: "))

    total_cost = 1000000
    semi_annual_raise = .07
    
    portion_down_payment = 0.25*total_cost
    r = 0.04
    getBestInteres()

        