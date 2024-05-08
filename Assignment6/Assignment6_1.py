"""
1.Design python application which creates two thread named as even and odd. Even
thread will display first 10 even numbers and odd thread will display first 10 odd
numbers.
"""
import threading

def EvenDisplay():
    print("List of Even Numbers :")
    x =2
    for i in range(20):
        print(x)
        x  = x + 2

def OddDisplay():
    print("List of ODD Numbers :")
    x = 1
    for i in range(20):
        print(x)
        x  = x + 2

    


def main():

    p1 = threading.Thread(target= EvenDisplay)
    p2 = threading.Thread(target= OddDisplay)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
if __name__ == "__main__":
    main()