# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:50:48 2022

@author: DAVID
"""
n=int(input("Ingresa un numero: "))
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return "No es primo"
    return "Es primo"
print(isPrime(n))
