#Faça um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opcionais:
#o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente



def ficha(nome='', gols=''):
    if not nome.strip():
        nome = 'desconhecido'

    if not gols.isdigit():
        gols = 0
    else:
        gols = int(gols)
        
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato')
    

nome = input(f'Nome do jogador: ')
gols = input(f'Número de Gols: ')
ficha(nome,gols)
