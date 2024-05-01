def MinNumber(Nlist):
    min = Nlist[0]
    for num in Nlist[1:]:
        if num < min:
            min = num   
    return min  

'''
second method 

def MinNumber(Nlist):
    min = min(Nlist)
    return min  

'''
         

def main():
    print("Number of elements :")
    N = int(input())
    
    print("Enter Elements :")
    Values = []
    for num in range(N):
        num = int(input())
        Values.append(num)
    Result = MinNumber(Values)
    print("Minimum Value is :",Result)

if __name__ == "__main__":
    main()