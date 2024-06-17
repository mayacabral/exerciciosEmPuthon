#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input('Qual o preço do produto? '))

desconto = n * 0.05
n2 = n - desconto

print(f'O novo preço do produto é {n2}')