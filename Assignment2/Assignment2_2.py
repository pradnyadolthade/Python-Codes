


def DisplayPattern(num):
    for i in range(num):
        print()
        for i in range(num):
            print("*",end=" ")



def main():
    print("Enter number :")
    Num = int(input())
    DisplayPattern(Num)
  
if __name__ == "__main__":
    main()

