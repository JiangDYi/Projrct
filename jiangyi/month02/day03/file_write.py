f=open('file','a')

# f.write(b"hello,bitch\n")
# f.write("滚\n".encode())
l=['baby\n','想你了\n']
f.writelines(l)

f.close()