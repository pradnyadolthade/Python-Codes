#Accept number and print its summation with recurssion 
sum = 0

def DisplaySum(no):
    global sum
    if no == 0:
        return 0
    else:
        sum = sum + no%10
        no = int(no/10)
        DisplaySum(no)
    
    return sum

    
    
    
   
        
        



def main():
    print("Enter Number :")
    Val = int(input())
    ans = DisplaySum(Val)
    print(ans)
if __name__ == "__main__":
    main()