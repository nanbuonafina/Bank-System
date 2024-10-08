import datetime
from time import strftime

# a classe utilidades contém o metodo get_log que registra todos as movimentações das contas
class Utilities:
    def get_log(self):
        # Obtém a data e hora atuais
        d = datetime.datetime.now()
        # Formata a data e hora
        formated_datetime = strftime("%y/%m/%d %H:%M")
        return formated_datetime

class Conta:
    # construtor
    def __init__(self):
        # objeto = atributo
        self._balance = 0 # protected
        self.statement = []
        self.utilities = Utilities()

    # metodo deposit
    def deposit(self, value):
        deposit_value = value
        confirm_deposit = input(f"Are you sure that you want to deposit R${deposit_value}? (Y) Yes / Any other caracter to deny: ")

        if confirm_deposit.lower() == 'y':
            self._balance += value
            print('Deposit done.')
            log = self.utilities.get_log()
            self.statement.append(f'Deposit: {deposit_value} at {log}')
        else:
            print("Operation denied.")

        return self._balance, self.statement

    # metodo withdraw
    def withdraw(self, value):
        withdraw_value = value
        confirm_withdraw = input(f'Are you sure that you wanto to take R${withdraw_value}? (Y) Yes / Any other caracter to deny: ')

        if confirm_withdraw.lower() == 'y' and withdraw_value < self._balance:
            self._balance -= withdraw_value
            print('Successfully done!')
            log = self.utilities.get_log()
            self.statement.append(f'Withdraw: {withdraw_value} at {log}')
        else:
            print('OPERATION DENIED')

        return self._balance, self.statement

    # metodo bank_statement
    def bank_statement(self):
        if not self.statement:
            print(f'Balance: R${self._balance}')
            print('No operations!')
        else:
            print(f'Your balance is: R${self._balance}\nStatement list:')
            for i, item in enumerate(self.statement, start=1):
                print(f'{i}. {item}')

        return self._balance, self.statement

