

def Factorial(No):
    fact = 1
    while(No>=1):
        fact = fact * No
        No = No - 1
    return fact



def main():
    print("Enter number :")
    Num = int(input())
    Result = Factorial(Num)
    print(Result)
  
if __name__ == "__main__":
    main()

