#Faça um programa que leia a largura e a altura de uma parede
#em metros, calcule a sua área e a quantidade de tinta necessária
#para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m2


l = float(input(f'Qual a largura? '))
a = float(input(f'Qual a altura? '))

area = l * a

tinta = area/2 

print(f' A area da sua parede é {area}m^2 e serão necessários {tinta} litros de tintas')