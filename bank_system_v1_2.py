# SISTEMA BANCÁRIO > DEPÓSITOS, SAQUES E EXTRATO

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print('Por favor, insira valores acima de R$0.00')
        except ValueError:
            print('Por favor, insira um númeor válido.')

def deposit(balance, statement):
    print('DEPOSIT OPERATION')
    deposit_value = get_positive_float('Value of Deposit: R$')

    confirm_deposit = input(f"Are you sure that you wanto to deposit R${deposit_value}? (Y) Yes / Any other caracter to deny: ")

    if confirm_deposit.lower() == 'y':
        balance += deposit_value
        print('Deposit done.')
        statement.append(f'Deposit: {deposit_value}')
    else:
        print("Operation denied.")   

    return balance, statement

def withdraw(balance, statement):
    print("WITHDRAW OPERATION")
    
    withdraw_value = get_positive_float('Value of withdraw: R$')
    confirm_withdraw = input(f'Are you sure that you wanto to take R${withdraw_value}? (Y) Yes / Any other caracter to deny: ')

    if confirm_withdraw.lower() == 'y' and withdraw_value < balance:
        balance -= withdraw_value
        print('Successfully done!')

        statement.append(f'Withdraw: {withdraw_value}')
    else:
        print('OPERATION DENIED')

    return balance, statement

def bank_statement(balance, statement):
    if not statement:
        print('No operations')
    else:
        print(f'Your balance is: R${balance}\nStatement list:')
        for i, item in enumerate(statement, start=1):
            print(f'{i}. {item}')

    return balance, statement

def close_system():
    close_confirmation = input('Are you sure that you want to close the system? (Y) Yes / Any other caracter to cancel: ')
    return close_confirmation.lower() == 'y'

def main():
    name = input('Type your name: ')
    balance = 0.0
    statement = []
    counter = 0
    max_transations_operations = 10

    print(f'Hi, {name}! Welcome to your bank system!')
    print()

    while True:
        choice = input('''M E N U
        (1) Deposit
        (2) Withdraw
        (3) Bank Statement
        (4) Exit
               
        Type your choice: ''')

        if choice == '1':
            if counter < max_transations_operations:
                balance, statement = deposit(balance, statement)
                counter +=1
            else:
                print("Transaction limit exceeded.")
        elif choice == '2':
            if counter < max_transations_operations:
                balance, statement = withdraw(balance, statement)
                counter +=1
            else:
                print("Transaction limit exceeded.")
        elif choice == '3':
            balance, statement = bank_statement(balance, statement)
        elif choice == '4':
            if close_system():
                print("Exiting the system. See you later!")
                break
        else:
            print("Invalid choice. Please, try again using 1-4.")

if __name__ == "__main__":
    main()