# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:53:54 2017

@author: Sebastian
"""

balance = int(input("balance = "))
annualInterestRate = float(input("annualIntesetRate = "))

monthlyInterestRate = annualInterestRate/12.0
lowestPayment = 10
initial_balance = balance

while True:
    for i in range(12):
        monthlyUnpaidBalance = balance - lowestPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
        
    
    if monthlyUnpaidBalance <= 0:
        break
    else:
        balance = initial_balance
        lowestPayment += 10
    
print("Lowest Payment: {0:.2f}".format(lowestPayment))