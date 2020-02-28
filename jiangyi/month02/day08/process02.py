from multiprocessing import Process
from time import sleep
import os

def t1():
    sleep(2)
    print("吃饭")
    print(os.getppid(),"--",os.getpid())

def t2():
    sleep(3)
    print("睡觉")
    print(os.getppid(),"--",os.getpid())

def t3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),"--",os.getpid())

jobs=[]
for t in [t1,t2,t3]:
    p=Process(target=t)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()