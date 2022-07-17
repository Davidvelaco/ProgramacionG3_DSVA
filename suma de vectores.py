# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:15:44 2022

@author: DAVID
"""


vector1=[1,2,3,4,5,6]
vector2=[1,2,3,4,5,6]
vector3=[0]*6

for h in range(0,6):
 vector3[h]=vector1[h]+vector2[h]

for h in range(0,6):
  print(vector3[h],end=" ")
print(" ")
for h in range(0,6):
 vector3[h]=vector1[h]-vector2[h]

for h in range(0,6):
 print(vector3[h],end=" ")
print(" ") 
for h in range(0,6):
 vector3[h]=vector1[h]*vector2[h]

for h in range(0,6):
 print(vector3[h],end=" ")
print(" ") 
for h in range(0,6):
 vector3[h]=vector1[h]/vector2[h]

for h in range(0,6):
 print(vector3[h],end=" ")
