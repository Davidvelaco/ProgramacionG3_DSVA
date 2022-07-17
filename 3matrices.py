# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:30:24 2022

@author: lab
"""

A=[[2,4,5],[5,6,7],[4,6,7],[4,6,7]]
B=[[2,4,5],[5,6,7]]
C=[[2,4,5],[5,6,7],[4,1,5]]

print()
for fila in A:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()

for fila in B:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()

for fila in C:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()
