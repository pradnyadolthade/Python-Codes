from functools import reduce

def main():
    print("Enter number of elements :")
    N = int(input())
    print("Enter numbers :")
    num = []
    for val in range(N):
        val = int(input())
        num.append(val)

    fResult = list(filter((lambda A : A % 2 == 0), num))
    print("List after filter :",fResult)

    mResult = list(map((lambda A : A * A), fResult))
    print("List after map :",mResult)

    rResult = reduce((lambda A , B: A + B), mResult)
    print("List after reduce :",rResult)



if __name__ == "__main__":
    main()