# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 19:15:17 2023

@author: aleja
"""

''' Se ingresan 2 números A y B de los cuales se le pide 
a usted mostrar por pantalla cuando A es mayor que B, 
o cuando B es mayor que A, también debe mostrar por 
pantalla cuando A y B son iguales.
'''
''' You input 2 numbers, A and B, and you are asked to 
display on the screen when A is greater than B or when 
B is greater than A. You should also display on the screen
 when A and B are equal.'''

A=None
B=None
A=int(input("Ingrese el número A "))
B=int(input("Ingrese el número B "))
if A>B:
    print("A es mayor que B")
elif A==B:
    print("A y B son iguales")
else:
    print("B es mayor que A")