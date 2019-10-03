class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.make_deposit (amount)
        return self
    def make_withdrawal(self, amount):
        self.account.make_withdrawal (amount)
        return self
    def make_transfer(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.rate = int_rate
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Your interest rate is {self.rate} and your balance is now {self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance * self.rate + self.balance
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jim = User("Jimmathy Halpert", "JHalpert@dundermifflin.com")
print(guido.name, "*balance*", guido.account.balance)
guido.make_deposit(100).make_deposit(60).make_deposit(90) .account.yield_interest()
print(guido.name, "*balance*", guido.account.balance)