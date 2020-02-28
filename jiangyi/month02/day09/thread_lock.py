
from threading import Thread,Lock

a=b=0
lock=Lock()

def value():
    while True:
        lock.acquire()
        if a != b:
            print("a=%d,b=%d"%(a,b))
        lock.release()

t=Thread(target=value)
t.start()

while True:
    lock.acquire()
    a+=1
    b+=1
    lock.release()


t.join()