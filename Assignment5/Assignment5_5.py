fact = 1
def Factorial(No):
    global fact
    if(No>1):
        fact = No * Factorial(No-1)
    return fact

def main():
    print("Enter Number :")
    num = int(input())
    Res = Factorial(num)
    print("Factorial is ", Res)

if __name__ == "__main__":
    main()