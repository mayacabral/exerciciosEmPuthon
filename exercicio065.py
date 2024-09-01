#Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução,
#mostre a media entre todos os valores e qual foi o maior e o menor valores lidos
#O progrmaa deve perguntar ao usuario se ele quer ou não continuar a digitar 



soma = 0
contador = 0
continuar = True
numroMaior = 0
numeroMenor = 0

while continuar == True:

    numero = int(input('Entre com um numero: '))
    soma = numero + soma

    contador += 1
    resposta = input('Digite sim [s] para continuar ou não[n] para parar!').lower()
    if resposta == 'n':
        continuar = False

    if numero > numroMaior :
        numroMaior =  numero
    elif numroMaior < numero :
        numeroMenor  = numero
    
    

media = soma/contador

print(media)
print(f'O maior numero é {numroMaior} e o menor é {numeroMenor}')