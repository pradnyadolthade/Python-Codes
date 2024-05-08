"""
3.Design python application which creates two threads as evenlist and oddlist. Both the
threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input
list and display the addition.
"""
import threading

def EvenList(NumList):
    sumE = 0
    for i in NumList:
        if i%2 == 0:
            sumE = sumE + i
    print("Addition of Even numbers from list:",sumE)
    

def OddList(NumList):
    sumO = 0
    for i in NumList:
        if i%2 != 0:
            sumO = sumO + i
    print("Addition of Odd numbers from list :",sumO)
    
def main():
    print("enter number of values :")
    No = int(input())
    noList = []
    print("Enter number :")
    for num in range(No):
        val = int(input())
        noList.append(val)

    p1 = threading.Thread(target= EvenList, args=(noList,))
    p2 = threading.Thread(target= OddList, args=(noList,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()