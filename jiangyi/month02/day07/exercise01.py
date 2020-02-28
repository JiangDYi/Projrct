"""
利用二级子进程的方法处理僵尸
【1】 父进程创建子进程，等待回收子进程
【2】 子进程创建二级子进程然后退出
【3】 二级子进程称为孤儿，和原来父进程一同执行事件
"""

import os
import time
import signal


def fun1():
    print("开始第一件事")
    time.sleep(4)
    print("结束第一件事")

def fun2():
    print("开始第二件事")
    time.sleep(3)
    print("结束第二件事")



pid = os.fork()

if pid < 0:
    print("进程创建失败")
elif pid == 0:
    p=os.fork()
    if p<0:
        print('创建失败')
    elif p==0:
        fun2()
    else:
        os._exit(0)
else:
    os.wait()
    fun1()
