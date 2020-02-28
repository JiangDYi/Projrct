#!/usr/bin/python3

# print("hello world!")

"""
获取100000以内的质数之和
计算使用一个单进程程序执行该任务的用时
再计算使用4个进程执行该任务用时
    思路 ： 100000分成4分 1----25000  25001---50000 以此类推
再计算使用10个进程执行该任务用时
    思路 ： 100000分成10分 1----10000  10001---20000 以此类推
"""

import time
from multiprocessing import Process

def timeit(f):
    def wrapper(*args,**kwargs):
        print(f)
        start_time = time.time()
        # 可以往被装饰的函数传参
        res = f("hello","python")
        end_time = time.time()
        print("函数执行时间：",end_time-start_time)
        return res
    return  wrapper

# 判断一个数是不是质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
           return False
    return True

class Prime(Process):
    def __init__(self,begin,end):
        super().__init__()
        self.begin = begin
        self.end = end

    def run(self):
        prime = []
        for i in range(self.begin, self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))


@timeit
def process_10(A,B):
    print(A)
    print(B)
    jobs = []
    for i in range(1,500001,10000):
        p = Prime(i,i+10000)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()


if __name__ == '__main__':

    process_10() # 函数执行时间： 19.56751275062561