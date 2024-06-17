#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo

a =int(input('Entre com o valor: '))
b =int(input('Entre com o valor: '))
c =int(input('Entre com o valor: '))

if a<b+c and b<a+c and c<a+b:
    print('É possível construir um triângulo')
else:
    print('Não é possível construir um triângulo')