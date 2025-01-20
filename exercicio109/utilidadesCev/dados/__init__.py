def leiaDinheiro(menssagem):
    while True:
        entrada = input(menssagem)
        
        if entrada.isdigit():
            return float(entrada)
        else:
            print(f'Não é um valor válido! tente apenas numeros')
        

