class User:
    def __init__(self, name):
        self.name = name
        self.accounts = []
    def new_account(self, number):
        self.accounts.append(BankAccount(number, int_rate=0.02))
        return self
    def make_deposit(self, number, amount):
        self.accounts[number].balance += amount
        return self
    def make_withdrawal(self, number, amount):
        if(amount > self.accounts[number].balance):
            print("This would overdraw the account")
        else:
            self.accounts[number].balance -= amount
        return self
    def display_user_balance(self, number):
        print("User: " + str(self.name), "Account #" + str(number), "Balance: " + str(self.accounts[number].balance))
        return self
    
    def make_transfer(self, number1, amount, user2, number2):
        if(amount < self.accounts[number1].balance):
            self.make_withdrawal(number1, amount)
            user2.make_deposit(number2, amount)
            print("Transfer made!")
            print("User: " + str(self.name), "Balance: " + str(self.accounts[number1].balance))
            print("User: " + str(user2.name), "Balance: " + str(user2.accounts[number2].balance))
            return self

class BankAccount:
    all_accounts = []
    def __init__(self, acc_num, int_rate):
        self.acc_num = acc_num
        self.int_rate = int_rate
        self.balance = 0
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        if(amount > self.balance):
            print("This would overdraw the account")
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(" Balance: " + str(self.balance))
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

Ryan = User("Ryan")
Nick = User("Nick")
Tram = User("Tram")

Ryan.new_account(0).new_account(1).new_account(2)
Nick.new_account(0).new_account(1).new_account(2)
Tram.new_account(0).new_account(1).new_account(2)


Ryan.make_deposit(0, 500).make_deposit(1, 1000).make_deposit(2, 2000).make_withdrawal(0, 150).display_user_balance(0).display_user_balance(1).display_user_balance(2)

Nick.make_deposit(0, 500).make_deposit(1, 1000).make_withdrawal(0, 100).make_withdrawal(1, 200).display_user_balance(0).display_user_balance(1)

Tram.make_deposit(0, 1000).make_withdrawal(0, 100).make_withdrawal(0, 100).make_withdrawal(0, 100).display_user_balance(0)

Ryan.make_transfer(0, 50, Tram, 0)

Ryan.accounts[0].yield_interest()
Ryan.display_user_balance(0)
