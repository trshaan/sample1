class bankaccount:
    def __init__(self, balance):
        self.balance=balance
    def deposit(self, amount):
        self.balance=self.balance+amount
    def withdraw(self, amount):
        if (self.balance-amount<0):
            print("no money!!!!")
        else:
            self.balance=self.balance-amount
    def show_balance(self):
        print(self.balance)
b1 = bankaccount(100)
b1.withdraw(200)   # refuse — more than balance
b1.withdraw(100)   # ok — exactly the balance, should work now
b1.deposit(50)     # now 50
b1.show_balance()  # should print 50