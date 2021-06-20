# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:36:14 2021

@author: Jozua Palandi
"""

def greet(*names): 
    """This function greets all 
    the person in the names tuple.""" 
    # names is a tuple with arguments 
    for name in names: 
        print("Hello", name) 
greet("Monica", "Luke", "Steve", "John") 