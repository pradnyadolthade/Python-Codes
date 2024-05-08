"""
2.Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer. Evenfactor thread will display
addition of even factors of given number and oddfactor will display addition of odd
factors of given number. After execution of both the thread gets completed main
thread should display message as “exit from main”.
"""
import threading

def EvenFactor(Num):
    sumE = 0
    for i in range(1,Num):
        if Num % i == 0:
            if i%2 == 0:
                sumE = sumE + i
    print("Addition of Even factors :",sumE)
    

def OddFactor(Num):
    sumO = 0
    for i in range(1,Num):
        if Num % i == 0:
            if i%2 != 0:
                sumO = sumO + i
    print("Addition of Odd factors :",sumO)
    
def main():
    print("enter number :")
    No = int(input())

    p1 = threading.Thread(target= EvenFactor, args=(No,))
    p2 = threading.Thread(target= OddFactor, args=(No,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Exit from main")
if __name__ == "__main__":
    main()