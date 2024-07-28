#Faça um programa que leia o ano de nascimento de um jovem e infome, de acordo com sua idade:
# Se ele ainda vai se alitar ao serviço militar
#Se é a hora de se alistar 
#Se já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo


ano = int(input("Qual o ano de nascimento? "))
idade = 2024 - ano

if idade < 18:
    idade = 18 - idade
    print(f'Ele ainda vai se alistar ao serviço militar. Ainda faltam {idade} para ele se alistar.')
elif idade > 18 and idade < 45:
    print(f'É a hora de se alistar!')
else:
    idade = idade - 45
    print(f'Já se passaram {idade} anos do tempo do alistamento')