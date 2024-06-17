#Crie um programa que leia o nome completo de uma pessoa e mostre
#O nome com todas as letraas maiusculas 
#O nome com todas as letras minusculas
#Quantas letras ao todo (sem considerar os espaços)
#Quantas letras tem o primeiro nome

nome = input('Entre com um nome: ')


maiuscula = nome.upper()
print(f'{maiuscula}')

minuscula = nome.lower()
print(f'{minuscula}')

quantidadeSemOsEspaços = len(nome) - nome.count('')
print(f'{quantidadeSemOsEspaços}')

primeiraLetra = nome.title()
separa = primeiraLetra.split()
print(f'Seu primeiro nome é {separa[0]}')

