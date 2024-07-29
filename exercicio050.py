#Faça uma tabuada usando for do numero que o usuario digitar

numero = int(input('Entre com um número: '))

for c in range(0,11):
    multiplicacao = numero * c
    print(f' {c} vezes {numero} = {multiplicacao}')