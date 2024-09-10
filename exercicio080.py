#Crie um programa onde o usuario possa digitar cinco valores numericos
# e cadastre-os em uma lista, na na posição correta da inserção
#(sem usar o sort())

lista = []
for contador in range(0,5):
    numero = int(input(f' Digite um valor: '))
    if contador == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)