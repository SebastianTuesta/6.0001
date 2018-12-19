# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:19:09 2017

@author: Sebastian
"""

balance = int(input("balance = "))
annualInterestRate = float(input("annualIntesetRate = "))

monthlyInterestRate = annualInterestRate/12.0
monthlyPaymentLowerBound = balance/12
monthlyPaymentUpperBound = (balance * pow(1 + monthlyInterestRate,12))/12.0

er = 0.02

initial_balance = balance

while True:
        
    monthlyPaymentMiddleBound = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) /2        
                 
    if monthlyPaymentUpperBound - monthlyPaymentLowerBound < er:
        print("Lowest Payment : {0:.2f}".format(monthlyPaymentMiddleBound))
        break

    else:        
        for i in range(12):
            monthlyUnpaidBalance = balance - monthlyPaymentMiddleBound
            balance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
        
        balance = initial_balance
        
        if monthlyUnpaidBalance > 0:
            monthlyPaymentLowerBound = monthlyPaymentMiddleBound
        else:
            monthlyPaymentUpperBound = monthlyPaymentMiddleBound