#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um numero de tipo invalido
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt():
    while True:
        try:
            num_inteiro = int(input('Digite um inteiro: '))
        except (ValueError, TypeError):
            print('ERRROUUUU')        
        except (KeyboardInterrupt):
            print('O usuário preferil não diditar um numero, portanto será 0') 
            num_inteiro = 0
        else:
            return num_inteiro    

def leiaFloat():
    while True:
        try:
            num_real = float(input('Digite um real: '))
        except (ValueError, TypeError):
            print('ERRROUUUU')
        except (KeyboardInterrupt):
            print('O usuário preferil não diditar um numero, portanto será 0') 
            num_real = 0    
        else:
            return num_real   

inteiro = leiaInt()
real = leiaFloat()
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')