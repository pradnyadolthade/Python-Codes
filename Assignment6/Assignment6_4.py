"""
4.Design python application which creates three threads as small, capital, digits. All the
threads accepts string as parameter. Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of
digits. Display id and name of each thread.
"""
import threading
import os

def small(str):
    sm =[]
    for letter in str:
        if letter.islower():
            sm.append(letter)
    print("Lower letters are :",sm)
    print("PID of small function ",os.getpid())

def capital(str):
    cp =[]
    for letter in str:
        if letter.isupper():
            cp.append(letter)
    print("Capital letters are ",cp)
    print("PID of capital function ",os.getpid())


def digits(str):
    dg = []
    for letter in str:
        if letter.isdigit():
            dg.append(letter)
    print("Digits are :",dg)
    print("PID of digit function ",os.getpid())



def main():
    print("PID of main function ",os.getpid())
    print("Enter a string :")
    name = input()

    p1 = threading.Thread(target=small, args=(name,))
    p2 = threading.Thread(target=capital, args=(name,))
    p3 = threading.Thread(target=digits, args=(name,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

if __name__ == "__main__":
    main()