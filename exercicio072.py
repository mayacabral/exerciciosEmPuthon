# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vente.
# Seu programa deverá ler um número pelo teclado (ente 0 e 20) e mostrá-la por extenso

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 
            'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente', end = '')

print(f'VOcê digitou o número {contagem[numero]}')
