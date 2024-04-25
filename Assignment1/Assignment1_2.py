def ChkNum(no):
    if(no%2==0):
        return True
    else:
        return False


def main():
    print("Enter a number :")
    No = int(input())
    Result = ChkNum(No)
    if(Result == True):
        print("Even Number")
    else:
        print("Odd Number")


if __name__ == "__main__":
    main()