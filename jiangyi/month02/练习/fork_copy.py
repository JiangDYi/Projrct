import os

size=os.path.getsize('j.jpg')

def up_part():
    f1=open('j.jpg','rb')
    f2=open('jj.jpg','ab')
    f2.write(f1.read(size//2))
    f1.close()
    f2.close()

def down_part():
    f1=open('j.jpg','rb')
    f2=open('jj.jpg','ab')
    f1.seek(size//2,0)
    f2.write(f1.read())
    f1.close()
    f2.close()

def main():
    pid=os.fork()
    if pid<0:
        print("创建失败")
    elif pid==0:
        up_part()
    else:
        down_part()

if __name__ == '__main__':
    main()
