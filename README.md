# Sistema Bancário Simples

Este projeto é um sistema bancário simples em Python que permite realizar operações básicas como depósitos, saques e visualização de extratos. Ele foi desenvolvido para funcionar com um único usuário e inclui verificações para garantir a integridade das transações.

## Funcionalidades

1. **Depósito**:
   - Permite o depósito de valores positivos.
   - O valor depositado é adicionado ao saldo da conta e registrado no extrato.

2. **Saque**:
   - Permite realizar até 3 saques diários.
   - Cada saque tem um limite máximo de R$ 500,00.
   - O sistema verifica se há saldo suficiente antes de permitir o saque.
   - Saques realizados são registrados no extrato.

3. **Extrato**:
   - Exibe todos os depósitos e saques realizados.
   - Mostra o saldo atual da conta.
   - Se não houver movimentações, informa que não foram realizadas transações.

4. **Sair**:
   - Permite ao usuário encerrar o programa.

## Como Usar

1. **Inicialização**:
   - O saldo inicial é definido como R$ 100,00.

2. **Operações**:
   - O usuário pode escolher a operação desejada através de um menu de opções:
     - `[d]` para depositar
     - `[s]` para sacar
     - `[e]` para exibir o extrato
     - `[q]` para sair

## Exemplo de Uso

Após iniciar o programa, o usuário verá um menu com as opções disponíveis. Dependendo da escolha, o usuário pode depositar dinheiro, sacar (com as verificações adequadas) ou visualizar o extrato da conta. O programa continua em loop até que o usuário escolha a opção de sair (`[q]`).

## Validações

- Depósitos e saques aceitam apenas valores positivos.
- O sistema limita o número de saques diários a 3 e impõe um valor máximo de R$ 500,00 por saque.
- Verifica se há saldo suficiente para realizar um saque.

## Código Principal

O código principal inclui um loop que exibe o menu de operações e processa as entradas do usuário utilizando a estrutura `match-case` para tratar cada operação. A função `obter_valor` garante que os valores de entrada sejam válidos.
