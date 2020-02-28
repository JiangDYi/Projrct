
def seek_word(word):
    f=open('dict.txt','r')

    for lien in f:
        w=lien.split(' ')[0]
        if w>word.decode():
            f.close()
            return "没有找到该单词"

        elif w==word.decode():
            f.close()
            return lien

    else:
        f.close()
        return "没有找到该单词"


from socket import *
# 创建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 绑定地址
server_addr = ('127.0.0.1', 9999)
sockfd.bind(server_addr)
# 循环收发数据

while True:
    data, addr = sockfd.recvfrom(1024)
    print("收到", addr, "消息：", data.decode())
    result=seek_word(data)
    sockfd.sendto(result.encode(),addr)

sockfd.close()