class Account:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
        print(f"{amount} deposited successfully. Current balance of {self.name} is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"You don't have sufficiant balance. Your balance is {self.balance}")
        else:
            self.balance-=amount
            print(f"Amount {amount} withdrawn successfully. Current balance of {self.name} is {self.balance}")
    def getbalance(self):
        return self.balance
class ATM:
    def __init__(self):
        self.users={}
    def createAccount(self,name):
        if name in self.users:
            print("Account already exists.")
        else:
            account= Account(name)
            self.users[name]=account
            print("Account created successfully")
    def getMyAccount(self,name):
        if name in self.users:
            return self.users[name]
            print(f"Your account named : {name} is accessed")
        else:
            print("Account does not exist")
atm = ATM()
atm.createAccount('Ramnath')
user=atm.getMyAccount('Ramnath')
if user:
    user.deposite(1000000)
    user.withdraw(500000)
atm.createAccount('Rohan')
user1=atm.getMyAccount('Rohan')
if user1:
    user1.deposite(100000)
    user1.withdraw(140)
user.deposite(100)
