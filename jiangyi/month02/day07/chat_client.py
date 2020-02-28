"""
chat room 客户端
发送请求 得到结果
"""

from socket import *
import os,sys


#服务器地址
ADDR=('127.0.0.1',9999)

#发送消息
def send_msg(s,name):
    while True:
        try:
            content=input("发言：")
        except:
            content='quit'
        if content=='quit':
            msg="tc "+name
            s.sendto(msg.encode(),ADDR)
            sys.exit("谢谢使用")
        msg="lt %s %s"%(name,content)#根据协议组织消息
        s.sendto(msg.encode(),ADDR)
#接收消息
def recv_msg(s):
    while True:
        data,addr=s.recvfrom(1024)
        if data.decode()=="EXIT":
            sys.exit()
        print(data.decode()+'\n发言：',end="")

#启动函数--> 向服务端发送初始请求
def main():
    #udp客户端
    s=socket(AF_INET,SOCK_DGRAM)
    while True:
        name=input("请输入姓名：")
        msg="jr "+name
        s.sendto(msg.encode(),ADDR)#发送请求
        data,addr=s.recvfrom(1024)#等待反馈结果
        if data.decode()=="OK":
            print("你进入聊天室.")
            break
        else:
            print("该用户名已存在.")

    #创建父子进程
    pid = os.fork()
    if pid < 0:
        print("创建失败")
        return
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)



if __name__ == '__main__':
    main()