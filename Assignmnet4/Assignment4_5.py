from functools import reduce

def chckPrime(num):
    flag = True
    if num == 1:
        flag = False
    for i in range(2,num):     
        if num % i == 0:              
            flag = False
            break
    return flag

def mul(num):
    return num * 2

def Max(A,B):
    max = A
    if B > A:
        max = B
    return max

def main():
    print("Enter number of elements :")
    N = int(input())
    print("Enter numbers :")
    num = []
    for val in range(N):
        val = int(input())
        num.append(val)

    fResult = list(filter(chckPrime, num))
    print("List after filter :",fResult)

    mResult = list(map(mul, fResult))
    print("List after map :",mResult)

    rResult = reduce(Max, mResult)
    print("List after reduce :",rResult)



if __name__ == "__main__":
    main()