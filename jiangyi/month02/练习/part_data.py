

f=open('talk.txt','r')
f1=open('老王.txt','a')
f2=open('老李.txt','a')
f3=open('老张.txt','a')

for line in f:
     data=line.split(" ",2)
     if data[0]=="老王:":
         f1.write(line)
     elif data[0]=="老李:":
         f2.write(line)
     else:
         f3.write(line)

f.close()
f1.close()
f2.close()
f3.close()