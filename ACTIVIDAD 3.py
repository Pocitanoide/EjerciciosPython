# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 19:27:08 2023

@author: aleja
"""

''' Elaborar un programa que permita mostrar por pantalla, 
el sueldo promedio de un grupo de empleados. Debe tener 
en cuenta que la cantidad de empleados se ingresa por teclado'''

'''Create a program that allows displaying on the screen the 
average salary of a group of employees. It should take into 
account that the number of employees is entered through the 
keyboard.'''

nrodeempleados=0
sueldopromedio=0
sueldoempleado=0
nro=0
nrodeempleados=int(input("Ingrese la cantidad de empleados "))
while nro!=nrodeempleados:
    nro+=1
    sueldoempleado=int(input("Ingrese el sueldo del empleado "+ str(nro) 
                             +" "))
    sueldopromedio+=sueldoempleado
else:
    print("El sueldo promedio es: ", sueldopromedio/nrodeempleados)
    