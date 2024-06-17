#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

n = float(input('Qual o valor do seu salário? '))

porcento = n * 0.15
aumento = porcento + n

print(f'O valor ajustado do salário é {aumento}')