# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 12:33:11 2022

@author: DAVID
"""

numero=int(input("Ingresa un numero entero positivo: "))
resultado=0
while numero<0 or numero==0:
    print("Numero erroneo, intenta otra vez")
    numero=int(input("Ingresa un numero entero positivo: "))

if numero>0:

    for i in range(1,numero+1):
        resultado=resultado+(1/i)##nota esto es igual a poner resultado+=(1/i)
            
        print("El resultado es",resultado)