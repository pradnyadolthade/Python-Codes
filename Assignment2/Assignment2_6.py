def DisplayPattern(No):
        while 1 <= No:
            print("*  " * No)
            No = No - 1

def main():
    print("Enter a number :")
    Num = int(input())

    DisplayPattern(Num)
    

if __name__ == "__main__":
    main()