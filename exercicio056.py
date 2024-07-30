#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final doo progrmaa, mostre:
#A media de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos

somaIdade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1,5):
    nome = input(f'Qual o nome da {c}º apessoa? ')
    idade = int(input(f'Qual a idade da {c}º pessoa? '))
    sexo = input(f'Qual o sexo da {c}º pessoa? ')

    somaIdade += idade  
    mediaIdade = somaIdade/4

    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


print(idade)