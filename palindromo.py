# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:28:22 2022

@author: DAVID
"""

numero=input("Digite un número: ")
if str(numero)==str(numero)[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")