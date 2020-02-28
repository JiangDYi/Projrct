from socket import *
import time

ADDR=('127.0.0.1',8999)

s=socket()

s.connect(ADDR)

f=open('justin.jpg','rb')

while True:
    data=f.read(1024)
    if not data:
        time.sleep(0.2)
        s.send("文件发送完毕".encode())
        break
    s.send(data)

f.close()
s.close()
