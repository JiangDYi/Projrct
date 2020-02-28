from multiprocessing import Process
import time

def fun():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

p=Process(target=fun,name="TT")

p.daemon=True

p.start()

print("name:",p.name)
print("is alive:",p.is_alive())
print("PID",p.pid)
time.sleep(2)