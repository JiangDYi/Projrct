from socket import *

import  struct
st=struct.Struct("i32sif")

sockfd=socket(AF_INET,SOCK_DGRAM)

server_addr=('127.0.0.1',9999)
sockfd.bind(server_addr)

f=open('student.txt','a')
while True:
    data,addr=sockfd.recvfrom(1024)
    info = st.unpack(data)
    if info[-1]>=90:
        id,name,age,score=info
        name=name.decode().strip('\x00')
        stu="%d %s %d %.2f\n"%(id,name,age,score)
        f.write(stu)
        f.flush()


s.close()