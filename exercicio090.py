# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionario. No final, mostre o conteudo da estrutura na tela

aluno = {}

aluno['nome']= str(input(f'Entre coom o nome: '))
aluno['nota'] = int(input(f'Entre com uma nota: '))

if aluno["nota"] >= 7:
    aluno["situacao"] = 'Aprovado'
elif aluno["nota"] >= 5:
     aluno["situacao"] = 'Recuperação'
else:
     aluno["situacao"] = "Reprovado"


for nomes, notas in aluno.items():
    print(f'{nomes} é igual a {notas}')