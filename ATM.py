import time


name = input("Please what is your name? ")
password = input("Enter your Pin ")
if password.isdigit():
    password=int(password)
else:
    print("Invalid, Pin must be digits ")
    quit()
print("Hello"+" "+name+" "+"You are Welcome to The USA World Bank ATM Machime (UWB) ")
initial_amount = input("What is your current bank balance? ")
if initial_amount.isdigit():
    initial_amount = int(initial_amount)
else:
    print("Invalid input please enter a number next time...")
    for seconds in range(2,0,-1):
        print(seconds)
        time.sleep(1)
    print("Please take your card ")
    quit()
confirm_password=input("Please confirm your Pin ")
if confirm_password.isdigit():
    confirm_password=int(confirm_password)
else:
    print("Invalid, Pin must be digits")
while password!=confirm_password:
    confirm_password=input("Please confirm your password ")
    if confirm_password.isdigit():
        confirm_password=int(confirm_password)
    else:
        print("Invalid, Pin must be digits")
        continue
else:
    print("You are welcome sire/Ma")
card_type = input(""" Choose card to continue the process 

Enter type of Card
    1 for credit card
    2 for debit card
    3 for balance """)
if card_type =="1":
    credit_card = input("would you like to transfar? Enter 1 to continue 2 to quit ")
    if credit_card =="1":
        amount=input("""Enter amount for transaction
    1-> 5000    2-> 10000

    3-> 15000   4-> 20000

    5-> Other """)
        if amount =="1":
            amount1 = 5000
            print(f"You are about to transfar ${amount1} from you balance ")
            amount10 = input("Would you like to continue the process Enter 1 for yes 2 for no (1/2) ")
            if amount10 =="1":
                account_number = input("Enter the account number for the transaction ")
            elif amount10 =="2":
                print("Thank you for banking with us")
                for seconds in range (3,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                print("Invalid input")
                for seconds in range (2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            if account_number.isdigit():
                account_number = int(account_number)
            else:
                print("Invalid input pls enter Digits next time")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card ")
                quit()
            if amount1 > initial_amount:
                print("Sorry Insufficient balance")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                print(f"Transcation of ${amount1} to {account_number} was Successful")
                balance5 = input("Will you like to see your account balance?Enter 1 for yes 2 for no (1/2) ")
                if balance5 =="1":
                    balance5 = initial_amount-amount1
                    print(f"Your current balance is ${balance5}")
                    print("Thank you for banking with us")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                elif balance5 =="2":
                    print("Thank you for banking with us ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card ")
                    quit()
                else:
                    print("Invalid input ")
                    for seconds in range(2,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card ")
                    quit()
        elif amount =="2":
            amount2 = 10000
            print(f"You are about to transfar ${amount2} from your balance ")
            amount9 = input("Would you like to continue with the process Enter1 for yes 2 for no (1/2) ")
            if amount9 =="1":
                account_number2=input("Enter the account number for the transaction ")
            elif amount9 =="2":
                print("Thank you for banking with us")
                for seconds in range(3,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                print("Invalid input")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card ")
            if account_number2.isdigit:
                account_number2 = int(account_number2)
            else:
                print("Invalid input pls enter Digits next time")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card ")
                quit()
            if  amount2>initial_amount:
                print("Sorry Insufficient balance")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                print(f"Transcation of ${amount2} to {account_number2} was Successful")
                balance2=input("Will you like to see your current account balance? 1 for yes 2 for no (1/2) ")
                if balance2=="1":
                    balance2=initial_amount-amount2
                    print(f"Your current balance is ${balance2}")
                    print("Thank you for banking with us")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                elif balance2=="2":
                    print("Thank you for banking with us ")
                    for seconds in range(3,0,-2):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card ")
                    quit()
                else:
                    print("Invalid input ")
                    for seconds in range(2,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card ")
                    quit()
            
        elif amount=="3":
            amount3=15000
            print(f"You are about transfar ${amount3} from your balance")
            amount8=input("Would you like to continue with the process Enter 1 for yes 2 for no (1/2) ")
            if amount8=="1":
                account_number3=input("Enter the account number for the transaction ")
            elif amount8=="2":
                print("Thank you for banking with us")
                for seconds in range(3,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                print("Invalid input")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            if account_number3.isdigit():
                account_number3=int(account_number3)
            else:
                print("Invalid input please enter Digits next time")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            if amount3>initial_amount:
                print("sorry Insufficient balance")
                for seconds in range (2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                print(f"Transcation of ${amount3} to {account_number3} was Successful")
                balance3=input("Will you like to see you account balance? Enter 1 for yes 2 for no(1/2) ")
                if balance3=="1":
                    balance3=initial_amount-amount3
                    print(F"Your current balance is ${balance3}")
                    print("Thank you for banking with us")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print('Please take your card')
                    quit()
                elif balance3=="2":
                    print("Thank you for banking with us ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card ")
                    quit()
                else:
                    print("Invalid input")
                    for seconds in range (2,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card ")
                    quit()
        elif amount=="4":
            amount4=20000
            print(f"You are about to transfar ${amount4} from your balance")
            amount7=input("Would you like to continue the process enter 1 for yes 2 for no (1/2) ")
            if amount7=="1":
                account_number4=input("Enter the account number for the transaction ")
            elif amount7=="2":
                print("Thank you for banking with us")
                for seconds in range(3,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                print("Invalid input")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
            if account_number4.isdigit():
                account_number4=int(account_number4)
            else:
                print("Invalid input pls enter Digits next time")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card ")
                quit()
            if amount4>initial_amount:
                print("Sorry Insufficient balance")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card ")
                quit()
            else:
                print(f"Transaction of ${amount4} to {account_number4} was Successfully")
                balance2=input("Will you like to see your account balance? 1 for yes 2 for no (1/2) ")
                if balance2=="1":
                    balance2=initial_amount-amount4
                    print(f"Your account balance is ${balance2} ")
                    print("Thank you for banking with us")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Take your card")
                    quit()
                elif balance2=="2":
                    print("Thank you banking with us ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card ")
                    quit()
                else:
                    print("Invalid input")
                    for seconds in range(2,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card ")
                    quit()
        elif amount=="5":
            amount5=input("Enter the amount for Transaction ")
            if amount5.isdigit():
                amount5=int(amount5)
            else:
                print("Invalid input pls enter Digits next time")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            amount6=print(f"You are about to transfar ${amount5} from your balance")
            amount6=input("Will you like to continue the process 1 for yes 2 for no(1/2) ")
            if amount6=="1":
                account_number5=input("Enter the account number for the transaction ")
            elif amount6=="2":
                print("Thank you for banking with us ")
                for seconds in range(3,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
            else:
                print("Invalid input")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            if amount5>initial_amount:
                print("Sorry Insufficient balance")
                for seconds in range(2,0,1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                print(f'Transcation of ${amount5} to {account_number5} was Successfully')
                balance2=input("Will you like to see your account balance? 1 for yes 2 for no (1/2) ")
                if balance2=="1":
                    balance2=initial_amount-amount5
                    print(f"Your account balance is ${balance2} ")
                    print("Thank you for banking with us ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                elif balance2=="2":
                    print("Thank you for banking with us ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                else:
                    print("Invalid input")
                    for seconds in range(2,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
    else:
        print("Thank you for banking with us ")
        for seconds in range(3,0,-1):
            print(seconds)
            time.sleep(1)
        time_watch=time.localtime()
        local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
        print(local_time)
        print("Please take your card")
        quit()
elif card_type=="2":
    debit_card=input("Would you like to withdraw? Enter 1 to withdraw and 2 to cancel the process(1/2) ")
    if debit_card=="1":
        withdraw=input("""You are about to withdraw, Enter for withdrawal
    1-> 5000    2-> 10000
        
    3-> 15000   4-> 20000

    5-> Other """)
        if withdraw=="1":
            cash=5000
            if cash>initial_amount:
                print("Sorry Insufficient balance")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card ")
                quit()
            else:
                for seconds in range(3,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print(f"Pls take you cash..")
                balance=input('Will you like to see your account balance? 1 for yes 2 for no(1/2) ')
                if balance=="1":
                    balance=initial_amount-cash
                    print(f"Your balance is ${balance}")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                elif balance=="2":
                    print("Thank you for banking with us ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit
                else:
                    print("Invalid input ")
                    for seconds in range(2,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
        elif withdraw=="2":
            cash2=10000
            if cash2>initial_amount:
                print("Sorry Insufficient balance")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                for seconds in range(3,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Pls take your cash")
                balance=input("Will you like to see you account balance 1 for yes 2 for no (1/2) ")
                if balance=="1":
                    balance2=initial_amount-cash2
                    print(f"Your current balance is ${balance2} ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                elif balance=="2":
                    print("Thank you for banking with us ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                else:
                    print("Invalid input")
                    for seconds in range(2,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
        elif withdraw=="3":
            cash3=15000
            if cash3>initial_amount:
                print("Sorry Insufficient balance")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                for seconds in range(3,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your cash")
                balance=input("Will you like to see your account balance 1 for yes 2 for no (1/2) ")
                if balance=="1":
                    balance3=initial_amount-cash3
                    print(f"Your account balance is ${balance3}")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                elif balance=="2":
                    print("Thank you for banking with us ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                else:
                    print("Invalid input ")
                    for seconds in range (2,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
        elif withdraw=="4":
            cash4=20000
            if cash4>initial_amount:
                print("Sorry Insufficient balance")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your cash")
                balance=input("Will you like to see your account balance 1 for yes 2 for no(1/2) ")
                if balance=="1":
                    balance4=initial_amount-cash4
                    print(f"Your account balance is ${balance4}")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                elif balance=="2":
                    print("Thank you for banking with us ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                else:
                    print("Invalid input...")
                    for seconds in range(2,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
        elif withdraw=="5":
            cash5=input("Enter amount for withdrawal ")
            if cash5.isdigit():
                cash5=int(cash5)
            else:
                print("Invalid pls input a number next time")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            if cash5>initial_amount:
                print("Sorry Insufficient balance")
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take your card")
                quit()
            else:
                for seconds in range(2,0,-1):
                    print(seconds)
                    time.sleep(1)
                time_watch=time.localtime()
                local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                print(local_time)
                print("Please take you cash ")
                balance=input("Would you like see your account balance yes for 1 no for 2 (1/2) ")
                if balance=="1":
                    balance5=initial_amount-cash5
                    print(f"Your available balance is ${balance5}")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                elif balance=="2":
                    print("Thank you for banking with us ")
                    for seconds in range(3,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
                else:
                    print("Invalid input")
                    for seconds in range(2,0,-1):
                        print(seconds)
                        time.sleep(1)
                    time_watch=time.localtime()
                    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
                    print(local_time)
                    print("Please take your card")
                    quit()
    else:
        print("Thank you for banking with us")
        for seconds in range(3,0,-1):
            print(seconds)
            time.sleep(1)
        time_watch=time.localtime()
        local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
        print(local_time)
        print("Please take your card")
        quit()
elif card_type=="3":
    print(f"Your account balance is ${initial_amount}")
    while True:
        card=input("Enter 1 to take your card ")
        if card!="1":
            continue
        else:
            print("Thank you for banking with us")
            for seconds in range(3,0,-1):
                print(seconds)
                time.sleep(1)
            time_watch=time.localtime()
            local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
            print(local_time)
            print("Please take your card")
else:
    print("Invalid input")
    for seconds in range(2,0,-1):
        print(seconds)
        time.sleep(1)
    time_watch=time.localtime()
    local_time=time.strftime("%B %d %Y %H:%M:%S", time_watch)
    print(local_time)
    print("Please take your card")
    quit()