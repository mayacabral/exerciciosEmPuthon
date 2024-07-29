#Faça um programa que calcula a soma entre todos os numeros impares que são multiplos de três e que se encontram no inintervalo de 1 até 500


soma = 0
for c in range(0, 10):
    if c%3 == 0:
        print(f'os multiplos de 3 são {c}')
        soma += c
print(soma)

