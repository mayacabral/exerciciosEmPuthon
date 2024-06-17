#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
#O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será nagado


casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do salário? '))
anos = int(input('Quantos anos você pretende pagar? '))


anos = anos * 12

parcela = casa/anos

if parcela <= (salario*0.3):
    print(f'Parabéns! Seu emprestimo foi aprovado!')
else:
    print(f'Seu emprestimo foi reprovado! A parcela ficaria de {parcela}')