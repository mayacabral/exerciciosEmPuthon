#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci


numero = int(input(f'Quantos numeros da sequendcia de Fibonacci você quer exibir? '))
contador = 1

elemento = 0
resultado = 0
while contador < numero:
    
    resultado = resultado + elemento
    
    print(resultado)
    resultado += 1
    contador += 1