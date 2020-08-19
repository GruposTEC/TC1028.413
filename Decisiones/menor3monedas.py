#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:07:17 2020

@author: avmejia
"""

#Algoritmo Menor a tres;
#Recibir Primera moneda;
#recibir Segunda moneda;
#Recibir Tercera moneda;
#if moneda1 < moneda2{
#  menor es la moneda 1;
#  imprimo que la menor es la moneda1;
#}
#else{
#  menor es la moneda 2;
#  imprimo que la menor es la momneda2
#}
#if moneda3 < menor{
#  menor es la moneda 3
#}
#Imprimir cual es la menor;
#Fin

moneda1 = int(input())
moneda2 = int(input())
moneda3 = int(input())
if moneda1 < moneda2:
    menor = moneda1
    print(f'El menor hasta ahora es la moneda 1 : {moneda1}')
    if menor == 100:
        print("Me gane la loteria")
elif moneda2 < moneda1:
    menor = moneda2
    print(f'El menor hasta ahora es la moneda 1 : {moneda2}')
else:
    menor = moneda1    
if moneda3 < menor :
    menor = moneda3
print(f'La moneda de menor denomicacion es la de {menor} pesos')