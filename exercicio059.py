#Crie um progrma que leia dois valores e mostre um menu na tela
#[1] somar, [2] multiplicar, [3] maior, [4] novos numero, [5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso 

variavel1 = int(input('Entre com o primeiro número: '))
variavel2 = int(input('Entre com o segundo número: '))


opcao = 0

while opcao != 5:
    opcao = int(input('Escolha uma opção:\n'
        '[1] Somar\n'
        '[2] multiplicar\n'
        '[3]  maior\n'
        '[4] Dividir\n'
        '[5] Sair\n'
        'Digite a sua opção: '))
    if opcao == 1:
        resultado = variavel1 + variavel2
        print(resultado)
    elif opcao == 2:
        resultado= variavel1 * variavel2
        print(resultado)
    elif opcao == 3:
        if variavel1 > variavel2:
            resultado = variavel1
            print(resultado)
        elif variavel2 > variavel1:
            resultado = variavel2
            print(resultado)
        else:
            print('Os dois são valores iguais')
    elif opcao == 4:
        print('esta opção entra com novos números')
        variavel1 = int(input('Entre com o novo primeiro número'))
        variavel2 = int(input('Entre com o novo segundo número'))
