#faça um programa que tenha uma lista chamada números e duas funções chamada sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma
#entre todos os valores PARES sorteados pela função anterior
import random

def sorteia():
    numeros = []
    
    contador = 0
    
    while contador < 5 :
        numero = random.randint(0,100)
        numeros.append(numero)
        contador = contador +1

    return (numeros)
    
def somaPar():
    numeros = sorteia()

    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero

    print(numeros, soma)

somaPar()

