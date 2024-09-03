# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuario. O programa será interrompido quando o numero solicitado for negativo

while True:
    valor = int(input(' Entre com um novo numero (numero negativo faz parar): '))
    if valor < 0:
        print('Numero negativo, o programa foi interrompido...')
        break

    for valores in range(1, 11):
        tabuada = valor * valores
        print(f'{valor} x {valores} = {tabuada}')