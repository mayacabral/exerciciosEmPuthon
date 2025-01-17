#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
#e vai retornar um dicionario com as seguinters informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A media da turma
# A situação(opcional)


def notas(*notas, situacao = False):
    quantidade = len(notas)

    maiorNota = notas[0]
    for nota in notas:
        if nota > maiorNota:
            maiorNota = nota

    menorNota = notas[0]
    for nota in notas:
        if nota < menorNota:
            menorNota = nota

    
    soma = 0
    for nota in notas:
        soma += nota
    media = soma/quantidade

    dados = dict()
    dados["total"] = quantidade
    dados["maior"] = maiorNota
    dados["menor"] = menorNota
    dados["media"] = media

    if situacao == True:
        if media >= 7:
           dados["situação"] = 'BOA'
        elif media >=5 and media < 7:
            dados["situação"] = 'razoavel'
        elif media < 5:
            dados["situação"] = 'ruim'



    print(dados)

notas(3,5,7,8,situacao = True)


