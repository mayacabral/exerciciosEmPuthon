#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessas cadastradas


def cadastrar(nome):
    pessoas = []
    pessoas.append(nome)
    return pessoas

def listar():
    pessoas = cadastrar()
    for pessoa in pessoas:
        print(f'{pessoa}')


while True: 
    escolha = input(
        "DIGITE 1 PARA: cadastrar nova pessoa\n"
        "DIGITE 2 PARA: listar pessoas\n"
        "DIGITE 6 PARA: sair\n"
    )

    match escolha:
        case "1":
           pessoa = cadastrar(input(' Qual nome você deseja cadastrar? '))
        case "2":
            listar()
        case "6":
            print(f"OBRIGADA E ADEUS!")
            break
        case _:
            print("Opção inválida. Tente novamente.\n")