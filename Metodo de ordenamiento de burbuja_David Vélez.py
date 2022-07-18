# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:02:58 2022

@author: DAVID
"""
vector1=0
aleatorio=0
    
import random
    
def vector_aleatorio(n):
    vector1=[0]*n
    for i in range(n):
        vector1[i]=random.randint(50,100)
    return vector1
print("Ingrese el tamaño del primer vector: ")
n=int(input())

import time
time.sleep(1)
print(" ")
        
aleatorio=vector_aleatorio(n)
print(aleatorio)
print(" ")
import time
time.sleep(1)

ascendente=sorted(aleatorio)
print("De forma ascendente: ",ascendente)



    