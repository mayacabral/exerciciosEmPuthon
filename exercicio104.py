#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
#só que fazendo a vaidação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n')


def leiaInt(numero):
    if numero.isdigit():
        print(f'Você acabou de digitar o número {numero}')
    else:
        print(f'ERRO! Digite um número inteiro válido')


numero = input(f'Digite um número: ')
leiaInt(numero)