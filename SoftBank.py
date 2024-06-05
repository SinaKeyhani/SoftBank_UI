import random as rd 

import math 


user_accounts = {'sina.keyhani@gmail.com' : {'pin': '1234', 'balance': 10000.00, 'credit_score': rd.randint(300,999)},
                 'negin.morti@gmail.com' : {'pin': '2357', 'balance': 100000.00, 'credit_score': rd.randint(300,999)},
                 'navid.boghche@yahoo.co.uk' : {'pin': '8473', 'balance': 1500000.00, 'credit_score': rd.randint(300,999)},
                 'sara.taylor51@outlook.com' : {'pin': '5212', 'balance': 750000.00, 'credit_score': rd.randint(300,999)},
                 'farhad.jahan@gmail.com' : {'pin': '5774', 'balance': 850000.00, 'credit_score': rd.randint(300,999)},
                 'shayan.salehi@gmail.com' : {'pin': '8646', 'balance': 6420000.00, 'credit_score': rd.randint(300,999)},
                 'carlos.garcia04@hotmail.com' : {'pin': '6934', 'balance': 9530000.00, 'credit_score': rd.randint(300,999)},
                 'mina.kumar03@outlook.com' : {'pin': '1453', 'balance': 1000000.00, 'credit_score': rd.randint(300,999)},
                 'ananya.chen05@example.com' : {'pin': '9654', 'balance': 6520000.00, 'credit_score': rd.randint(300,999)},
                 'fatima.smith20@example.com' : {'pin': '8643', 'balance': 233000.00, 'credit_score': rd.randint(300,999)},
                 'jin.kumar19@hotmail.com' : {'pin': '1245', 'balance': 122300.00, 'credit_score': rd.randint(300,999)},
                 'youssef.omar16@gmail.com' : {'pin': '1215', 'balance': 463340.00, 'credit_score': rd.randint(300,999)},
                 'mateo.smith08@outlook.com' : {'pin': '1369', 'balance': 84353450.00, 'credit_score': rd.randint(300,999)},
                 'hana.ivanova07@yahoo.com' : {'pin': '1385', 'balance': 342342.00, 'credit_score': rd.randint(300,999)},
                 'aiko.nguyen01@gmail.com' : {'pin': '3323', 'balance': 575644.00, 'credit_score': rd.randint(300,999)},
                 'paul.moore74@outlook.com' : {'pin': '6646', 'balance': 643523.00, 'credit_score': rd.randint(300,999)},
                 'jane.brown20@hotmail.com' : {'pin': '9974', 'balance': 484534.00, 'credit_score': rd.randint(300,999)},
                 'eva.doe74@outlook.com' : {'pin': '8534', 'balance': 234324.00, 'credit_score': rd.randint(300,999)},
                 'sam.anderson80@yahoo.com' : {'pin': '9764', 'balance': 937327.00, 'credit_score': rd.randint(300,999)},
                 'paul.anderson80@yahoo.com' : {'pin': '8274', 'balance': 459435.00, 'credit_score': rd.randint(300,999)},
                 'sara.smith60@gmail.com' : {'pin': '9802', 'balance': 3424234.00, 'credit_score': rd.randint(300,999)},
                 'jane.miller47@yahoo.com' : {'pin': '9812', 'balance': 948473.00, 'credit_score': rd.randint(300,999)},
                 'mark.anderson79@gmail.com' : {'pin': '2658', 'balance': 2139684.00, 'credit_score': rd.randint(300,999)},
                 'lisa.miller28@outlook.com' : {'pin': '9753', 'balance': 347397.00, 'credit_score': rd.randint(300,999)},
                 'paul.anderson59@hotmail.com' : {'pin': '1694', 'balance': 3594583.00, 'credit_score': rd.randint(300,999)},
                 'nina.smith10@outlook.com' : {'pin': '1968', 'balance': 3498504.00, 'credit_score': rd.randint(300,999)},
                 }


# lambda function to split email and capitalize the username
split_email = lambda email : email.split("@")[0].capitalize()

# lambda function for invalid choice message 
invalid_choice_message = lambda : print('Invalid choice! Please select a number from 1 to 7 ')


def login():

    """
    Prompt the user to enter their email and PIN to log in.
    Returns the email and PIN if the login is successful.
    """

    print(f''' 
            --------------------------------
            
            Welcome to SoftBank Banking App!

            Please enter your details below. 
          
            ----------------------------------
''')

    while True:

        email = input('\nPlease enter your email address : ').strip()
        pin = input('\nPlease enter your 4-digit PIN number :').strip()

        if login_check(email,pin):

            return email, pin
        

def login_check(email,pin):

    """
    Check the user credentials for login.
    Args:
        email (str): User email address.
        pin (str): User PIN.
    Returns:
        bool: True if the credentials are valid, False otherwise.
    """


    if email not in user_accounts.keys():
        print('email account not valid! Please try again.')
        return False
    
    elif pin != user_accounts[email]['pin']:
        print("Incorrect PIN! Please try again.")
        return False 
    
    else: 
        username = split_email(email)
        print(f'Login successful! Welcome back {username}.')
        return True


        
def logout(email):

    """
    Prompt the user to confirm logout.
    Args:
        email (str): User email address.
    """

    while True:

        selection = input('\nAre you sure you want to logout? ("yes" or "no") : ').lower().strip()

        if selection == 'yes':
            print(f'logging out. Goodbye, {split_email(email)}!')
            start_banking()

        elif selection == 'no':
            print('logout cancelled.')
            break

        else: 
            print('Invalid input! Please type "yes" or "no". ')
            continue

