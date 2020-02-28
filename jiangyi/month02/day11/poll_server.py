"""
poll方法
"""
from socket import *
from select import *

s=socket()
s.bind(('0.0.0.0',11111))
s.listen(3)

#关注s
p=poll()
p.register(s,POLLIN)

#建立查找字典  时刻与register保持一致
fdmap={s.fileno():s}

#提交监控
while True:
    print("等待IO发生...")
    events=p.poll()
    for fd,event in events:
        if fd ==s.fileno():
            c,addr=fdmap[fd].accept()
            print("connet from",addr)
            #关注新的套接字对象
            c.setblocking(False)
            p.register(c,POLLIN|POLLERR)
            fdmap[c.fileno()]=c#维护字典，与register保持一致
        elif event & POLLIN:
            #有客户端发送消息
            data=fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)#取消关注
                fdmap[fd].close()
                del fdmap[fd]#从字典中删除
                continue
            print(data)
            fdmap[fd].send(b'OK')

