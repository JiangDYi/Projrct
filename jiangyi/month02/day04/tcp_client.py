"""
tcp客户端：重点代码
"""

from socket import *

#服务器地址
server_addr=("127.0.0.1",9998)

#创建tcp套接字
sockfd=socket()#默认值就是tcp套接字

#连接服务器
sockfd.connect(server_addr)

#发送接收消息
while True:
    data=input(">>")
    sockfd.send(data.encode())
    if not data:
        break
    #输入##表示退出
    # if data=="##":
    #     break
    data=sockfd.recv(1024)
    print("接收到：",data.decode())


sockfd.close()