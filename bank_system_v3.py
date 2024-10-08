from Conta import Conta
import datetime
from time import strftime

# pega os logs do sistema geral: criação de conta, troca e falhas
def get_log():
    # Obtém a data e hora atuais
    d = datetime.datetime.now()
    # Formata a data e hora
    formated_datetime = strftime("%y/%m/%d %H:%M")
    return formated_datetime

# facilita a verificação o input do usuário
def get_positive_float(prompt):
    # Loop para garantir que o usuário insira um valor positivo
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print('Please, only type values above R$0.00')
        except ValueError:
            print('Please, type a number valid.')

contas = {} # armazena a relação: {id} : {Conta}
system_logs = [] # armazena os logs relacionados a criação das contas

# função para criar os objetos (contas) da classe Conta
def create_account():
    identifier = int(input('Type the id of your new account: '))
    contas[identifier] = Conta()
    print(f'Account {identifier} created')
    log = get_log()
    system_logs.append(f'Account {identifier} created at {log}')

# função para o usuário trocar de conta
def choose_account():
    identifier = int(input('Type the account id: '))
    if identifier in contas.keys():
        log_1 = get_log()
        system_logs.append(f'Account switched to {identifier} at {log_1}')
        return contas[identifier]
    else:
        print('Not Found')
        log_2 = get_log()
        system_logs.append(f'Account Identifier Not Found at {log_2}')
        return None


def main():
    while True:
        choice = int(input('''---===<<< MENU >>>===---
        (1) Create Account
        (2) Select Account
        (3) System Logs
        (4) Exit

        Type your choice: '''))

        if choice == 1:
            create_account()

        elif choice == 2:
            selected_account = choose_account()
            if selected_account:
                max_transations_operations = 3
                counter = 0
                while True:
                    operation = input('''---===<<< OPERATIONS >>>===---
                    (1) Deposit
                    (2) Withdraw
                    (3) Bank Statement
                    (4) Back

                    Type your choice: ''')

                    if operation == '1':
                        print('DEPOSIT OPERATION')
                        if counter < max_transations_operations:
                            value = get_positive_float('Value of Deposit: R$ ')
                            selected_account.deposit(value)
                            counter += 1
                        else:
                            print("Transaction limit exceeded.")

                    elif operation == '2':
                        print("WITHDRAW OPERATION")
                        if counter < max_transations_operations:
                            value = get_positive_float('Value of Withdraw: R$ ')
                            selected_account.withdraw(value)
                            counter += 1
                        else:
                            print("Transaction limit exceeded.")

                    elif operation == '3':
                        print('BANK STATEMENT')
                        selected_account.bank_statement()

                    elif operation == '4':
                            print("Back to Main Menu")
                            break
                    else:
                        print("Invalid choice. Please, try again using 1-4.")

        elif choice == 3:
            for i, item in enumerate(system_logs, start=1):
                print(f'{i}. {item}')

        elif choice == 4:
            print("Saindo...")
            break

        else:
            print("Invalid choice. Please, try again using 1-3.")

if __name__ == "__main__":
    main()
