"""
thread_server 基于多线程的并发
重点代码
"""

from socket import *
from threading import Thread

# 全局变量
HOST = '0.0.0.0'
PORT = 11111
ADDR = (HOST, PORT)

def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')
    c.close()

# 创建监听套接字
s = socket()
s.bind(ADDR)
s.listen(3)

print("listen the prot 11111")

# 循环等待客户端链接
while True:
    c, addr = s.accept()
    print("connect from", addr)

    #创建线程处理客户端请求
    t=Thread(target=handle,args=(c,))
    # t.setDaemon(True)#分支线程随主线程退出
    t.start()

