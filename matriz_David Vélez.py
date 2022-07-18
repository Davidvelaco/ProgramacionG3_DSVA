# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:03:22 2022

@author: DAVID
"""

fila=int(input("Ingrese el numero de filas: "))
columna=int(input("Ingrese el numero de columnas: "))
vector1=[]
vector2=[]
vector3=[]
for i in range(fila):
    vector1.append([])
    vector3.append([])
for i in range(fila):
    vector1[i]=int(input("elemetos fila{}: ".format(i+1)))
    
for i in range(columna):
    vector2.append([])
for i in range (columna):
    vector2[i]=int(input("Elemento columnas{}: ".format(i+1)))
print("   ",end=" ")

for i in range(len (vector2)):
    print(vector2[i], end="  ")
print()
for i in range(len(vector1)):
    for j in range(len(vector2)):
        valor=vector1[i]*vector2[j]
        vector3[i].append(valor)
        print(vector1[i],vector3[i],end="   ")
        print()