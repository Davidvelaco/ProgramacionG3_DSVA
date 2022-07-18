# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:27:58 2022

@author: DAVID
"""

def isPrime(n):
    for i in range (2,n):
        if n % i == 0:
            return False
        else: 
            return True
    
for i in range (1,20):
    if isPrime(i+1):
        print (i+1)    
print()