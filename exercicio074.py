# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
from random import randint

tupla = ()
numero_maior = 0
numero_menor = 0

contador = 0 
while contador < 5:
    numero = randint(1,10)
    tupla = tupla + (numero,) 
    contador += 1

for numero_tupla in tupla:
    if numero_tupla < numero_maior:
        numero_menor = numero_tupla
    else:
        numero_maior = numero_tupla

    
print(f'Os números gerados são {tupla}')
print(f'O menor número gerado é {numero_menor}')
print(f'O maior valor que tem na tupla é: {numero_maior}')
