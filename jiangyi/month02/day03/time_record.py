import time
f= open('file','a+')
f.seek(0,0)
n=1
for line in f:
   n+=1

while True:
    time.sleep(2)
    s="%d.  %s\n"%(n,time.ctime())
    f.write(s)
    f.flush()
    n+=1


f.close()