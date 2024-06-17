#Faça um programa que leia um ângulo qualquer e mostre na ttela o valor do seno, cosseno e tangente desse ângulo

import math

n = int(input('Entre com o grau'))

seno = math.sin(math.radians(n))
cosseno = math.cos(math.radians(n))
tangente = math.tan(math.radians(n))

print(f"Seno de {n} graus: {seno}")
print(f"Cosseno de {n} graus: {cosseno}")
print(f"Tangente de {n} graus: {tangente}")
