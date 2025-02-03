class BankAccount:
    def __init__(self, name, balance=0):
        self.account_name = name
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.account_name, self.balance + other.balance)

    def __sub__(self, amount):
        return BankAccount(self.account_name, self.balance - amount)

    def __str__(self):
        return f"{self.account_name}'s account balance: ${self.balance:.2f}"

account1 = BankAccount("Rajeev", 1000)
account2 = BankAccount("Rajeev", 500)

combined_account = account1 + account2
print(combined_account)

new_balance = combined_account - 200
print(new_balance)
