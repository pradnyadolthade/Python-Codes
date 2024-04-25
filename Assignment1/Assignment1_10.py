
def DisplayLength(Value):
    res = 0
    res = len(Value)
    return res




def main():
    print("Enter a String :")
    Val = input()
    Result = DisplayLength(Val)
    print(Result)



if __name__ == "__main__":
    main()