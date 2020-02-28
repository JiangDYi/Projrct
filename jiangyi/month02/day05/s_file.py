from socket import *

s=socket()

s.bind(("127.0.0.1",8999))

s.listen(6)

c,addr=s.accept()
print('连接到:',addr)

f=open('jj.jpg','wb')

while True:
    data=c.recv(1024)
    if data=="文件传输完毕".encode():
        break
    f.write(data)

f.close()
s.close()
c.close()
