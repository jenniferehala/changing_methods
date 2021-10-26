class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self


Picard = User('Picard', 'picard@gmail.com')
Riker = User('Riker','riker@gmail.com')
Worf = User('Worf', 'worf@gmail.com')

Picard.make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawal(50).display_user_balance()

Riker.make_deposit(200).make_deposit(200).make_withdrawal(50).make_withdrawal(50).display_user_balance()

Worf.make_deposit(200).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()