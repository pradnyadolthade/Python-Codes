def DigitLength(No):
        digits = 0
        digits = len(str(No))
        return digits
             
        

def main():
    print("Enter a number :")
    Num = int(input())

    Result = DigitLength(Num)
    print(Result)
    

if __name__ == "__main__":
    main()