# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:04:09 2021

@author: ABIOLA
"""

#minimum monthly payment = Minimum monthly payment rate * Balance
#(minimum monthly payment gets split into interest paid and principal)
#interest paid = annual interest rate/12 months * Balance
#principal paid = minimum monthly payment - interest paid
#remaining balance = balance - principal paid

outstanding_balance = float(raw_input("Enter outstanding balance "))
annual_interest_rate = float(raw_input("Enter annual interest rate as decimal "))
assert type(annual_interest_rate) == float,"input must be decimal"
minimum_monthly_payment_rate = float(raw_input("Enter minimum monthly payment rate as decimal "))
assert type(minimum_monthly_payment_rate) == float,"input must be decimal"
#minimum_monthly_payment_rate = (minimum_monthly_payment_rate / 100)
month = 1
total_interest = 0

total_principal_paid = 0
while month<=12:
    print "Month:",month
    print "Balance at the beginning of the month:",outstanding_balance
    
    minimum_monthly_payment = minimum_monthly_payment_rate * outstanding_balance
    print "Minimum Monthly Payment:",minimum_monthly_payment
    
    interest_paid = ((annual_interest_rate/(12)) * outstanding_balance)
    print "Interest Paid:",interest_paid
    principal_paid = minimum_monthly_payment - interest_paid
    
    print "Principal Paid:",principal_paid
    
    remaining_balance = outstanding_balance - principal_paid
    
    print "at the end of the month the remaining balance is:",remaining_balance
    outstanding_balance = remaining_balance
    total_principal_paid = total_principal_paid + principal_paid
    total_interest = total_interest + interest_paid
    month+=1
    print "\n"
total_amount_paid = total_interest + total_principal_paid
print "Total Amount Paid:",total_amount_paid
print "Total Principal Paid:",total_principal_paid
print "Total Interest Paid:",total_interest
print "Remaining Balance:",remaining_balance




    
    
    






































#paying off debt in a year

