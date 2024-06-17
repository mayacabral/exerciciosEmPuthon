#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

n = float(input('Entre com o valor em metros: '))

centimetros = n*100
milimetros = n*1000

print(f'{n} metros equivalem a {centimetros} cm e {milimetros} mm')