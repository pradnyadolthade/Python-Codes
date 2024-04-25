

def CheckDivisible(Number):
    if( Number % 5 == 0):
        return True
    else:
        return False



def main():
    print("Enter a number :")
    num = int(input())
    Result = CheckDivisible(num)
    if (Result == True):
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()