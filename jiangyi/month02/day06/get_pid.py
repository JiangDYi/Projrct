import os

pid=os.fork()

if pid<0:
    print("进程创建失败")
elif pid==0:
    print("Child PID:",os.getpid())
    print("Get Parent PID:",os.getppid())

else:
    print()
    print("原来的进程")

print("实验完毕")