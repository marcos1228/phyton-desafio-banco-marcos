# Lista de usuários e contas
usuarios = []
contas = []

# Funções para operações bancárias
def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato, numero_saques

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato, numero_saques

def extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Funções para gerenciamento de usuários e contas
def criar_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Operação falhou! Usuário com este CPF já existe.")
    else:
        usuarios.append({
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco
        })

def criar_conta_corrente(cpf):
    global contas
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    if usuario is None:
        print("Operação falhou! Usuário não encontrado.")
    else:
        contas.append({
            'agencia': '0001',
            'numero': len(contas) + 1,
            'usuario': usuario
        })

# Menu de opções
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[u] Criar usuário
[c] Criar conta corrente

=> """

# Inicialização de variáveis
saldo = 100.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do programa
while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        if saldo >= valor:
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "e":
        extrato(saldo, extrato=extrato)

    elif opcao == "u":
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento do usuário (dd/mm/aaaa): ")
        cpf = input("Informe o CPF do usuário (somente números): ")
        endereco = input("Informe o endereço do usuário (logradouro, nro - bairro - cidade/sigla estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário para criar a conta corrente (somente números): ")
        criar_conta_corrente(cpf)

    elif opcao == "q":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")