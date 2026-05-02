print("Welcome To The ATM Simulator Hassan Application")
balance = 1000
pin = 1234
amount = int(input("Enter Your Deposite "))
if amount > 0:
    balance = balance + amount
pin_users = int(input("Enter Your Pin "))
if pin_users == pin:
    
    print(" Deposite Suscessefull")
    print("Your New Balance is", balance)
else:
    print("wrong pin")


amount = int(input("Enter Your amount to Withdraw "))
if amount > 0:
    balance = amount - balance
pin_users = int(input("Enter Your Pin "))
if pin_users == pin:
    
    print(" Withdrawal Suscessefull")
    print("Your New Balance is", balance)
else:
    print("wrong pin")


    
    