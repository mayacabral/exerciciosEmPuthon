# Faça um programa que leia nome e pesos de varias pessoas, guardndo tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

lista = []
contador = 0

mais_pesada = 0
mais_leve = 0

valor = True

while valor == True:
    nome = str(input(f'Digite o nome da pessoa: '))
    peso = int(input(f'Digite um numero: '))

    lista = [nome,peso]
    lista.append(peso)

    if peso > mais_pesada:
        mais_pesada = peso
    if peso < mais_pesada:
        mais_leve = peso

    resposta = str(input(f'Deseja continuar? [S/N] ')).lower()
    if resposta == 'n':
        valor = False

    contador += 1

print(f'Foram cadastradas {contador} pessoas. A mais pesada é {mais_pesada} e a mais leve é {mais_leve}')