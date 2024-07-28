#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: obesidade morbida

altura = float(input('Qual o valor da sua altura? '))
peso = float(input('Qual o valor da sua peso? '))

imc = peso/(altura*altura)

if imc <= 18.5:
    print(f'O paciente está abaixo do peso')
elif  18.5 < imc <= 25:
    print(f'O paciente está no peso ideal')
elif  25 < imc <= 30:
    print(f'O paciente está com sobrepeso')
elif  30 < imc <= 40:
    print(f'O paciente está com obesidade')
else:
    print(f'O paciente está com obesidade morbida')