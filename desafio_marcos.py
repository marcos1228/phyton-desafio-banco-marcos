# Menu de opções
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Inicialização de variáveis
saldo = 100.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def obter_valor(mensagem):
    """Função para obter um valor float do usuário com validação"""
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("O valor deve ser positivo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Loop principal do programa
while True:
    opcao = input(menu).lower()

    match opcao:
        case "d":
            valor = obter_valor("Informe o valor do depósito: ")
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

        case "s":
            if numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.")
                continue

            valor = obter_valor("Informe o valor do saque: ")

            if valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > limite:
                print("Operação falhou! O valor do saque excede o limite.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

        case "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        case "q":
            print("Saindo do sistema. Até logo!")
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
