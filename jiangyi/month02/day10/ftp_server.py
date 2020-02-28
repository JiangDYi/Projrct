"""
FTP文件处理
多线程并发和套接字联系
"""
from socket import *
from threading import Thread
import os,time

# 全局变量
HOST = '0.0.0.0'
PORT = 11111
ADDR = (HOST, PORT)

#文件库
FTP="/home/traena/FTP/"

#处理客户端请求
class FTPServer(Thread):
    def __init__(self, connfd):
        self.connfd=connfd
        super().__init__()

    #处理文件列表
    def list(self):
        file_list=os.listdir(FTP)
        #判断文件夹是否为空
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        #发送文件列表
        data='\n'.join(file_list)#将文件以\n拼接
        self.connfd.send(data.encode())

    #处理下载文件
    def get(self,filename):
        try:
            f=open(FTP+filename,'rb')
        except:
            #不存在这个文件
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        #发送文件
        while True:
            data = f.read(1024)
            if not data:
                self.connfd.send(b'##')#结束标志
                break
            self.connfd.send(data)
        f.close()

    #处理上传文件
    def put(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        #循环接收文件写入本地
        f=open(FTP+filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            #文件接收完毕的标志
            if data == b'##':
                break
            f.write(data)
        f.close()

    #循环接收请求，分发任务
    def run(self):
       while True:
           data=self.connfd.recv(1024).decode()#循环接收请求
           if not data or data=='E':
               return #run函数结束对应线程即退出
           elif data=='L':
               self.list()
           elif data[0]=='G':
               filename=data.split(' ')[-1]
               self.get(filename)
           elif data[0] == 'P':
               filename = data.split(' ')[-1]
               self.put(filename)

#框架机构，启动函数
def main():
    # 创建监听套接字
    s = socket()
    s.bind(ADDR)
    s.listen(3)

    print("listen the prot 11111")

    while True:
        c, addr = s.accept()
        print("connect from", addr)

        # 创建线程处理客户端请求
        t = FTPServer(c)
        t.setDaemon(True)#分支线程随主线程退出
        t.start()

    s.close()

if __name__ == '__main__':
    main()