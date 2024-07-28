#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma menssagem 
# O primeiro valor é o maior, o segundo valor é o maior ou não existe valor maior, os dois são iguais

numero1 = int(input('Qual o primeiro valor: '))
numero2 = int(input('Qual o segundo valor: '))

if numero1 > numero2:
    print(f'O primeiro valor é maior')
elif numero2 > numero1:
    print(f'O segundo valor é maior')
elif numero1 == numero2:
    print(f'Não existe valor maior, os dois são iguais')