class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,cash):
        if cash > 0:
            self.balance = self.balance + cash
            print (f"the operation to deposit {cash} tenge was successful")
        else:
            print("you must deposit more than 0 tenge")
    def withdraw(self,mycash):
        if mycash <= self.balance:
            self.balance = self.balance - mycash
            print (f"you withdrew money in the amount of {mycash} tenge")
        else:
            print ("insufficient funds")

bank = Bank("hmm", 570)
bank.deposit(30)
bank.withdraw(700)
bank.deposit(100)
bank.withdraw(700)
            
