def DisplayPattern(No):
        for i in range(1,No+1):
             print()
             for i in range(1,No+1):
                  print(i, end = " ")
        

def main():
    print("Enter a number :")
    Num = int(input())

    DisplayPattern(Num)
    

if __name__ == "__main__":
    main()