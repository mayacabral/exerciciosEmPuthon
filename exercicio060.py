#Faça um programa que leia um número qualquer e mostre o seu fatorial


numero = int(input('Entre com um número: '))

resultado = 1

while numero > 0:    
    resultado = resultado * numero
    numero -=  1
    
    
print(resultado)