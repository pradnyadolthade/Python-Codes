def Addition(Nlist):
    sum = 0
    for val in Nlist:
        sum += val 
    return sum 

def main():
    print("Number of elements :")
    N = int(input())
    
    print("Enter Elements :")
    Values = []
    for num in range(N):
        num = int(input())
        Values.append(num)
    Result = Addition(Values)
    print("Addition is :",Result)

if __name__ == "__main__":
    main()