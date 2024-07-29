#Desenvolva uma programa que leia o primeiro termo de uma PA e a razão. noo final mostre os 10 primeiros termos dessa progressão

numero = int(input('Qual o primeiro numero de uma PA: '))
razao = int(input('Qual a razão da PA: '))
decimo = numero +(10-1) * razao
for c in range(numero, decimo + razao, razao):
    print('{}'.format(c), end = '--> ')
