# Faça um programa que jogue par ou impar com o computador. O jogo será interrompido
# quando o jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo

import random

contador = 0

while True:
    jogador = str(input('Par ou impar? ')).lower().replace(" ","")
    if jogador == 'impar':
        jogador = 1
    elif jogador == 'par':
        jogador = 2
    else:
        print('entre com o valor par ou impar')
        break
    
    numero_jogador = int(input('Qual o seu número? '))

    computador = random.choice([1, 2])

    if computador == 1:
        computador = 'impar'
    elif computador == 2:
        computador = 'par'

    numero_computador = random.choice([1, 10])

    resultado = numero_jogador + numero_computador


    if resultado % 2 != 0 and jogador == 1:
        contador += 1
        print(f'O computador escolheu {computador} e jogou {numero_computador}. Sendo assim o resultado é {resultado} que é impar e você ganhou!')
    elif resultado % 2 == 0 and jogador == 2:
        contador += 1
        print(f'O computador escolheu {computador} e jogou {numero_computador}. Sendo assim o resultado é {resultado} que é par e você ganhou!')
    else:
        break

print(f'O computador escolheu {computador} e jogou {numero_computador}.Sendo assim o resultado é {resultado} e infelizmente você perdeu, com {contador} vitorias')