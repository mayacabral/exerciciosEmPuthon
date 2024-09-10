# Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
# Depois disso, você deve mostrar, para cada palavra, aqui são as vogais

palavras = ('python', 'programacao', 'linguagem', 'computador', 'codigo', 'dados', 'algoritmo', 'funcao', 'variavel', 'biblioteca')

for palavra in palavras:
    print(f' \n As vogais da plavra {palavra} são: ',end= '')
    for letra in palavra:
        if  letra.lower() in 'aeiou':
            
            print(letra ,end= '')
       