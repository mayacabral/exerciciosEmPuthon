#Crie um programa que leia varios nomes e o preço de varios produtos
#O progrmaa deverá perguntar se o usuario vai continuar. No final, mostre:

#A) Qual é o total gasto na compra
#B) Quantos produtos custam mais de R$100
#C) Qual é o nome do produto mais barato 
valor_da_compra = 0
contador_preco = 0
preco_barato = 0

while True: 
    preco = float(input('Qual o preço: '))

    produto = str(input('Qual o nome do produto: ')).lower().strip()[0]
    
    valor_da_compra = valor_da_compra + preco

    if preco > 100:
        contador_preco += 1
    
    if preco_barato < preco:
        produto_barato = produto

    continuar = ' '
    while continuar not in 'sn' :
        continuar = str(input('Quer continuar: [s/n]')).lower().strip()[0]
    if continuar == 'n':
        break

print(f'O total gasto na compra é {valor_da_compra}, foram passados {contador_preco} com mais R$ 100,00 e o produto mais barato é {produto_barato}')