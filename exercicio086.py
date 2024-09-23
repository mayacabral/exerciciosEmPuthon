# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final mostre a matriz na tela, com a formatação correta


lista = [[0,0,0],[0,0,0],[0,0,0]]

for elemento_externo in range(0,3):
    for elemento_interno in range(0,3):
        lista[elemento_externo][elemento_interno] = int(input(f'Digite um valor: '))

for elemento_externo in range(0,3):
    for elemento_interno in range(0,3):
        print(f'[{lista[elemento_externo][elemento_interno]}]', end ='')
    print()