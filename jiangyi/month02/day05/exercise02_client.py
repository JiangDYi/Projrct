from socket import *

import  struct
st = struct.Struct("i32sif")

ADDR=('127.0.0.1',9999)

sockfd=socket(AF_INET,SOCK_DGRAM)

while True:
    print("------------------------------------------")
    id=int(input("请输入学号："))
    name=input("请输入姓名：").encode()
    age=int(input("请输入年龄："))
    score=float(input("请输入成绩："))

    data=st.pack(id,name,age,score)
    sockfd.sendto(data,ADDR)


sockfd.close()

