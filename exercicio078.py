#Faça um programa que leia 5 valores numericos e guarde em uma lista
#No final, mostre qual foi a maior e o menor valor digitados e as suas respectivas posições


valores = []
contador = 0
numero_maior = 0
numero_menor = None


while contador < 5:
    numero = int(input(f'Entre ocm um número: '))
    valores.append(numero)
    if contador == 0:
        numero_menor = numero
    contador +=1

for valor in valores:
    if valor > numero_maior:
        numero_maior = valor
    if valor < numero_maior:
        numero_menor = valor
   
print(valores)
print(f' O maior numero é {numero_maior} e o menor é {numero_menor}')