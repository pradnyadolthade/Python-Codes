
def DisplayStar(Num):
    for i in range(Num):
        print("*",end=" ")



def main():
    print("Enter a number of star you want to display :")
    Num = int(input())
    DisplayStar(Num)




if __name__ == "__main__":
    main()