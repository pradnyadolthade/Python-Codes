def DigitAdd(No):
    sum = 0
    for num in str(No):
        sum = sum + int(num)
    return sum

             
        

def main():
    print("Enter a number :")
    Num = int(input())

    Result = DigitAdd(Num)
    print(Result)
    

if __name__ == "__main__":
    main()