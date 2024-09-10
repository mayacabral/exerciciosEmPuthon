# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares

tupla = ()
contador = 0
while contador < 4:
    numero = int(input('Entre com um número: '))
    tupla = tupla + (numero,)
    contador += 1

contador9 = 0
numeros_pares = []

for numero in tupla:
    if numero == 9:
        contador9 += 1

    if numero == 3:
        numero3 = tupla.index(numero) + 1

    if numero % 2 == 0:
        numeros_pares.append(numero)

print(f'\n Apareceram {contador9} numeros 9')
print(f' Os numeros pares são: {numeros_pares}')
print(f' O nuemro 3 foi o {numero3}º número a ser digitado')