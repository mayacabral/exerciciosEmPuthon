#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior

def maior(list):
    maior = menor = list[0]
    
    for numero in list:
        if numero > maior:  
            maior = numero
        if numero < menor: 
            menor = numero
    
    print(f'foram passados {len(list)} valores, sendo o maior {maior}')



valores = [18,5,2,6,3,7]
maior(valores)