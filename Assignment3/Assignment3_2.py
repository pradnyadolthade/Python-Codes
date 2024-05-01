def MaxNumber(Nlist):
    max = Nlist[0]
    for num in Nlist[1:]:
        if num > max:
            max = num   
    return max  

'''
second method 

def MaxNumber(Nlist):
    max = max(Nlist)
    return max  

'''
         

def main():
    print("Number of elements :")
    N = int(input())
    
    print("Enter Elements :")
    Values = []
    for num in range(N):
        num = int(input())
        Values.append(num)
    Result = MaxNumber(Values)
    print("Maximum Value is :",Result)

if __name__ == "__main__":
    main()