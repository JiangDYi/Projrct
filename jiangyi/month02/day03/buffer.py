f=open('file','w')

while True:
    data=input(">>")
    if not data:
        break
    f.write(data+'\n')
    f.flush()

f.close()