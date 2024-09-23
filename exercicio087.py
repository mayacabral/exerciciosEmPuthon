# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna 
# C) O maior valor da segunda linha

lista = [[0,0,0],[0,0,0],[0,0,0]]
todos_elementos_somados = 0
elementos_terceira_coluna_somados = 0
maior_valor_da_segunda_linhda = 0

for elemento_externo in range(0,3):
    for elemento_interno in range(0,3):
        lista[elemento_externo][elemento_interno] = int(input(f'Digite um valor: '))
        todos_elementos_somados = todos_elementos_somados + lista[elemento_externo][elemento_interno] 

for valores in lista[2]:
    elementos_terceira_coluna_somados = elementos_terceira_coluna_somados + valores
    
for valores in lista[1]:
    if valores > maior_valor_da_segunda_linhda:
        maior_valor_da_segunda_linhda = valores

print(f'A) A soma de todos os valores é: {todos_elementos_somados}')
print(f'B) A soma dos elementos da terceira coluna são: {elementos_terceira_coluna_somados}')
print(f'C) O maior valor da segunda coluna é: {maior_valor_da_segunda_linhda}')

