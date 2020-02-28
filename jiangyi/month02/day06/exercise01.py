from socket import *

def request():
    data = c.recv(2048)
    
    if not data:
        return
    info=data.decode().split()[1]
    print('请求内容',info)
    if info=='/':

        f = open('index.html', 'r')
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type:text/html\r\n"
        data += "\r\n"
        data += f.read()
        f.close()
    else:
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type:text/html\r\n"
        data += "\r\n"
        data += "sorry..."

    c.send(data.encode())

    c.close()


# 创建套接字
s = socket()
s.bind(('127.0.0.1', 8000))
s.listen(3)

# 等待客户端（浏览器）链接
while True:
    c, addr = s.accept()
    print("Connect from", addr)
    request()



s.close()