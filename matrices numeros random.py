# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:32:26 2022

@author: DAVID
"""

from random import randint

m=[0]*4
for i in range(4):
    m[i]=[0]*4
    
for j in range(4):
    for h in range(4):
        t=randint(0, 1000)
        m[j][h]=t
        
for j in range(4):
    for h in range(4):
        print(m[j][h],end=" ")
    print("")