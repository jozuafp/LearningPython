# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:11:21 2021

@author: Jozua Palandi
"""
#Coba Analisa 1
total_belanja = int(input("Total belanja: Rp ")) 
bayar = total_belanja 
 
if total_belanja > 100000: 
    print("Kamu mendapatkan bonus minuman dingin") 
    print("dan diskon 5%") 
    diskon = total_belanja * 5/100 
    bayar = total_belanja - diskon 
 
print("Total yang harus dibayar: Rp ", bayar) 
print("Terima kasih sudah berbelanja") 
print("Datang lagi yaa...") 