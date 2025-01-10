#Faça um programa que tenha uma função chamada escreva, que receba um texto qualquer como parâmetro
#e mostre uma menssagem com tamanho adaptavel

def escreva(menssagem):
    tamanho = len(menssagem)
    print("~" * tamanho)
    print(menssagem)
    print("~" * tamanho)

escreva('paralelepipado')