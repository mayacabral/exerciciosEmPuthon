#crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobrar() e metade()
#adicione ao modulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já 
# temos no modulo criado até aqui

from moeda import * 

try:
    dinheiro = int(input(f'OLÁ, BEM-VINDO AO CAIXA MÁGICO. QUANTO DE DINHEIRO VOCÊ QUER INVESTIR?'))
except ValueError:
    print("Valor inválido. Por favor, insira um número.")

print("\nPERFEITO! AGORA, O QUE VOCÊ DESEJA FAZER:")
escolha = input(
    "DIGITE 1 PARA: aumentar 1,00\n"
    "DIGITE 2 PARA: diminuir 1,00\n"
    "DIGITE 3 PARA: dobrar a quantia\n"
    "DIGITE 4 PARA: metade da quantia\n"
    "DIGITE 5 PARA: visualizar resumo\n"
)


match escolha:
    case "1":
        dinheiro = aumentar(dinheiro)  
        print(f"O valor atualizado é: R$ {dinheiro:.2f}")
    case "2":
        dinheiro = diminuir(dinheiro)  
        print(f"O valor atualizado é: R$ {dinheiro:.2f}")
    case "3":
        dinheiro = dobrar(dinheiro)  
        print(f"O valor atualizado é: R$ {dinheiro:.2f}")
    case "4":
        dinheiro = metade(dinheiro)  
        print(f"O valor atualizado é: R$ {dinheiro:.2f}")
    case "5":
        resumo = resumo(dinheiro) 
    case _:
        print("Opção inválida. Tente novamente.")