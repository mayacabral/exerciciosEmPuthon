#Desenvolva um progrma que leia seis numeros inteiros e mostre a soma apenas daquele que forem pares.
#Se o valor digitado for impar, desconsidere

soma = 0
for c in range(1,6 +1):
    numero = int(input(f'Entre com {c}º número: '))
    if numero%2 == 0:
        soma += numero
print(soma)