#write a program which contains one function named as ADD() which accepts two numbers from the user and return addition of that two numbers.

def Add(no1, no2):
    Ans = 0
    Ans = no1 + no2
    return Ans

def main():
    print("Enter first number :")
    No1 = int(input())
    print("Enter second number :")
    No2 = int(input())

    Result = Add(No1,No2)
    print("Addition is : ",Result)

if __name__ == "__main__":
    main()