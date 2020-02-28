"""
文件读写
"""


f=open('file','r')

# data=f.read(2)
# print(data)
#循环读取
# while True:
#     data=f.read(10)
#     if not data:
#     if data=='':
#         break
#     print(data)

# data=f.readline(20)
# print(data)
# data=f.readline(1)
# print(data)
data=f.readlines(1)
print(data)
# for line in f:
#     print(line)

f.close()