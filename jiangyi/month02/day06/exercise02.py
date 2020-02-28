import os
import time

def sum():
    result=0
    for i in range(9999):
        result+=i
    print("结果：%.2f万"%(result))

def write():
    with open("file.txt","w") as f:
        for i in range(9999):
            f.write("hello world\n")

tm=time.time()

pid=os.fork()

if pid<0:
    print("进程创建失败")
elif pid==0:
    sum()

else:
    write()
    

print("执行时间：",time.time()-tm)