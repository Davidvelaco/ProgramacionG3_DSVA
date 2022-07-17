# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 16:52:38 2022

@author: DAVID
"""

def validar(nombre, edad, cedula, email):
    valido = True
    for i in nombre:
        if(i >= '0' and i <= '9'):
            valido = False
            print("Su nombre tiene algun error, intentelo de nuevo")
            return valido

    for i in edad:
        if(i >= '0' and i <= '9'):
            valido = True
        else:
            valido = False
            print("Su edad tiene algun error, intentelo de nuevo")
            return valido

    if (edad > '0' and edad < '90'):
        valido = True
    else:
        valido = False
        print("Su edad no es correcta")
        return valido

    numCedula = 0
    for i in cedula:
        if(i >= '0' and i <= '9'):
            numCedula = numCedula+1
            valido = True
        else:
            print("Su numero de cedula tiene algun error, intentelo de nuevo")
            valido = False
            return valido
    if (numCedula == 10):
        valido = True
    else:
        valido = False
        print("Su numero de cedula tiene mas o menos digitos")
        return valido

    indice = 0
    num = 0
    for i in email:
        if i == "@":
            indice = num
        num = num + 1

    if ( indice > 0 and email[indice:] == "@edu.ec"):
        valido = True
    else:
        print("Su email tiene algun error, intentelo de nuevo")
        valido = False
        return valido
            
    return valido


print(validar ("David Velez", "185", "17260264938", "dveleza2@edu"))