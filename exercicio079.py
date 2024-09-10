#Crie um programa onde o usuario possa digitar varios valores numericos
#e cadastre-os em uma lista. Caso o número já exista lá dentro ela não será adicionada.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente

lista = []
contador = 0
resposta = True
while resposta == True:
    numero = int(input(f'Digite um numero: '))    
    if numero not in lista:
        lista.append(numero)

    resposta_usuario = input(f'Deseja continuar? [S/N]').lower()
    if resposta_usuario == 'n':
        resposta = False

lista_ordenada = sorted(lista)

print(lista_ordenada)