#Faça um programa que tenha uma função chamada contador(),que receba três parametros:inicio, meio e fim.
#e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
#a)de 1 até 10, de 1 em 1
#b)de 10 até 0, de 2 em 2
#c)uma contagem personalizada

def contador(inicio,fim,passo):

    if inicio < fim:    
        print("=-" * 20)
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
        for i in range(inicio, fim+1, passo):  
            print(f'{i}',end=' ')
        print("\n" )
        print("=-" * 20)
    elif fim < inicio :
        print("=-" * 20)
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
        for a in range(inicio, fim, -passo):  
            print(f'{a}',end=' ')
        print("\n" )
        print("=-" * 20)


contador(1,10,1)
contador(100,0,10)
print("=-" * 20)
print(f"AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!")
print("=-" * 20)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)