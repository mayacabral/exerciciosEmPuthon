#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

n = int(input('Digite um numero: '))

dobro = n*2
triplo = n*3
raiz = math.sqrt(n)

print(f'O numero {n} tem como seu dobro {dobro}, seu triplo {triplo} e como sua raiz {raiz}')