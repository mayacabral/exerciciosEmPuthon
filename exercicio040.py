#Crie um programa que leia duas notas de um aluno e calcule a sua media, mostrando uma menssagem no final, de acordo com a media atingida
#Media abaixo de 5: reprovado
#Media entre 5 e 6.9 recuperação
#Media 7 ou superior: aprovado

nota1 = float(input('Qual o valor da primeira nota: '))
nota2 = float(input('Qual o valor da segunda nota: '))

media = (nota1 + nota2)/2

if media <= 5:
    print(f'O aluno está reprovado!')
elif 5 < media <= 6.9:
    print(f'O aluno está em recuperação')
elif media >= 7:
    print(f'Aluno aprovado!')