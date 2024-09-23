# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastro-os(com idade)
# em um dicionario se por acaso a CTPS for diferente de zero, o dicionario receberá também o ano de contratação
# e o salário. Calcule e acrescente, além da idade, com quantos alnos a pessoa vai se aposentar considerando que para se aposentar são 35 anos de contribuição

dados ={}
hoje =  2024

dados["nome"] = str(input(f'Entre com um nome: '))

ano_de_nascimento = int(input(f'Qual o ano de nascimento: '))

idade_usuario = hoje - ano_de_nascimento

dados["idade"] = idade_usuario 

dados["carteiraDeTrabalho"] = int(input(f'Qual o número da carteira de trabalho: '))
