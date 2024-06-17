#Crie um programa que leia um número inteiro e mostre na tela se ela é par ou impar


numero = int(input('Entre com um número: '))

if numero % 2 == 0:
    print(f'O numero {numero} é par')
else:
     print(f'O numero {numero} é impar')