#Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F'
#Caso esteja errado, peça a digitação novamente até ter um valor correto


sexo = str(input(f'Informe o sexo: [M/F]'))
while sexo not in 'MmFf':
    sexo = str(input('Dado invalido. Por favor digite [M/F]'))

print(f'Sexo {sexo} registrado com sucesso')