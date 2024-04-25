def checkPrime(No):
    flag = False
    if No <= 1:
        flag = False
    if No == 2:
        flag = True
    for val in range(2,No):
        if(No % val == 0):
            flag = False
            break    
        else:
            flag = True
    return flag



def main():
    print("Enter a number :")
    Num = int(input())

    Result = checkPrime(Num)
    if(Result == True):
        print("It is Prime Number")
    else:
        print("It is Not a Prime Number")


if __name__ == "__main__":
    main()