#faça um jogo (usando while) onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

import random

contador = 0
numeroUsuario = int(input('Entre com um número entre 0 e 10: '))
numeroComputador = random.randint(1,10)

while numeroUsuario != numeroComputador:
    if numeroUsuario > 10 or numeroUsuario < 0:
        numeroUsuario = int(input('Número invalido, entre com um número entre 0 e 10! '))
    else:
        contador += 1
        numeroUsuario = int(input('Você não adivinhou! Entre novamente com outro número: '))

print(f'PARABÉNS você adivinhou! O número que eu pensei foi {numeroComputador}, foram necessárias {contador} tentativas!')
        
