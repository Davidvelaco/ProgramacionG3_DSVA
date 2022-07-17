# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:08:15 2022

@author: lab
"""

dinero=anios=interes=0
while(dinero<500):
    dinero=float(input("Ingrese la cantidad de dinero inicial: "))
while (anios<=0):
    anios=int(input("Ingrese el timepo(años): "))
while(interes<=0 or interes>10):
    interes=float(input("Ingrese el interes: "))
for i in range(1,anios*12+1):
    dinero+=(dinero*interes)/100
    print(f"Total de la póliza: {round(dinero,2)}")
    