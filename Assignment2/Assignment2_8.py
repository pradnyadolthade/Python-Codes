def DisplayPattern(No):
        for i in range(1,No+1):
             j = 1
             while j <= i:
                  print(j,end=" ")
                  j = j + 1
             print() 
                  
                  
        

def main():
    print("Enter a number :")
    Num = int(input())

    DisplayPattern(Num)
    

if __name__ == "__main__":
    main()