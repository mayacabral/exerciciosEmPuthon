#Faça um programa que recebe quantos dias um carro foi alugado, quantos kilometros foram rodados e print o total a paga, 
#sabendoo que o carro custa R$60 por dia e R$0,15 por Km rodado

d = int(input('Quantos dias o carro passou alugado? '))
km = float(input('Quantos Km rodados? '))


custo = (d*60) + (km*0.15)

print(f'O total a pagar é {custo}')
