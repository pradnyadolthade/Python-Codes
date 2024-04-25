from Arithmatic import Add,Sub,Mul,Div


def main():
    print("Enter first number :")
    Num1 = int(input())
    print("Enter second number :")
    Num2 = int(input())
    print("Addition of numbers :", Add(Num1 , Num2))
    print("Substraction of numbers :", Sub(Num1 , Num2))
    print("Multiplication of numbers :", Mul(Num1 , Num2))
    print("Division of numbers :", Div(Num1 , Num2))


if __name__ == "__main__":
    main()
