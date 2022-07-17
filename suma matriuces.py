# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:41:50 2022

@author: lab
"""
acu=0
A=[[2,4,5],[5,6,7],[4,6,7],[4,6,7]]
print()
for fila in A:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()
i=0
columna=[fila[i] for fila in A]
print(columna)
print()
for i in range(len(A)):
    for j in range(A[i]):
        acu=acu+A[i][j]
print(acu)