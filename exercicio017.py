#Faça um programa que leia o comprimento do cateto oposto e cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math

catetoOposto = float(input('Entre com o cateto oposto: '))
catetoAdjacente = float(input('Entre com o cateto adjacente: '))

hipotenusa = math.sqrt(pow(catetoOposto, 2) + pow(catetoAdjacente, 2))

print(f' Sua hipotenusa é {hipotenusa}')