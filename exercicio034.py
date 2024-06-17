#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#Para salários superiores a R$1250, calcule um aumento de 10%
#Para os inferiors ou iguais, o aumento é de 15%


salario = float(input('Qual o valor do salario? '))

if salario > 1250:
    salario = (salario*0.1) + salario
    print(f'O salario fica por {salario}')
else:
    salario = (salario*0.15) + salario
    print(f'O salario fica por {salario}')