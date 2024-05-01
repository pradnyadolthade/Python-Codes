def checkFrequency(Nlist,check):
    freq = 0
    for val in Nlist:
        if check == val:
            freq = freq + 1 
    return freq  
        
def main():
    print("Number of elements :")
    N = int(input())
    
    print("Enter Elements :")
    Values = []
    for num in range(N):
        num = int(input())
        Values.append(num)
    print("Element to search :")
    search = int(input())
    Result = checkFrequency(Values,search)
    print("Frequency of the Value is :",Result)

if __name__ == "__main__":
    main()