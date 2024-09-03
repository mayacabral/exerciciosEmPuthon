#Crie um programa que leia a idade e o sexo de varias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuario quer ou continuar.
#No final, mostre:
#A) Quantas pessoas tem mais de 18 anos
#B) QUantos homens foram cadastrados 
#C) Quantas mulheres tem mais de 20 anos 


while True: 
    idade = int(input('Qual a idade: '))

    genero = ' '
    while genero not in 'mf':
        genero = str(input('Qual o genero: [M/F] ')).lower().strip()[0]


    resultado_idade = 0
    if idade > 18 :
        resultado_idade += 1
    
    resultado_homens = 0 
    if genero == 'm':
        resultado_homens += 1

    resultado_mulheres = 0
    if genero == 'f' and idade > 20:
        resultado_mulheres += 1 
        resultado_idade += 1

    continuar = ' '
    while continuar not in 'sn' :
        continuar = str(input('Quer continuar: [s/n]')).lower().strip()[0]
    if continuar == 'n':
        break

print(f'Foram apresentados {resultado_idade} com mais de 18 anos. {resultado_homens} homens. E {resultado_mulheres} mulheres com mais de 20 anos.')