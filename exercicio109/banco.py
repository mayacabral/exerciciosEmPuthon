#Crie um pacote chamdo utilidadesCev que tenham dois módulos internos chamdos moeda e dado
#Transfira todas as funções utilizadas nos desafios 107 e 108 para o primeiro pacote e mantenha tudo fechado

from utilidadesCev import moedas
from utilidadesCev import dados


dinheiro = dados.leiaDinheiro('OLÁ, BEM-VINDO AO CAIXA MÁGICO. QUANTO DE DINHEIRO VOCÊ QUER INVESTIR?')


print("\nPERFEITO! AGORA, O QUE VOCÊ DESEJA FAZER:")

while True: 
    escolha = input(
        "DIGITE 1 PARA: aumentar 1,00\n"
        "DIGITE 2 PARA: diminuir 1,00\n"
        "DIGITE 3 PARA: dobrar a quantia\n"
        "DIGITE 4 PARA: metade da quantia\n"
        "DIGITE 5 PARA: visualizar resumo\n"
        "DIGITE 6 PARA: sair\n"
    )

    match escolha:
        case "1":
            dinheiro =  moedas.aumentar(dinheiro)  
            print(f"O valor atualizado é: R$ {dinheiro:.2f}\n")
        case "2":
            dinheiro = moedas.diminuir(dinheiro)  
            print(f"O valor atualizado é: R$ {dinheiro:.2f}\n")
        case "3":
            dinheiro = moedas.dobrar(dinheiro)  
            print(f"O valor atualizado é: R$ {dinheiro:.2f}\n")
        case "4":
            dinheiro = moedas.metade(dinheiro)  
            print(f"O valor atualizado é: R$ {dinheiro:.2f}\n")
        case "5":
            resumo = moedas.resumo(dinheiro) 
        case "6":
            print(f"OBRIGADA E ADEUS!")
            break
        case _:
            print("Opção inválida. Tente novamente.\n")