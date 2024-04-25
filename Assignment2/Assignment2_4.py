
def FactAdd(Val):
    Sum = 0
    for num in range(1,Val):
        if(Val % num == 0):
            Sum = Sum + num
    return Sum



def main():
    print("Enter a number :")
    num = int(input())

    Result = FactAdd(num)
    print(Result)




if __name__ == "__main__":
    main()