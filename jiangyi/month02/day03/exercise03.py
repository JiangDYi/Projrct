import time

f = open('file','a+') # 确保每次启动继续写

# 先判断有多少行
f.seek(0,0) #　把文件偏移量移动到开头
n = 1   # 应该等于　行数+1
for line in f:
    n += 1

# noinspection PyInterpreter
while True:
    time.sleep(2)  # 2s间隔
    s = "%d.  %s\n"%(n,time.ctime())
    f.write(s)
    f.flush()
    n += 1