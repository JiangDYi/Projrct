f=open('file','wb+')

f.write("病毒大爆炸".encode())
f.flush()

f.seek(3,0)
f.write("病毒大爆炸".encode())
data=f.read()
print(data.decode())

f.close()