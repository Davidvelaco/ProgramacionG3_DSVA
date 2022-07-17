# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:13:57 2022

@author: lab
"""

A=[[1,2,3,7],[4,5,6,8]]
for fila in A:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()

vec=[]
t=len(A)*len(A[0])

for i in range(len(A[0])):
    for j in range(len(A)):
        val=A[j][i]
        vec.append(val)
print(vec)

print() 



    