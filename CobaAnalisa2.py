# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:12:17 2021

@author: Jozua Palandi
"""
#Coba Analisa 2

jawab = 'ya' 
hitung = 0 
while(True): 
    hitung += 1 
    jawab = input("Apakah Anda mau ulang lagi(ya/tidak)? ") 
    if jawab == 'tidak': 
        break 
 
print("Total perulagan: " + str(hitung))