# Sistema bancário em Python

## Visão geral

Este é um sistema bancário baseado em Python que permite aos usuários gerenciar várias contas. Ele foi projetado seguindo os princípios da Programação Orientada a Objetos (POO) e fornece recursos como depósitos, retiradas e registros de transações.

## Recursos

- Crie várias contas bancárias
- Execute depósitos e retiradas
- Rastreie todas as transações em um extrato de conta (extracto)
- Sistema de registro para registrar cada operação com um registro de data e hora

## Descrições de classe

### `Utilitários`

Esta classe fornece funções de utilitário para o sistema bancário.

#### Métodos:

- **`get_log()`**: Retorna a data e a hora atuais como uma string no formato `AAAA-MM-DD HH:MM:SS`. Usado para registrar transações.

---

### `Conta`

Representa uma conta bancária com operações básicas, como depósitos, retiradas e visualização do saldo da conta e histórico de transações.

#### Atributos:

- **`numero_conta`**: Número da conta (string ou inteiro).
- **`_saldo`**: Atributo privado que representa o saldo da conta.
- **`extrato`**: Uma lista de logs de transações.
- **`util`**: Uma instância da classe `Utilities` para gerar logs.

#### Métodos:

- **`__init__(self, numero_conta)`**: Inicializa uma nova conta com o número de conta fornecido, define o saldo inicial como zero e prepara uma lista vazia para logs de transações.

- **`depositar(self, valor)`**: Deposita o valor fornecido na conta. Se o depósito for bem-sucedido, a transação será registrada com o registro de data e hora.

- **`sacar(self, valor)`**: Retira o valor especificado da conta se o saldo for suficiente. Registra a transação com o registro de data e hora.

- **`mostrar_saldo(self)`**: Exibe o saldo atual da conta.

- **`ver_extrato(self)`**: Exibe o histórico completo de transações (extrato) da conta, mostrando todos os depósitos e retiradas com seus respectivos timestamps.

---

## Exemplo de uso

```python
# Criar uma conta
conta1 = Conta(numero_conta=12345)

# Depositar na conta
conta1.depositar(1000)

# Sacar da conta
conta1.sacar(200)

# Verificar saldo
conta1.mostrar_saldo()

# Ver histórico de transações
conta1.ver_extrato()
