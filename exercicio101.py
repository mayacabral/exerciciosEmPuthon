#Crie um programa que tenha uma função chamada voto( ) que vai recebercomo parametro
#o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,OPCIONAL ou OBRIGATORIO
#nas eleições
from datetime import date


def eleicao (ano):
    data_hoje = date.today()
    ano_atual = data_hoje.year

    validacao = ano_atual - ano 

    if validacao < 16:
        return f'Com {validacao} VOTO: NEGADO'
    elif validacao == 16 and validacao < 18:
        return f'Com {validacao} VOTO: OPCIONAL'
    elif validacao >= 18 and validacao <= 70 :
        return f'Com {validacao} VOTO: OBRIGATORIO'
    else:
        return f'Com {validacao} VOTO: OPCIONAL'
    


ano = int(input(f'Em que ano você nasceu? '))
print(eleicao(ano))