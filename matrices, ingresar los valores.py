# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:11:51 2022

@author: DAVID
"""

matriz=[]
filas=4
columna=4
for i in range(filas):
    f=int(input("Ingrese los numero de filas: "))
    matriz.append([f])
    for j in range(columna-1):
        c=int(input("Ingrese los numeros de la columna"))
        matriz[i].append(c)
import random
    
