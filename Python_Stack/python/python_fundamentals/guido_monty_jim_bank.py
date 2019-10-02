class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def make_transfer(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jim = User("Jimmathy Halpert", "JHalpert@dundermifflin.com")
print("\n")
print(guido.name, "*balance*", guido.account_balance)
guido.make_deposit(100).make_deposit(60).make_deposit(90)
print(guido.name, "*balance*", guido.account_balance)
guido.make_withdrawal(50)
print(guido.name, "*balance*", guido.account_balance, "\n")
print(monty.name, "*balance*", monty.account_balance)
monty.make_deposit(100).make_deposit(40)
print(monty.name, "*balance*", monty.account_balance)
monty.make_withdrawal(30).make_withdrawal(20)
print(monty.name, "*balance*", monty.account_balance, "\n")
print(jim.name, "*balance*", jim.account_balance)
jim.make_deposit(600)
print(jim.name, "*balance*", jim.account_balance)
jim.make_withdrawal(80).make_withdrawal(40)
print(jim.name, "*balance*", jim.account_balance, "\n")
print("*transfer*", guido.name, "-to-", jim.name, "\n")
guido.make_transfer(jim, 75)
print(guido.name, "*balance*", guido.account_balance)
print(jim.name, "*balance*", jim.account_balance, "\n")
print(monty.name, "*balance*", monty.account_balance, "\n")