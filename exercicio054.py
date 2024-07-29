#Crie um programa que leia o ao de nascimento de sete paessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

import datetime
now = datetime.datetime.now()
ano_atual = now.year

soma_maior_idade = 0
soma_menor_idade = 0

for c in range(0,7):
    ano = int(input('Qual o ano de nascimento: '))
    idade = ano_atual - ano
    if idade > 18:
        soma_maior_idade += 1
    else:
        soma_menor_idade += 1
        

print(f'São {soma_maior_idade} maiores de idade')
print(f'São {soma_menor_idade} menores de idade')