#Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 9999,
#que é a condição de parada. No final, mostre quantos npumeros foram  digitados e qual foi a soma
#entre eles (desconsiderando o flag)

numero = 0
soma = 0
contador = 0

while numero != 999:
    numero = int(input('Entre com um número (999 faz parar): '))
    if numero != 999:
        soma = numero + soma
        contador += 1
    else:
        break

print(f'Foram digitados {contador} e a soma de todos eles é: {soma}')