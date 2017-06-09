# First i am defining a class Account
class Account(object):
    def __init__(self):
       self.balance=0

    def  Deposit(self,amount):
        self.balance +=amount
        return self.balance

    def withdraw(self,amount):
        if ((self.balance-amount)<0):
            return "You Entered balanced is not Vaild"
        else:
            self.balance -=amount
            return self.balance
        

    def balance(self):
        return self.balance

    def transfer(self,amount):
        if ((self.balance-amount)<0):
            return 'You Cant Transfer Money You balance low'
        else:
            self.balance -=amount
            return "Transaction is sucessfull Now Your Main Balance:" ,self.balance
        
