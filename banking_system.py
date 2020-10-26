#!/usr/bin/env python3

banks = []
for i in range(3):
    bank = []
    for j in range(10):
        bank.append([j, 0, []])
    banks.append(bank)


def converter(value):
    """
    convert string into intger value
    it's take one argument
    """

    try:
        int(value)
        return int(value)
    except:
        return False


def action_deposit(bank_name, user_account):
    """ this is preaction required for deposit"""

    print("Welcome to deposit")

    value_str = input("Please Enter the value to be deposited -->")
    amount = converter(value_str)

    if isinstance(amount, int) and amount > 0:
        flag = deposit(bank_name, user_account, amount)

        if flag == 1:
            print("____status____")
            print("success")
        else:
            print("____status_____")
            print("failed")
    else:
        print("Enter the correct amount")


def deposit(bank_name, account_name, amount):
    """this function deposing money in bank
    it's take three arugment """

    bank = banks[bank_name]
    acc = bank[account_name]
    acc[1] = acc[1] + amount

    if len(acc[2]) >= 10:
        acc[2].pop(0)
    acc[2].append(amount)

    return 1


def action_withdraw(bank_name, user_account):
    """preaction required for withdraw"""

    print("Welcome to withdraw")

    value_str = input("Please Enter the value to be withdrawn-->")
    amount = converter(value_str)

    if isinstance(amount, int) and  amount > 0:
        flag = withdraw(bank_name, user_account, amount)
        if flag == 1:
            print("____status____")
            print("success")
        else:
            print("____status_____")
            print("failed")
    else:
        print("Enter the correct amount")


def withdraw(bank_name, account_name, amount):
    """this function remove money from bank"""

    bank = banks[bank_name]
    acc = bank[account_name]

    if acc[1] >= amount:
        acc[1] = acc[1] - amount

        if len(acc[2]) >= 10:
            acc[2].pop(0)
        acc[2].append(-amount)
        return 1
    else:
        print("insufficent fund")
        return False


def action_transfer(bank_name, user_account):
    """This is pre action required for transfering"""

    print("Welcome to transfer")
    print("Enter Reciver bank name")
    print("press 'i' for ICIC")
    print("press 'h' for HDFC")
    print("press 'p' for PNB")
    reciver_bank = input("Enter -->")

    if reciver_bank == 'i':
        reciver_bank_name = 0
        trans(bank_name, user_account, reciver_bank_name)
    elif reciver_bank == 'h':
        reciver_bank = 1
        trans(bank_name, user_account, reciver_bank)
    elif reciver_bank == 'p':
        reciver_bank = 2
        trans(bank_name, user_account, reciver_bank)
    else:
        print("Enter correct bank name")


def trans(sendr_bank_name, sender_account_name, reciver_bank_name):
    """
    this is for transfer money one bank account to another
    """

    reci_str = input("Enter the receiver account number 0 to 9-->")
    reci_acc = converter(reci_str)

    if isinstance(reci_acc, int) and 0 <= reci_acc < 10:
        value_str = input("Enter the amount you want to transfer-->")
        amount = converter(value_str)

        if isinstance(amount, int):
            status = withdraw(sendr_bank_name, sender_account_name, amount)

            if status == 1:
                deposit(reciver_bank_name, reci_acc, amount)
                
                print("______status______")
                print("sucess")
            else:
                print("______status______")
                print("failed")
        else:
            print("Enter the valid amount")
    else:
        print("Enter valid account number")



def acc_info(bank_name, user_account):
    """ it provide account info"""

    bank = banks[bank_name]
    acc = bank[user_account]
    lenth = len(acc[2])

    print("welcome to Account Info")
    print("_______Account Info______")
    print("Your Balance is -->", acc[1])

    if lenth > 0:
        lenth = lenth - 1
        print("Your Last Trascation is --->", acc[2][lenth])


def statments(bank_name, user_account):
    """ it provide last 10 statemnts"""

    bank = banks[bank_name]
    acc = bank[user_account]
    lenth = len(acc[2])

    print(lenth)
    print("________statements_______")
    print("Balance = ", acc[1])

    if lenth > 0:

        for statment in range(lenth):
            print("Trascation {} --> |{}|".format(statment + 1, acc[2][statment]))
    else:
        print("You dont have any trascation")



def login_page():
    """it donesn't take any argument"""

    print("_______Login Page_______")
    print("Press 'i' for ICIC bank")
    print("Press 'h' for HDFC bank")
    print("Press 'p' for PNB bank")
    print("press 'q' for quite")


def main_manu():
    """it donesn't take any arugment"""

    print("________Main Manu_________")
    print("Press 'd' for Deposint")
    print("Press 'w' for Withdraw")
    print("Press 't' for Transfer")
    print("Press 'a' for Account Info")
    print("Press 's' for Satements")
    print("press 'q' for quite")




def manu_respone(bank_name, user_account):
    """ for getting response of manu
        it take no arument"""

    main_manu()
    manu_action = input("Enter -->")

    while manu_action != 'q':
        
        if manu_action == 'd':  # this response for deposit
            action_deposit(bank_name, user_account)
        elif manu_action == 'w':    #this response for withdreaw
            action_withdraw(bank_name, user_account)
        elif manu_action == 't':    #this response for transefer
            action_transfer(bank_name, user_account)
        elif manu_action == 'a':        #this response for Account info
            acc_info(bank_name, user_account)
        elif manu_action == 's':
            statments(bank_name, user_account) # this response for statements
        else:
            print("Enter correct input")

        main_manu()
        manu_action = input("Enter -->")
login_page()
login_action = input("Enter -->")
while login_action != 'q':

    if login_action == 'i':
        print("welcome to icic")

        bank_name = 0
        user_acc_str = input("Enter your account no in 0 to 9 -->")
        user_account = converter(user_acc_str)

        if isinstance(user_account, int) and (10 > user_account >= 0):
            manu_respone(bank_name, user_account)
        else:
            print("Error  Enter Correct Account NO !!!")
    elif login_action == 'h':
        print("welcome to hdfc")

        bank_name = 1
        user_acc_str = input("Enter your account no in 0 to 9 -->")
        user_account = converter(user_acc_str)

        if isinstance(user_account, int) and (10 > user_account >= 0):
            manu_respone(bank_name, user_account)
        else:
            print("Error !!! Enter Correct Account NO !!!")
    elif login_action == 'p':
        print("welcome to pnb")

        bank_name = 2
        user_acc_str = input("Enter your account no in 0 to 9 -->")
        user_account = converter(user_acc_str)

        if isinstance(user_account, int) and  (10 > user_account >= 0):
            manu_respone(bank_name, user_account)
        else:
            print("Error !!! Enter Correct Account NO !!!")
    login_page()
    login_action = input("Enter -->")
