from socket import *
import os

ADDR=('0.0.0.0',11111)

user={}


def do_login(s,name,addr):
    if name in user or "管理" in name:
        s.sendto(b"FAIL",addr)
    else:
        s.sendto(b"OK",addr)

    msg="\n欢迎 %s 加入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name]=addr

def do_chat(s,name,content):
    msg="\n %s: %s"%(name,content)
    for i in user:
        if i != name :
            s.sendto(msg.encode(),user[i])

def do_quit(s,name):
    msg="\n %s 退出聊天室"%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b"EXIT",user[i])

    del user[name]

def main():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid=os.fork()
    if pid<0:
        print("创建失败")

    elif pid==0:
        while True:
            content=input("管理员消息：")
            msg="lt %s %s "%("管理员消息",content)
            s.sendto(msg.encode(),ADDR)
    else:
        while True:
            data,addr=s.recvfrom(1024)
            tmp=data.decode().split(" ",2)
            if tmp[0]=='jr':
                do_login(s,tmp[1],addr)
            elif tmp[0]=='lt':
                do_chat(s,tmp[1],tmp[2])
            elif tmp[0]=='tc':
                do_quit(s,tmp[1])



if __name__ == '__main__':
    main()