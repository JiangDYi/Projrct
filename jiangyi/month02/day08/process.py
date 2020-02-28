from time import sleep
import multiprocessing

a=1

#进程执行函数
def fun():
    print("开始一个进程")
    sleep(2)
    global a
    print("a=",a)
    a=100
    print("子进程执行结束")


#创建进程对象
p=multiprocessing.Process(target=fun)

#启动进程 此时进程诞生 执行函数作为进程的执行内容
p.start()

#父进程
sleep(3)
print("父进程事件")
print("a:",a)
#回收进程 防止僵尸进程
p.join()
print("---------------------------------")