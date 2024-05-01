from MarvellousNum import chkPrime

def ListPrime(primelist):
    sum = 0
    for val in primelist:
        sum = sum + val 
    return sum
        
def main():
    print("Number of elements :")
    N = int(input())
    
    print("Enter Elements :")
    Values = []
    prime = []
    for num in range(N):
        num = int(input())
        Values.append(num)
        if chkPrime(num):
            prime.append(num)
    print(prime)
        
    Result = ListPrime(prime)
    print("Addition of prime number is :",Result)

if __name__ == "__main__":
    main()