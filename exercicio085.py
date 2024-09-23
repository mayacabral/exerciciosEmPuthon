# Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que 
# mantenha separados os valores pares e imapares. No final, mostre os valores pares e impares em ordem crescente

contador = 0
lista = [[],[]]

while contador < 7:
    numero = int(input(f'Entre com um numero: '))
    if numero%2 == 0:
        lista[0].append(numero)
    elif numero%2 != 0:
        lista[1].append(numero)

    contador += 1

print(f'Os numeros pares são: {lista[0]} e os numeros impares são: {lista[1]}')
