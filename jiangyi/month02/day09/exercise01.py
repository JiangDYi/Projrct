import os
from threading import Thread

old_dir=input("拷贝的目录名称：")

if old_dir[-1]=="/":
    old_dir=old_dir[:-1]
new_dir=old_dir+"-备份"

try:
    file_list=os.listdir(old_dir)
except:
    os._exit(0)

os.mkdir(new_dir)

def copy_file(file):
    fr=open(old_dir+'/'+file,'rb')
    fw=open(new_dir+'/'+file,'wb')
    while True:
        data=fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

jobs=[]
for file in file_list:
    t=Thread(target=copy_file,args=(file,))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()