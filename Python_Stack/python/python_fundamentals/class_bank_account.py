class BankAccount:
    def __init__(self, int_rate, balance, username):
        self.rate = int_rate
        self.account_balance = balance
        self.name = username
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print(f"{self.name} your interest rate is {self.rate} and your balance is now {self.account_balance}")
        return self
    def yield_interest(self):
        self.account_balance = self.account_balance * self.rate
        return self
account1 = BankAccount(2, 100, "Dwight")
account2 = BankAccount(5, 200, "Andy")
account1.make_deposit(20).make_deposit(60).make_deposit(30).make_withdrawal(75) .yield_interest() .display_account_info()
account2.make_deposit(80).make_deposit(100).make_withdrawal(20).make_withdrawal(40).make_withdrawal(15).make_withdrawal(50) .yield_interest() .display_account_info()