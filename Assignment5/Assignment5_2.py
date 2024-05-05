#display pattern with recurssion 
i = 1

def DisplayPattern(no):
    global i 
    if(i <= no):
        print(i, end=" ")
        i = i + 1
        DisplayPattern(no)



def main():
    print("Enter Number :")
    Val = int(input())
    DisplayPattern(Val)
if __name__ == "__main__":
    main()