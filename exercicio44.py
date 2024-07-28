#Elabora um programa que calcula o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
#A vista (dinherio/cheque): 10% de desconto
#A vista (cartão): 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

produto = float(input('Qual o valor do produto? '))
desconto = input('Qual a forma de pagamento?  ').lower().replace(" ", "")

if desconto == "dinheiro" or desconto == "cheque":
    desconto = produto * 0.1
    produtoFinal = produto - desconto
    print(f'O desconto será de: {produtoFinal} reais')
elif desconto == "cartao":
    desconto = produto * 0.05
    produtoFinal = produto - desconto
    print(f'O desconto será de: {produtoFinal} reais')