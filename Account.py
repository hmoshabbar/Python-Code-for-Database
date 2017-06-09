# First i am defining a class Account
class Account(object):
    def __init__(self,Account_Holder_Name,Account_Number,Account_Balance,Credit_line=2500):
        self.holder=Account_Holder_Name
        self.number=Account_Number
        self.balance=Account_Balance
        self.credit=Credit_line

    def  Deposit(self,amount):
        self.balance=amount

    def withdraw(self,amount):
        if (self.balance-amount<-self.credit):
            return False
        else:
            self.balance -=amount
            return True
        

    def balance(self):
        return self.balance

    def transfer(self,target,amount):
        if (self.balance-amount<-self.credit):
            return False
        else:
            self.balance -=amount
            target.balance +=amount
            return True
        
