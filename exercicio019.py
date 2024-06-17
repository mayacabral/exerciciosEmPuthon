#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import numpy as up
import random

alunos = []

for i in range(4):
    aluno = input(f'Qual o nome do aluno: ')
    alunos.append(aluno)


alunoSorteado = random.choice(alunos)

print(f'O aluno sorteado foi {alunoSorteado}')