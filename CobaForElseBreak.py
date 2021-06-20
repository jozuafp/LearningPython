# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:05:03 2021

@author: Jozua Palandi
"""
#Coba For Else Break
#Program to display student's marks from record 
student_name = 'Soyuj' 
marks = {'James': 90, 'Jules': 55, 'Arthur': 77} 
for student in marks: 
    if student == student_name: 
        print(marks[student]) 
        break 
else: 
    print('No entry with that name found.') 