class Account:
    def __init__(self,balance,accountNumber) -> None:
        self.balance=balance
        self.accountNumber=accountNumber
    
    #Debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited",self.balance,"is your balance")
    
    #Credit method
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited",self.balance,"is your balance")  
    
acc = Account(10000,1234)
acc.credit(68)