#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos: junior
#até 20 anos: sênior
#acima: master


data = int(input('Qual o ano de nascimento do atleta? '))

idade = 2024 - data

if idade <= 9:
    print(f'atleta com {idade} anos é da categoria MIRIM')
elif 9 < idade <= 14: 
    print(f'atleta com {idade} anos é da categoria INFANTIL')
elif 14 < idade <= 19: 
    print(f'atleta com {idade} anos é da categoria JUNIOR')
elif 19 < idade <= 20: 
    print(f'atleta com {idade} anos é da categoria SÊNIOR')
else:
    print(f'atleta com {idade} anos é da categoria MASTER')