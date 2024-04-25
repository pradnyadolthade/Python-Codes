
def PosNegNum(no):
    if(no > 0):
        return 1
    elif(no < 0):
        return 2
    else:
        return 3


def main():
    print("Enter a number :")
    Num = int(input())
    Result = PosNegNum(Num)
    if(Result == 1):
        print("Positive Number")
    elif(Result == 2):
        print("Negative Number")
    elif(Result == 3):
        print("Zero")


if __name__ == "__main__":
    main()