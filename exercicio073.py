# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação
# Depois mostre:
# A)Apensa os 5 primeiros colocados
# B)Os ultimos 4 colocados da tabela
# C)Uma lista com os times em ordem alfabetica
# D)Em que posição na tabela está o time da Chapeconese

times = (
    'Palmeiras', 'Flamengo', 'Corinthians', 'Internacional', 'Atlético-MG',
    'Fluminense', 'Grêmio', 'Santos', 'Athletico-PR', 'Botafogo',
    'Fortaleza', 'Ceará', 'Bahia', 'Goiás', 'Coritiba',
    'Sport', 'Vasco', 'Cruzeiro', 'América-MG', 'Avaí'
)

print(f'A) Os cinco primeiros colocados são {times[:5]}')

print(f'B) Os ultimos quatro colocados são {times[-4:]}' )

print(f'C) Os times na ordem alfabética são: {sorted(times) }')
