# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:25:54 2021

@author: ABIOLA
"""

def evaluate_poly(poly,x):
    
    """This function evalates a polynomial function for a given values of x.It takes
    a tuple of numbers poly and a number x. x and each element of poly is a float."""
    # power = The index of a number in the tuple represents power
    #coefficient = The value of a number in the tuple at a particular index, represents the coefficient for that term 
    # product_term = multiplication of the coefficient by the x value raised to power
    print "EVALUATE POLYNOMIAL"
    poly = tuple(poly)
    x = float(x)
    
    sum = 0
    for power in range(len(poly)):
       # print num
        
        if poly[power] != 0.0:
            coefficient = poly[power]
        
            product_term = (coefficient * (x ** power))
            
            sum = sum + product_term
        else:
            continue
   
    print poly,"evaluated at, f(x) =",x," =",sum
    return sum
poly = (0.0,0.0,5.0,9.3,7.0)
#x = -13
#print evaluate_poly(poly,x)
#
#print "\n\n"
#
def compute_deriv(poly):
    """This function computes the derivative of a polynomial function.It takes in a
    tuple of numbers called poly and return the derivative, which is also a polynomial represented
    as a tuple."""
        # power = The index of a number in the tuple represents power
    #coefficient = The value of a number in the tuple at a particular index, represents the coefficient for that term
    #derivative = tuple, which is a polynomial representation of the derivative of poly
    print "COMPUTE DERIVATIVE"
    
    derivative = ()
    for power in range(len(poly)):
        #n = len(poly) - 1
        if power == 0:
            print "derivative of a constant is 0"
            continue
        
        else:
            
            coefficient = power * poly[power]
           
            derivative = derivative + (coefficient,)
    print "Derivative of",poly," =",derivative
    return derivative
print compute_deriv(poly)



    
