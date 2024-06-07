class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0 

    def Accept(self,Radius):
        self.Radius = Radius

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of Circle :",self.Radius)
        print("Area of Circle :",self.Area)
        print("Circum of Circle :",self.Circumference)


obj = Circle()
radius = int(input("enter radius :"))
obj.Accept(radius)
obj.CalculateArea()
obj.CalculateCircumference()
obj.Display()



     

