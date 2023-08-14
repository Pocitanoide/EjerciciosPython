# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:21:37 2023

@author: aleja
"""
''' 1. Se ingresan la edad de distintas personas, 
 de las cuales se quiere saber cuantas
 son menores de edad y cuantas son mayores o 
 iguales a 18 años, el ingreso de
 las edades finaliza con la edad -1.'''

'''2.1. The ages of different individuals are 
# entered, of which it is desired to know how 
# many are under the age of 18 and how many are
#18 years old or older. The input of ages ends 
#with the age of -1.'''

eleccion=-1
edad=0
contadormas18=0
contadormenos18=0
while eleccion==-1:
    print("Ingrese la edad de la persona")
    edad=int(input())
    if edad==-1:
        eleccion=1
    if edad>=18:
        print("La persona es mayor de edad")
        contadormas18+=1
    else:
        print("La persona es menor de edad")
        contadormenos18+=1            
else:
    print("Las cantidad de personas menor de edad es", contadormenos18)
    print("La cantidad de personas mayores de edad es:", contadormas18)