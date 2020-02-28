"""
chat room 服务端
env:python3
socket and fork exercise
"""

from socket import *
import os
#全局变量
ADDR=('0.0.0.0',9999)

#应用于存储用户{name：addr}
user={}

#处理进入聊天室请求
def do_login(s,name,addr):
    if name in user or "管理" in name:
        s.sendto(b'FAIL',addr)
        return
    else:
        s.sendto(b'OK',addr)
    #通知其他人进入
    msg="\n欢迎 '%s' 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name]=addr

#处理聊天功能
def do_chat(s,name,centent):
    msg="\n%s:%s"%(name,centent)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

#处理退出
def do_quit(s,name):
    msg="\n%s'退出聊天室'"%name
    for i in user:
        if i !=name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[i])

#基本结构（接受请求，分配请求任务）
def main():
    # udp服务端套接字
    s=socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    pid=os.fork()
    if pid<0:
        print("创建失败")
    elif pid==0:
        while True:
            content=input("超级管理员：")
            msg="lt %s %s"%("超级管理员",content)
            s.sendto(msg.encode(),ADDR)
    else:
        #循环接受请求
        while True:
            data,addr=s.recvfrom(1024)
            tmp=data.decode().split(' ',2)#对请求内容简单解析
            print('接收到请求：',tmp)
            if tmp[0]=='jr':
                do_login(s,tmp[1],addr)
            elif tmp[0]=='lt':
                do_chat(s,tmp[1],tmp[2])
            elif tmp[0]=='tc':
                do_quit(s,tmp[1])

if __name__ == '__main__':
    main()

