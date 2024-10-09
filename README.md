# Sistema Bancário - Documentação

## Descrição do Projeto
Este projeto implementa um sistema bancário utilizando os conceitos de **Programação Orientada a Objetos (POO)**. O sistema permite que os usuários criem contas bancárias, realizem depósitos, saques, alternem entre contas e obtenham o histórico de transações com registro de data e hora. O projeto é composto por classes que encapsulam o comportamento e os atributos das contas bancárias e o gerenciamento das operações.

---

## Funcionalidades Principais

### 1. Criar Conta Bancária
- Os usuários podem criar novas contas bancárias.
- Cada conta é identificada por um número único ou identificação.
- As contas são armazenadas e podem ser acessadas para realizar operações.

### 2. Depósito
- O sistema permite que os usuários façam depósitos em suas contas.
- O valor depositado é adicionado ao saldo da conta.
- Cada transação de depósito é registrada no histórico da conta, com a data e hora exatas da operação.

### 3. Saque
- Os usuários podem realizar saques de suas contas, desde que o saldo seja suficiente.
- O valor sacado é subtraído do saldo da conta.
- Assim como os depósitos, os saques são registrados com data e hora no histórico da conta.

### 4. Trocar de Conta
- O usuário pode alternar entre diferentes contas bancárias, desde que a conta exista.
- Ao trocar de conta, as operações subsequentes (depósitos, saques) serão aplicadas à conta ativa.

### 5. Histórico de Transações
- O sistema mantém um registro detalhado de todas as transações (depósitos e saques) realizadas em cada conta.
- O histórico inclui a data, hora, tipo de operação (depósito ou saque) e o valor.

---

## Estrutura das Classes

### 1. Classe `Conta`
A classe `Conta` representa uma conta bancária individual. Ela armazena informações como o número da conta, o saldo atual e o histórico de transações.

**Atributos**:
- `id_conta`: Identificador único da conta.
- `saldo`: O saldo atual da conta.
- `historico`: Um log de todas as transações realizadas na conta (depósitos e saques).

**Métodos**:
- `depositar(valor)`: Realiza um depósito na conta e registra a transação no histórico.
- `sacar(valor)`: Realiza um saque da conta, desde que haja saldo suficiente, e registra a transação no histórico.
- `obter_historico()`: Retorna o histórico de todas as transações realizadas na conta.
- `__str__()`: Exibe um resumo das informações da conta (ID e saldo).

### 2. Classe `SistemaBancario`
A classe `SistemaBancario` gerencia as contas bancárias e as operações relacionadas, como criar uma nova conta, alternar entre contas e realizar operações.

**Atributos**:
- `contas`: Um dicionário que armazena as contas bancárias, onde a chave é o `id_conta` e o valor é o objeto `Conta`.
- `conta_atual`: A conta que está atualmente selecionada para realizar operações.

**Métodos**:
- `criar_conta(id_conta)`: Cria uma nova conta com o `id_conta` especificado.
- `trocar_conta(id_conta)`: Alterna para uma conta diferente, identificada pelo `id_conta`.
- `depositar(valor)`: Realiza um depósito na conta atualmente ativa.
- `sacar(valor)`: Realiza um saque da conta atualmente ativa.
- `obter_historico_conta()`: Retorna o histórico de transações da conta atualmente ativa.
- `__str__()`: Exibe um resumo das contas no sistema.

---

## Exemplo de Uso

Aqui está um exemplo de como usar o sistema bancário:

```python
# Criando o sistema bancário
sistema = SistemaBancario()

# Criando duas contas
sistema.criar_conta(1)
sistema.criar_conta(2)

# Trocando para a conta 1 e realizando operações
sistema.trocar_conta(1)
sistema.depositar(1000)
sistema.sacar(200)

# Trocando para a conta 2 e realizando operações
sistema.trocar_conta(2)
sistema.depositar(500)
sistema.sacar(100)

# Obtendo histórico de transações da conta 1
sistema.trocar_conta(1)
print(sistema.obter_historico_conta())

# Obtendo histórico de transações da conta 2
sistema.trocar_conta(2)
print(sistema.obter_historico_conta())
