#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km, mostre uma menssagem dizendo que ele foi multado.
#A multa vai custar 7,00 por cada Km acima do limite

numero = int(input('Qual a velocidade atingida pelo carro? '))

if numero > 80:

    multa = (numero - 80)*7
    print(f'O valor da sua multa é {multa}')

else:
    print(f' Você não atingiu o valor máximo')