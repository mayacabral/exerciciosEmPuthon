def aumentar(dinheiro):
   dinheiro +=1
   return dinheiro     

def diminuir(dinheiro):
    dinheiro -=1
    return dinheiro

def dobrar(dinheiro):
    dinheiro *= 2
    return dinheiro

def metade(dinheiro):
    dinheiro = dinheiro/2
    return dinheiro


def resumo(dinheiro):
    aumento = float(input(' Quantos por cento você deseja aumentar? '))
    diminuir = float(input(' Quantos por cento você deseja adiminuir? '))

    valor_aumento = (dinheiro * (aumento/100)) + dinheiro
    valor_diminuir = dinheiro - (dinheiro * (diminuir/100)) 

    largura = 60  
    print('--' * 30)
    print("RESUMO".center(largura))
    print('--' * 30)

    print(f'Preço analisado: {dinheiro}')
    print(f'Dobro do preço: {dobrar(dinheiro)}')
    print(f'Metade do preço: {metade(dinheiro)}')
    print(f'{aumento}% de aumento:  {valor_aumento}')
    print(f'{diminuir}% de redução: {valor_diminuir}')
    
    


   