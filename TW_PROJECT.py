"""S.E. ELECTRONICS, SEM 4, MHSSCE"""
"""NAME : TAJ MOHAMMED SHAH -- 4119006
          HAMZA ANSARI -- 4119007
          ADVAIT GURUNATH CHAVAN -- 4119008
          AAKASH GUPTA -- 4119009"""
""""TOPIC: ELECTRO ATM SYSTEM"""""
import getpass

# creating a lists of users, their PINs and bank statements
users = ['taj', 'hamza', 'advait', 'aakash']
pins = ['9006', '9007', '9008', '9009']
amounts = [4119006, 4119007, 4119008, 4119009]
count = 0
# while loop checks existence of the entered username
print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome to ELECTRO ATM SYSTEM                          *")
print("*                                                                          *")
print("****************************************************************************")
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        elif user == users[2]:
            n = 2
        else:
            n = 3
        break
    else:
        print('----------------')
        print('****************')
        print('INVALID USERNAME')
        print('****************')
        print('----------------')

# comparing pin
while count <= 3:
    print('------------------')
    print('******************')
    pin = input('PLEASE ENTER PIN: ')
    print('******************')
    print('------------------')
    if pin.isdigit():
        if user == 'taj':
            if pin == pins[0]:
                break
            else:
                count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()

        if user == 'hamza':
            if pin == pins[1]:
                break
            else:
                count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()
        if user == 'advait':
            if pin == pins[2]:
                break
            else:
                count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()
        if user == 'aakash':
            if pin == pins[3]:
                break
            else:
                count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()

    else:
        print('------------------------')
        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        print('------------------------')
        count += 1
    # in case of a valid pin- continuing, or exiting
    if count == 3:
        print('-------------------------------------------------------')
        print('*******************************************************')
        print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
        print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
        print('!!!!!!!!!!!!!!!PLEASE CONTACT YOUR BRANCH!!!!!!!!!!!!!!')
        print('*******************************************************')
        print('-------------------------------------------------------')
        exit()

        print('-------------------------')
        print('*************************')
        print('LOGIN SUCCESFUL, CONTINUE')
        print('*************************')
        print('-------------------------')
        print()
        print('--------------------------')
        print('**************************')
        print(str.capitalize(users[n]), 'welcome to ELECTRO ATM SYSTEM')
        print('**************************')
        print('----------ELECTRO ATM SYSTEM-----------')
# Main menu
while True:
    # os.system('clear')
    print('-------------------------------')
    print('*******************************')
    response = input(
        'SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nCash Withdraw___(W) \nCash Deposit___(C)  \nChange PIN_(P)  '
        '\nQuit_______(Q) \nType The Letter Of Your Choices: ').lower()
    print('*******************************')
    print('-------------------------------')
    valid_responses = ['s', 'w', 'c', 'p', 'q']
    response = response.lower()
    if response == 's':
        print('---------------------------------------------')
        print('*********************************************')
        print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n], 'RUPEES IN YOUR ACCOUNT.')
        print('*********************************************')
        print('---------------------------------------------')
    elif response == 'w':
        print('---------------------------------------------')
        print('*********************************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('*********************************************')
        print('---------------------------------------------')
        if cash_out % 500 != 0 and cash_out % 2000 != 0:
            print('------------------------------------------------------')
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 500 AND 2000 RUPEES NOTES')
            print('******************************************************')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
            print('-----------------------------')
        else:
            amounts[n] = amounts[n] - cash_out
            print('-----------------------------------')
            print('***********************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('***********************************')
            print('-----------------------------------')
    elif response == 'c':
        print()
        print('---------------------------------------------')
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
        print('*********************************************')
        print('---------------------------------------------')
        print()
        if cash_in % 500 != 0 and cash_in % 2000 != 0:
            print('----------------------------------------------------')
            print('****************************************************')
            print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 500 AND 2000 RUPEES NOTES')
            print('****************************************************')
            print('----------------------------------------------------')
        else:
            amounts[n] = amounts[n] + cash_in
            print('----------------------------------------')
            print('****************************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('****************************************')
            print('----------------------------------------')
    elif response == 'p':
        print('-----------------------------')
        print('*****************************')
        new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
        print('*****************************')
        print('-----------------------------')
        if new_pin.isdigit() and new_pin != pins & [n] and len(new_pin) == 4:
            print('------------------')
            print('******************')
            new_card_pin = str(getpass.getpass('CONFIRM NEW PIN: '))
            print('*******************')
            print('-------------------')
            if new_card_pin != new_pin:
                print('------------')
                print('************')
                print('PIN MISMATCH')
                print('************')
                print('------------')
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
            print('-------------------------------------')
            print('*************************************')
            print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('*************************************')
            print('-------------------------------------')
    elif response == 'q':
        exit()
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')
