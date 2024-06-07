class Arithmatic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        self.Value3 = 0 

    def Accept(self,Value1,value2):
        self.Value1 = Value1
        self.Value2 = value2

    def Addition(self):
        return self.Value1 + self.Value2
    def subtraction(self):
        return self.Value1 - self.Value2
    def multiplication(self):
        return self.Value1 * self.Value2
    def division(self):
        return self.Value1 / self.Value2
    
 

obj = Arithmatic()
no1 = int(input("enter first no :"))
no2 = int(input("enter second no :"))

obj.Accept(no1,no2)
add = obj.Addition()
sub = obj.subtraction()
mul = obj.multiplication()
div = obj.division()

print(f"add :{add}\nsub :{sub}\nmul:{mul}\ndiv:{div}")




     

