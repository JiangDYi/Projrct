
from multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("我叫 %s "%name)
        print("-----------------------")

p=Process(target=worker,args=(1,"小明"))
p.start()
p.join(3)
print("*************")