# Crie um programa que vai ler variaveis numericas e colocar em uma lista
# Depois disso, mostre:
# A) Quantos numeros foram digitados
# B) A lista de valores, ordenada de forma decrescent
# C) Se o valor 5 foi digitado e está ou não na lista


lista = []
valor = True

while valor == True:
    numero = int(input(f'Digite um numero: '))
    lista.append(numero)

    resposta = str(input(f'Deseja continuar? [S/N] ')).lower()
    if resposta == 'n':
        valor = False


lista.sort(reverse=True)
if len(lista) == 1:
    print(f'Foi inserido {len(lista)} número na lista: {lista}')
elif len(lista) > 1:
    print(f'Foram inseridos {len(lista)} números na lista: {lista}')

if 5 in lista:
    print(f'O valro 5 fazz parte da lista! ')
else:
    print(f'Não foi digitado o número 5')
