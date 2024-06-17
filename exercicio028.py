#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5.
#Peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador
#O programa deverá escerver na tela se o seu usuariovenceu ou perdeu


import random


sorteio = random.randint(0, 5)

numero = int(input('qual o numero que o computador pensou: '))

if sorteio == numero:
    print(f'Parabens você certou! O numero que o computador pensou foi {sorteio}')
else:
    print(f'Sinto muito! O numero que o computaor pensou foi {sorteio}')