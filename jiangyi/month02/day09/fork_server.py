"""
基于fork的多进程并发
重点代码
"""

from socket import *
import os
import signal

#全局变量
HOST='0.0.0.0'
PORT=11111
ADDR=(HOST,PORT)

def handle(c):
    while True:
        data=c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')
    c.close()


#创建监听套接字
s=socket()
s.bind(ADDR)
s.listen(3)

print("listen the prot 11111")
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

#循环等待客户端链接
while True:
    c,addr=s.accept()
    print("connect from",addr)

    #创建一个新的进程处理客户端请求
    pid=os.fork()
    if pid==0:
        #处理客户端请求
        handle(c)
        os._exit(0)#子进程处理完客户端请求就退出
    else:
        #出错或者父进程都继续等待客户端链接
        continue
s.close()