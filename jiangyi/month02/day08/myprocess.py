from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, value):
        super().__init__()
        self.value= value

    def fun1(self):
        print("1")
    def fun2(self):
        print("2")

    def run(self):
        self.fun1()
        self.fun2()


p = MyProcess(1) # 定义进程对象
p.start() # 将run作为进程执行
p.join()