#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

numero1 = int(input('Entre com o primeiro numero: '))
numero2 = int(input('Entre com o segundo numero: '))
numero3 = int(input('Entre com o terceiro numero: '))

#verificação de quem é menor
menor = 0
if numero2<numero1 and numero2<numero3:
    menor = numero2
if numero3<numero1 and numero3<numero2:
    menor = numero3

#verificação de quem é o maior
maior = 0
if numero2>numero1 and numero2>numero3:
    maior = numero2
if numero3>numero1 and numero3>numero2:
    maior = numero3

print(f'O menor valor é {menor}')
print(f'O menor valor é {maior}')