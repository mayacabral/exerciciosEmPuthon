#Crie umprograma que faça o computador jogar jokenpô com você

import random

palavras = ['pedra', 'papel','tesoura']

palavra_sorteada = random.choice(palavras)

jogador = input('Qual a sua escolha? pedra, papel ou tesoura? ').lower().replace(" ", "")

if jogador == palavra_sorteada:
    print('Ninguém ganha! Tente novamente')
elif palavra_sorteada == "pedra" and jogador == "papel":
    print('Papel ganha de pedra, o jogador ganhou')
elif palavra_sorteada == "pedra" and jogador == "tesoura":
    print('pedra ganha de tesoura, o computador ganhou')
elif palavra_sorteada == "papel" and jogador == "pedra":
    print('papel ganha de pedra, o computador ganhou')
elif palavra_sorteada == "papel" and jogador == "tesoura":
    print('tesoura ganha de papel, o jogador ganhou')
elif palavra_sorteada == "tesoura" and jogador == "pedra":
    print('pedra ganha de tesoura, o jogador ganhou')
elif palavra_sorteada == "tesoura" and jogador == "papel":
    print('tesoura ganha de papel, o computador ganhou')




