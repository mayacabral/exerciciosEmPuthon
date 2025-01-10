#Faça um programa que tenha uma função chamada area, que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno

def area(a,b):
    area = a*b
    print(f'A área de um terreno {a}x{b} é de {area}m²')

largura = int(input('LARGURA (m): '))
altura = int(input('ALTURA (m): '))
area(largura,altura)