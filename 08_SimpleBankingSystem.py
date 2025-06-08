#Simple banking system to check balance, withdraw and deposit balance, and update balance and store the updated balance in a txt file.
import os

BALANCE_FILE = "balance.txt"

#1
def initialize_balance():
    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "w") as file:
            file.write("0")

#2 Read Current balance
def current_balance():
    with open(BALANCE_FILE, "r") as file:
        balance = file.read()
        return float(balance) if balance else 0.0
    
#3 Update balance
def update_balance(newBalance):
    with open(BALANCE_FILE, "w") as file:
        file.write(str(newBalance))

#4 Deposit amount
def deposit(amount):
    if amount <= 0:
        print("Enter a valid amount greater than 0.")
        return
    balance = current_balance()
    newBalance = balance + amount
    update_balance(newBalance)
    print(f"Amount deposited successfully, new balance = {newBalance}rs")

#5 Withdraw amount
def withdraw(amount):
    if amount <= 0:
        print("Enter a valid amount greater than 0.")
        return
    balance = current_balance()
    if amount > balance:
        print("Unsufficient balance!")
    else:
        newBalance = balance - amount
        update_balance(newBalance)
        print(f"{amount}rs withdrawn successfully, new balance = {newBalance}rs")

#6 Menu
def menu():
    while True:
        print("\n------ Simple Banking System ------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Current Balance: ₹{current_balance()}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            withdraw(amount)
        elif choice == "4":
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice. Please try again.")

#7 Calling the initialization and menu methods
initialize_balance()
menu()