# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 12:27:13 2022

@author: DAVID
"""

import math
def digitoizquierdo(n):
    while n>10:
        n=math.trunc(n/10)
    return n

x=int(input("Digite un numero: "))
print("el primer digito es:",digitoizquierdo(x))

y=int(input("Digite un numero: "))
print("el primer digito es:",digitoizquierdo(y))