def check_balance(email):

    """
    Display the user's account balance.
    Args:
        email (str): User email address.
    """

    print(f'Your account balance is : £{round(user_accounts[email]["balance"],2): ,}')


def check_credit_score(email):

    """
    Display the user's credit score with a description.
    Args:
        email (str): User email address.
    """

    user_score = user_accounts[email]['credit_score']

    if 800<= user_score <= 999:
        print(f'Hi {split_email(email)}! Your credit score is {user_score} which is Execellent.')

    elif 740 <= user_score <= 799:
        print(f'Hi {split_email(email)}! Your credit score is {user_score} which is Very Good.')

    elif 670 <= user_score <=739:
        print(f'Hi {split_email(email)}! Your credit score is {user_score} which is Good.')
    
    elif 580 <= user_score <=669:
        print(f'Hi {split_email(email)}! Your credit score is {user_score} which is Fair.')

    elif 300 <= user_score <=579:
        print(f'Hi {split_email(email)}! Your credit score is {user_score} which is Poor.')



def transfer_check(email):

    """
    Prompt the user to enter the recipient email and transfer amount.
    Args:
        email (str): Sender's email address.
    Returns:
        tuple: Recipient email and transfer amount.
    """

    while True: 

        transfer_email = input('\nPlease enter email you wish to make a bank transfer : ').lower().strip()

        if transfer_email in user_accounts.keys() and transfer_email != email:

            break

        else:
            print('Invalid email to transfer! Please try again.')
            continue

    while True:

        try:

            amount = math.floor(float(input('\nPlease enter the amount you wish to transfer : £ '))*100)/100

            if is_positive(amount):
                break

            continue

        except ValueError as e:
            print(f'ValueError : {e}! Please enter a numerical value.')
            continue

    return transfer_email, amount


def balance_transfer(email, transfer_email, amount, pin):

    """
    Transfer balance from the user's account to another account.
    Args:
        email (str): Sender's email address.
        transfer_email (str): Recipient's email address.
        amount (float): Amount to transfer.
        pin (str): Sender's PIN.
    """
    
    attempts = 3

    if amount <= user_accounts[email]['balance']:
        
        while True:
            
            confirm_pin = input('\nPlease enter your 4-digit PIN number to confirm balance transfer: ').strip()

            if confirm_pin == pin:
                
                user_accounts[transfer_email]['balance'] += amount
                user_accounts[email]['balance'] -=amount 

                print(f'You have successfully transferred £{amount: ,} to {split_email(transfer_email)}') 
                break
            
            else:
                if attempts == 0:
                    print(f'Sorry {split_email(email)}, you have entered your PIN number incorrectly.')
                    start_banking()

                else: 
                    print(f'Invalid PIN number! Please try again, you have {attempts} attempts left.')
                    attempts -= 1

    else:
        print('Insufficient funds! Please make a deposite.')


def complete_balance_transfer(email,pin):
    
    transfer_email, amount = transfer_check(email)
    balance_transfer(email, transfer_email, amount, pin)


def is_positive(amount):
    
    if amount >0 :
        return True
    
    else: 
        print('Please enter a positive amount.')
        return False
    

def deposite(email):

    while True:

        try:
            amount = math.floor(float(input('\nPlease enter amount you wish to deposite: £ ')) * 100)/100

            if is_positive(amount):
                break

            continue

        except ValueError as e:
            print(f"ValueError : {e}! Please enter a numerical value.")
            continue

    user_accounts[email]['balance'] += amount 
    username = split_email(email)
    print(f'Hey {username}! Thank you for depositing £{amount: ,} into your account.')


def withdraw(email,pin):

    attempts = 3
    username = split_email(email)

    while True:

        try:
            amount = int(float(input('\nPlease enter the amount you wish to withdraw : £ ')))

            if is_positive(amount):
                if amount > user_accounts[email]['balance']:

                    print('Insufficient funds! Please make a deposite.')
                    break
                
                else:
                    while True:
                        confirm_pin = input('\nPlease enter your 4-digit PIN number to confirm withdraw: ')

                        if confirm_pin == pin:

                            user_accounts[email]['balance'] -= amount
                            print(f'You have successfully withdrawn £{amount: ,}.')
                            break
                        
                        else:
                            if attempts == 0:
                                print(f'Sorry {username}, you have entered your PIN number incorrect.')

                            else: 
                                print(f'Invalid PIN number! Please try again, you have {attempts} attempts left.')
                                attempts -=1

                    break

        except ValueError as e: 
            print(f'ValueError : {e}! Please enter a numerical value.')
            continue


def exit_application():
    print('Exiting the application. Thank you for using SoftBank!\n')
    exit()


def start_banking():

    email, pin = None, None

    while True:

        if email is None or pin is None:

            email, pin = login()

            print(f''' 
                ---------------------------------
                
                Please select an opntion
                [1]. Check Balance
                [2]. Balance Transfer
                [3]. Deposite Money 
                [4]. Withdraw Money 
                [5]. Check Credit Score 
                [6]. Log_out
                [7]. Exit
                
                ---------------------------------

    ''')


        choice = input('\nPlease select an option (1 - 7): ').strip()

        if choice == "1":
            check_balance(email)

        elif choice == '2':
            complete_balance_transfer(email,pin)
        
        elif choice == '3':
            deposite(email)

        elif choice == '4':
            withdraw(email, pin)

        elif choice == '5':
            check_credit_score(email)

        elif choice == '6':
            logout(email)

        elif choice == '7':
            exit_application()

        else:
            invalid_choice_message()



# Start the banking application
        
start_banking()



                        




                




