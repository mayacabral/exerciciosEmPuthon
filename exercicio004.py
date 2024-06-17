#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

n = input('Digite algo: ')

print(type(n))
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())