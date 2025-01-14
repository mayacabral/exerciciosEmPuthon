#Crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que indique o número a calcular e o outro chamado show,
#que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de calculo do faotrial



def fatoriais(num, show = False):
    """
    -> Calcula o Fatoria de um numero
    :param num: O numero a ser calculado
    :apram show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um numero    
    """

    fatorial = 1
    for fat in range(num, 0, -1):
        if show:
            print(fat, end='')
            if fat>1:
                print('x', end='')
        fatorial *= fat
    return fatorial




#print(fatoriais(5, show=False))
help(fatoriais)