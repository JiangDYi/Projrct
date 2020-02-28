"""
TCP服务器流程；重点代码
"""

import socket

#创建tcp套接字对象
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#端口立即重启（在bind之前）
sockfd.setsockopt(socket.SOL_SOCKET,socket.SOCK_STREAM)

#绑定地址 ip：“localhost” “127.0.0.1” “0.0.0.0” “192.168. .”
sockfd.bind(("127.0.0.1",9998))

#设置监听套接字
sockfd.listen(6)

#处理客户端链接
while True:
    print("等待连接...")
    connfd,addr=sockfd.accept()
    print("链接到",addr)

    #收发消息（网络传输数据用字节穿）
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        #收到了b‘##’退出
        # if data==b"##":
        #     break
        print("收到了：",data.decode())
        n=connfd.send('谢谢'.encode())
        print("发送%d字节"%n)


    connfd.close()
# 关闭套接字
sockfd.close()