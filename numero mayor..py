# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:56:16 2022

@author: DAVID
"""

num1=int(input("Digite el numero:"))
num2=int(input("Digite el numero:"))
num3=int(input("Digite el numero:"))
def max(num1,num2,num3):
	if num1>num2 and num1>num3:
		return num1
	elif num2>num3:
		return num2
	return num3
print("  ")
print("El numero mayor es :",max(num1, num2, num3))