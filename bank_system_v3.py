import datetime

class Utilities:
    def get_log(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Conta:
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self._saldo = 0
        self.extrato = []
        self.util = Utilities()

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            log = f"{self.util.get_log()} - Depósito de R${valor:.2f}"
            self.extrato.append(log)
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            log = f"{self.util.get_log()} - Saque de R${valor:.2f}"
            self.extrato.append(log)
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def mostrar_extrato(self):
        print(f"Extrato da conta {self.numero_conta}:")
        for log in self.extrato:
            print(log)
        print(f"Saldo atual: R${self._saldo:.2f}")

class SistemaBancario:
    def __init__(self):
        self.contas = {}

    def criar_conta(self):
        numero_conta = input("Digite o número da nova conta: ")
        if numero_conta not in self.contas:
            self.contas[numero_conta] = Conta(numero_conta)
            print(f"Conta {numero_conta} criada com sucesso.")
        else:
            print("Já existe uma conta com esse número.")

    def buscar_conta(self, numero_conta):
        return self.contas.get(numero_conta, None)

    def menu(self):
        while True:
            print("\n==== Menu Banco ====")
            print("1. Criar nova conta")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Mostrar extrato")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.criar_conta()
            elif opcao == "2":
                numero_conta = input("Digite o número da conta: ")
                conta = self.buscar_conta(numero_conta)
                if conta:
                    valor = float(input("Digite o valor para depósito: "))
                    conta.depositar(valor)
                else:
                    print("Conta não encontrada.")
            elif opcao == "3":
                numero_conta = input("Digite o número da conta: ")
                conta = self.buscar_conta(numero_conta)
                if conta:
                    valor = float(input("Digite o valor para saque: "))
                    conta.sacar(valor)
                else:
                    print("Conta não encontrada.")
            elif opcao == "4":
                numero_conta = input("Digite o número da conta: ")
                conta = self.buscar_conta(numero_conta)
                if conta:
                    conta.mostrar_extrato()
                else:
                    print("Conta não encontrada.")
            elif opcao == "5":
                print("Saindo do sistema bancário...")
                break
            else:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.menu()