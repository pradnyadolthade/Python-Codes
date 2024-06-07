class Numbers:
    def __init__(self, val):
        self.val = val

    def chkPrime(self):
        flag = True
        for i in range(2,self.val//2+1):
            if(self.val%i==0):
                flag= False
                break
            else:
                flag = True
        return flag


    def chkPerfect(self):
        sum = 0
        for i in range(1,self.val//2+1):
            if(self.val % i == 0):
                sum = sum + i
        if self.val == sum:
            return True
        else:
            return False

    def sumFactors(self):
        sum = 0
        for i in range(1,self.val//2+1):
            if(self.val % i == 0):
                sum = sum + i
        print("Sum of factors :",sum)
    
    def Factors(self):
        fact = []
        for i in range(1,self.val//2+1):
            if(self.val % i == 0): 
                fact.append(i)
        
        print("Factors :",fact) 


userNo = int(input("Enter number :"))
obj = Numbers(userNo)
ret = obj.chkPrime()
if(ret):
    print("Prime Number")
else:
    print("Not Prime")

ret = obj.chkPerfect()
if(ret):
    print("Perfect Number")
else:
    print("Not Perfect")

obj.Factors()
obj.sumFactors()
