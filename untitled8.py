# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 12:08:13 2022

@author: DAVID
"""

t=int(input("Ingrese el tamaño del vector: "))
a=[]
b=[]
for i in range(t):
    a.append([0])
    b.append([0])
for i in range(t):
    a[i]=int(input("Ingrese el elemento [{}]: ".format(i+1)))
for i in range(t):
    b[i]=int(input("Ingrese el elemento [{}]: ".format(i+1)))

print("a=",a)
print("b=",b)

def comparar(arr1,arr2,t):
    iguales=0
    for i in range(t):
        if arr1[i]==arr2[i]:
            iguales=+1
    return (iguales/t*100)
print("El porcentaje de similitud es: ",comparar(a, b, t))