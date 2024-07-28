#Refaça o desafio 035 e acrescente o recurso de mostrar que tipo de triangulo será formado


a =int(input('Entre com o valor: '))
b =int(input('Entre com o valor: '))
c =int(input('Entre com o valor: '))

if a<b+c and b<a+c and c<a+b:
    print('É possível construir um triângulo')
    if a == b == c:
        print(f' Todos os lados são iguais o triângulo é EQUILATERO')
    elif a == b or a == c or b == c:
        print(f' Dois dos lados são iguais, o triângulo é ISÓSCELES')
    else:
        print(f' Nenhum dos lados é iguais o triângulo é ISÓSCELES')
else:
    print('Não é possível construir um triângulo')

