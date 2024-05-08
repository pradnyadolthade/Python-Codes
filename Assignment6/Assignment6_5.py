"""
5.Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.
"""

import threading
import time

def Thread1():
    print("Numbers from 1 to 51 :\n")
    for i in range(1,51):
        print(i)
        time.sleep(0.1)
        
def Thread2():
    print("Numbers from 1 to 51 :\n")
    for i in range(50,0,-1):
        print(i)
        time.sleep(0.1)

def main():
 
    p1 = threading.Thread(target=Thread1, )
    p2 = threading.Thread(target=Thread2,)


    p2.start()
    p2.join()

    p1.start()
    p1.join()

if __name__ == "__main__":
    main()