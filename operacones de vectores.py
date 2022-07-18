# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 13:09:01 2022

@author: DAVID
"""

Dimension1=int(input('Ingrese el rango inferior mayor que 5:'))
Dimension2=int(input('Ingrese el rango superior menor que 30:'))
Suma2=int(input('Ingrese que operacion desea: suma ingrese 1 , resta ingrese 2, multiplicaion ingrese 3 , division ingrese 4 '))

a=0
b=0

for i in range (Dimension1,Dimension2):
    
    if Dimension1>5:
        from random import randint,random,uniform
        a=randint(Dimension1,Dimension2)
    if Dimension1<=5:
        print(" ")
        print('Ingrese un numero mayor a 5')
        

    if Dimension2<30:
         from random import randint,random,uniform
         b=randint(Dimension1,Dimension2)
        
      
    else:
        print('Ingrese un numero mayor a 5') 
        
    if Suma2==1:
        SUMA2=a+b
        
    if Suma2==2:
        SUMA2=a-b
    if Suma2==3:
        SUMA2=a*b
    if Suma2==4:
        SUMA2=a/b
    
    
    vector3=Dimension1*Dimension2         
     
 
print(a,"  p ",b)    
print(SUMA2)