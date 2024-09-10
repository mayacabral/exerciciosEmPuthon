# Crie um programa onde o usuário digite uma expressão qualquer que use parentese.
# Seu aplicativo deverá analisar se a expressão passada está com parenteses abertos e fechados na ordem correta



expressao = list(input(f'Digite uma expressão: '))

contador = 0
for elementos in expressao:
    if '(' in expressao or ')' in expressao:
        contador += 1

if contador%2 == 0:
    print('Expressão válida!')
else:
    print('Expressão invalida!')