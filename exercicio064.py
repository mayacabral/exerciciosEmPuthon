#Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles


numero = int(input('Qual o numero que você deseja? '))
contador = 0 
resultado = 0

while numero != 999:
    numero = numero + resultado
    contador += 1

    numero = int(input('Qual o numero que você deseja? '))
print(f' Foram {contador} numeros inseridos e {numero} o somatorio de todos eles')