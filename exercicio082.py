# Crie um programa que vai ler varios numeros e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteudo das três listas geradas

lista = []
valor = True
lista_par = []
lista_impar = []

while valor == True:
    numero = int(input(f'Digite um numero: '))
    lista.append(numero)

    resposta = str(input(f'Deseja continuar? [S/N] ')).lower()
    if resposta == 'n':
        valor = False

for valores in lista:
    if valores%2 == 0:
        lista_par.append(valores)
    else:
        lista_impar.append(valores)

print(f'A lista geral é: {lista} \n A lista par é: {lista_par} \n A lista impar é: {lista_impar}')