# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 18:00:47 2022

@author: DAVID
"""

from random import randint
filas=int(input("Ingrese el numero de filas: "))
columnas=int(input("Ingrese el numero de colmnas: "))
def llenar_matriz(n):
    matriz=[]
    for r in range(filas):
        fila=[]
        for c in range(columnas):
            fila.append(randint(4, 30))  
        matriz.append(fila)
    return matriz
resultado=llenar_matriz(5)

print(resultado)
for lista in resultado:
    maximo=max(lista)
    i_max=lista.index(maximo)
    print(f"El maximo es ",{maximo},"que se encuentra en ",{i_max})
