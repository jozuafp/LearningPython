# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:36:45 2021

@author: Jozua Palandi
"""

def factorial(x): 
    """This is a recursive function 
    to find the factorial of an integer""" 
    if x == 1: 
        return 1 
    else: 
        return (x * factorial(x-1)) 
num = 3 
print("The factorial of", num, "is", factorial(num)) 