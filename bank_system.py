# SISTEMA BANCÁRIO > DEPÓSITOS, SAQUES E EXTRATO

# USER
name = input('Type your name: ')
balance = 0.0
statement = []

print(f'Hi, {name}! Welcome to your bank system!')
print()

while(exit != 'Y'):
    choice = input('''M E N U
    (1) Deposit
    (2) Withdraw
    (3) Bank Statement
    (4) Balance
    (5) Exit
               
    Type your choice: ''')

    if choice == '1':
        print()
        print('DEPOSIT OPERATION!')
        print()

        deposit_value = input('Value of Deposit: R$')

        if float(deposit_value) > 0:
            confirm_deposit = input(f'Are you sure that you want to deposit R${deposit_value}? (Y) Yes / Any caracter to go back to menu: ')
            
            if (confirm_deposit == 'Y') or (confirm_deposit == 'y'):
                balance += float(deposit_value)
                print(f'Deposit done. Your balance now is it: R${deposit_value}.')
                print()
                statement.append(f'Deposit: {deposit_value}')
            else:
                print('Operation cancelled.')
                print()
        else:
            print('Denied. You have to deposit more than R$0.0')

    elif choice == '2':
        print()
        print('WITHDRAW OPEATION')
        print()

        counter = 0

        if counter < 3:
            withdraw_value = input('Value of Withdraw: R$')
            
            if (float(withdraw_value) > 0) and (float(withdraw_value) <= balance):
                print()
                confirm_withdraw = input(f'Are you sure that you want to take R${withdraw_value}? (Y) Yes / Any caracter to deny: ')
                
                if (confirm_withdraw == 'Y') or (confirm_withdraw == 'y'):
                    balance -= float(withdraw_value)
                    print(f'Successfully done! Your balance now is it R${balance}')

                    statement.append(f'Withdraw: R${withdraw_value}')
                    counter+=1
                else:
                    print('Withdraw operation denied.')
            else:
                print()
                if float(withdraw_value) <= 0:
                    print('Only values above R$0.0')
                else:
                    print('Balance insufficient.')
        else:
            print('Withdrawal limit exceeded')

    elif choice == '3':
        print()
        print('BANK STATEMENT OPERATION')
        print()
        if not statement:
            print('Nothing to show')
        else:
            print(f'Your Statement: \n{statement}\nYour balance: R${balance}')
        

    elif choice == '4':
        print()
        print(f'Your balance is: R${balance}.')
        print()

    elif choice == '5':
        print()
        exit = input('Do you want to exit? (Y) Yes / (N) No: ')
        print()

    else:
        print()
        print('Invalid Option')
        print()
        