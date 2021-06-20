# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:31:23 2021

@author: Jozua Palandi
"""
# Absolute Value

def absolute_value(num): 
    """This function returns the absolute 
    value of the entered number""" 
    if num >= 0: 
        return num 
    else: 
        return -num 
print(absolute_value(2)) 
print(absolute_value(-4)) 