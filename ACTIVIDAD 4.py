# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 19:47:59 2023

@author: aleja
"""

'''Un supermercado necesita un programa donde la persona 
ingrese el nombre de los productos y el precio, se le pide
 a usted desarrollar la funcionalidad para que cuando termine
 de ingresar los productos, le muestre por pantalla el
importe total. Se debe tener en cuenta que la carga de datos 
finaliza con “Fin”.'''
'''A supermarket needs a program where the person enters the
 names of the products and their prices. You are asked to develop
 the functionality so that when they finish entering the products,
 it displays the total amount on the screen. It should be noted that
 data entry ends with "End."'''
cantidadproduc=0
preciototal=0
palabra=None
while palabra!="Fin":
    nombreproducto=input("Ingrese el nombre del producto ")
    precio=int(input("Ingrese el precio del producto "))
    palabra=input("Desea agregar otro producto?, si no desea agregar\
                  mas productos,ingrese la palabra Fin " )
    preciototal+=precio
else:
    print("El importe total de su compra es:", str(preciototal))
    