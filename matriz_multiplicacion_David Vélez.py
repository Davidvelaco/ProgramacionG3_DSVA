# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:41:11 2022

@author: DAVID
"""

columnas=filas=0
while columnas<=0:
    columnas=int(input("coloque el numero de columnas:"))
while filas<=0:
    filas=int(input("Coloque el numero de filas:"))
print(" |",end="")
for i in range(1,filas+1):
	for j in range(1,columnas+1):
		print('{:3}'.format(i*j), end=" ")
	print()