#Escreva um programa que leia um numero inteiro qualquer e paça para o usuario escolher qual será a base de conversão
#1 para binario, 2 para octal e 3 para hexadecimal


numero = int(input('Entre com um número: '))
escolha = int(input('Qual a base de conversão? '))

if escolha == 1:
    numeroBi = bin(numero)[2:]
    print(f'O numero {numero} na base binária é {numeroBi}')
elif escolha == 2:
    numeroOc = oct(numero)[2:]
    print(f'O numero {numero} na base octal é {numeroOc}')
elif escolha == 3:
    numeroHex = hex(numero)[2:]
    print(f'O numero {numero} na base hexadecimal é {numeroHex}')