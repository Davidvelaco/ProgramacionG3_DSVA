# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:55:20 2022

@author: lab
"""

A=[['a','b','c'],['d','e','f'],['g','h','i']]
print()
for fila in A:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()
i=2
columna=[fila[i] for fila in A]
print(columna)