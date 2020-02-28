from socket import *
import os,sys

ADDR=('127.0.0.1',11111)

s=socket(AF_INET,SOCK_DGRAM)

def send_msg(s,name):
    while True:
        try:
            content=input(">>:")
        except:
            content='quit'

        if content=='quit':
            msg="tc "+content
            s.sendto(msg.encode(),ADDR)
            sys.exit("谢谢使用")
        msg="lt %s %s"%(name,content)
        s.sendto(msg.encode(),ADDR)

def recv_msg(s):
    while True:
        data,addr=s.recvfrom(1024)
        if data.decode()=="EXIT":
            sys.exit()
        print(data.decode()+"\n>>：",end="")

def main():
    while True:
        name=input("请输入名字:")
        msg="jr "+name
        s.sendto(msg.encode(),ADDR)
        data,addr=s.recvfrom(1024)
        if data.decode()=="OK":
            print("你已进入聊天室")
            break
        else:
            print("名字已存在请重新输入")


    pid=os.fork()
    if pid<0:
        print("创建失败")
    elif pid==0:
        send_msg(s,name)
    else :
        recv_msg(s)



if __name__ == '__main__':
    main()