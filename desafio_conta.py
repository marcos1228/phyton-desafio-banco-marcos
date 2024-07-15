import textwrap


def menu():
    menu_text = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_text))


def depositar(saldo, valor):
    if valor > 0:
        saldo += valor
        print(f'\n=== Depósito de R$ {valor:.2f} realizado com sucesso! ===')
        return saldo, f"Depósito:\tR$ {valor:.2f}\n"
    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
        return saldo, ""


def sacar(saldo, valor, limite, numero_saques, limite_saques):
    if valor <= 0:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
    elif valor > saldo:
        print('\n@@@ Operação falhou! Saldo insuficiente. @@@')
    elif valor > limite:
        print('\n@@@ Operação falhou! O valor do saque excede o limite. @@@')
    elif numero_saques >= limite_saques:
        print('\n@@@ Operação falhou! Número máximo de saques excedido. @@@')
    else:
        saldo -= valor
        numero_saques += 1
        print(f'\n=== Saque de R$ {valor:.2f} realizado com sucesso! ===')
        return saldo, f"Saque:\t\tR$ {valor:.2f}\n"

    return saldo, ""


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return None


def listar_contas(contas):
    if not contas:
        print("\n=== Nenhuma conta cadastrada. ===")
    else:
        for conta in contas:
            print("=" * 100)
            print(f"Agência:\t{conta['agencia']}")
            print(f"C/C:\t\t{conta['numero_conta']}")
            print(f"Titular:\t{conta['usuario']['nome']}")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo, valor, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
