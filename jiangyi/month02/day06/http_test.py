"""
http基本演示
"""
from socket import *

# 创建套接字
s = socket()
s.bind(('127.0.0.1', 8000))
s.listen(3)

# 等待客户端（浏览器）链接
c, addr = s.accept()
print("Connect from", addr)

# http请求
data = c.recv(2048)
print(data.decode())

data="""HTTP/1.1 200 OK
Content-Type:text/html

hello world
"""

c.send(data.encode())

c.close()
s.close()