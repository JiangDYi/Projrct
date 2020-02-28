import os
from time import sleep

a=1

pid=os.fork()

if pid<0:
    print('创建失败')
elif pid==0:
    print('a=',a)
    a=1000
    print('新的进程')
else:
    sleep(0.5)
    print('原来的进程')
    print('a:',a)

print('s',a)