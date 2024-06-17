#Desenvolva um programa que pergunte a distancia de uma viagem em Km.
#Calcule o preço da passagem, cobrando 0,50 por km para viagens de até 200km
#E 0,45 para viagens mais longas


viagem = int(input('Qual a distância da viagem? '))

if viagem <= 200: 
    viagem = viagem * 0.5
    print(f'O valor final da viagem é R$ {viagem}')
else:
    viagem = viagem * 0.45
    print(f'O valor final da viagem é R$ {viagem}')