"""
file_open.py
文件打开方式
"""
#打开文件
# f=open('file','w') #读  文件必须存在

# f=open('file','r') #写  文件不存在创建，存在清空

f=open('file', 'a')  #写  文仔不存在创建，存在则追加


print(f)


f.close()