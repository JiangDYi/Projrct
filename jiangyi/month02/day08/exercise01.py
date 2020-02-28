"""
获取100000以内的质数之和
计算使用一个单进程程序执行该任务的用时
再计算使用4个进程执行该任务用时
    思路 ： 100000分成4分 1----25000  25001---50000 以此类推
再计算使用10个进程执行该任务用时
    思路 ： 100000分成10分 1----10000  10001---20000 以此类推
"""
from multiprocessing import Process
import time

def timeit(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("函数执行时间：",end_time-start_time)
        return res
    return  wrapper

def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

@timeit
def no_process():
    prime=[]
    for i in range(1,10001):
        if isPrime(i):
            prime.append(i)
    print(sum(prime))

# no_process()
class Prime(Process):
    def __init__(self,begin,end):
        super().__init__()
        self.begin=begin
        self.end=end

    def run(self):
        prime=[]
        for i in range(self.begin,self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))

@timeit
def process_4():
    jobs=[]
    for i in range(1,10001,2500):
        p=Prime(i,i+2500)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()

process_4()