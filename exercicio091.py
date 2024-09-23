# Crie um programa onde 4 jogadors joguem um dado e tenham resultados aleatorios.
# Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem,
# sabendo que o vencedor tirou o maior numero no dado

import random
from time import sleep
from operator import itemgetter

resultados = {
    'jogador1' : random.randint(0, 6),
    'jogador2' : random.randint(0, 6),
    'jogador3' : random.randint(0, 6),
    'jogador4' : random.randint(0, 6),
}

for jogador in resultados:

    print(f'O {jogador} tirou: {resultados[jogador]}')
    sleep(1)

rankin = {}
rankin = sorted(resultados.items(), key=itemgetter(1), reverse=True)

for contador, colocacao in enumerate(rankin):
    print(f'O {contador+1}° lugar foi o {colocacao[0]} com {colocacao[1]} pontos')

