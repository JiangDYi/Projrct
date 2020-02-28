
from threading import Thread,Lock

lock1=Lock()
lock2=Lock()

def print_num():
    for i in range(1, 53,2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()

def print_char():
    for i in range(65, 91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t2=Thread(target=print_num)
t1=Thread(target=print_char)

lock2.acquire()

t1.start()
t2.start()
t1.join()
t2.join()




