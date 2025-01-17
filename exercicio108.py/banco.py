

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
)

# Verifica a escolha usando match-case
match escolha:
    case "1":
        dinheiro = aumentar(dinheiro) 
    case "2":
        dinheiro = diminuir(dinheiro)  # Atualiza o valor
        print(f"O valor atualizado é: R$ {dinheiro:.2f}")
    case "3":
        dinheiro = dobrar(dinheiro)  # Atualiza o valor
        print(f"O valor atualizado é: R$ {dinheiro:.2f}")
    case "4":
        dinheiro = metade(dinheiro)  # Atualiza o valor
        print(f"O valor atualizado é: R$ {dinheiro:.2f}")
    case _:
        print("Opção inválida. Tente novamente.")