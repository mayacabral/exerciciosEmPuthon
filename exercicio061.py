#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progresaão uasndo a estrutura while


primeiroTermo = int(input('Entre com o número: '))
razao = int(input('Entre com a razao: '))

numero = primeiroTermo + razao
contador = 1

resultado = 0

resultado = 0

if primeiroTermo%2 == 0:
    resultado = primeiroTermo

while contador < 9 :
    
    if numero%2 == 0:
        resultado = resultado + numero
        
    numero = numero + razao
    contador += 1

print(resultado)