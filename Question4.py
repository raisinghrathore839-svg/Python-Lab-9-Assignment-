class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display_balance(self):
        print(self.account_holder, self.balance)

a = BankAccount("Raisingh", 1000)
a.deposit(500)
a.withdraw(200)
a.display_balance()
