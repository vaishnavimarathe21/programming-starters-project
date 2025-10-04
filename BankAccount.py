class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def display(self):
        print(f"Account: {self.name}, Balance: {self.balance}")
accounts = {}
def create_account():
    name = input("Enter name: ")
    if name not in accounts:
        accounts[name] = BankAccount(name)
def deposit_money():
    name = input("Enter name: ")
    if name in accounts:
        amount = float(input("Amount: "))
        accounts[name].deposit(amount)
def withdraw_money():
    name = input("Enter name: ")
    if name in accounts:
        amount = float(input("Amount: "))
        accounts[name].withdraw(amount)
def display_account():
    name = input("Enter name: ")
    if name in accounts:
        accounts[name].display()
while True:
    print("1.Create 2.Deposit 3.Withdraw 4.Display 5.Exit")
    choice = input("Choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        display_account()
    elif choice == "5":
        break
