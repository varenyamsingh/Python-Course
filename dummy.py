# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Method to debit amount from balance
    def debit(self, amount):
        self.balance -= amount
        print(amount, "was debited")
        print("total balance is:", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print(amount, "was credited")
        print("total balance is:", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(90000, 123456)
acc1.debit(500)
acc1.credit(1000)
acc1.credit(80000)

