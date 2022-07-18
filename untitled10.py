# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 12:23:20 2022

@author: DAVID
"""
import math
t=int(input('Ingrese el tamaño del vector:'))
a=[]

for i in range(t):
    a.append([0])

for i in range(t):
    a[i]=int(input('Ingrese el elemento a[{}]:'.format(i+1)))   

def media(vec,t):
    acu=0
    for i in range(t):
        acu=acu+vec[i]
    return (acu/t)

def varianza(vec,t):
    acu=0
    for i in range(t):
        acu=float(acu+(vec[i]-media(vec, t))**2)
    return (acu/t)
        
print("a =",a)
print("la media es: ",media(a,t))
print("La varianza es: ",varianza(a, t))
print("La desviacion estandar es: ",math.sqrt(varianza(a,t)))
    