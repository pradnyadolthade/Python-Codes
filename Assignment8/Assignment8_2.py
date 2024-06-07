class BankAccount:
    ROI = 10.5
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Deposit(self,amt):
        self.Amount = self.Amount+amt
    def Withdraw(self,amt):
        self.Amount = self.Amount-amt

    def CalculateIntrest(self):
        interest = self.Amount * BankAccount.ROI
        print("interest amt :",interest)

    def Display(self):
        print("Name :",self.Name) 
        print("Amount :",self.Amount)

obj1 = BankAccount("Ram",10000)
obj1.Display()
obj1.Deposit(20000)
obj1.Display()
obj1.Withdraw(10000)
obj1.Display()
obj1.CalculateIntrest()

obj2 = BankAccount("Shyam",5000)
obj2.Display()
obj2.Deposit(2000)
obj2.Display()
obj2.Withdraw(500)
obj2.Display()
obj2.CalculateIntrest()
