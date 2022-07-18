# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:31:10 2022

@author: DAVID
"""
t=int(input("Ingrese el tamaño del vector: "))
a=[]
b=[]
acu1=0
acu2=0
for i in range(t):
    a.append([0])
    b.append([0])
for i in range(t):
    a[i]=int(input("Ingrese el elemento [{}]: ".format(i+1)))
    acu1=acu1+a[i]
for i in range(t):
    b[i]=int(input("Ingrese el elemento [{}]: ".format(i+1)))
    acu2=acu2+a[i]
    
print("a=",a)
print("La suma es= ",acu1)
print("b=",b)
print("La suma es= ",acu2)