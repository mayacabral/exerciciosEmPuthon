#Faça um programa que leia o peso de cinco pessoas. No final. mostre qual foi o maior e o menor peso lido

maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'Qual o peso da {c}º?'))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')

