# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

balance = int(input("balance = "))
annualInterestRate = float(input("annualInterestRate = "))
monthlyPaymentRate = float(input("monthlyPayment = "))

monthlyInterestRate= annualInterestRate/12.0
previous_balance = balance

for i in range(12):
    monthlyPayment  = monthlyPaymentRate*previous_balance
    monthlyUnpaid = previous_balance - monthlyPayment
    previous_balance = monthlyUnpaid + (monthlyInterestRate*monthlyUnpaid)
    
print("Remaining balanc :{0:.2f}".format(previous_balance))