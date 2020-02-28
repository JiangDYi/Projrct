word=input("请输入一个单词：")

f=open('dict.txt','r')

for lien in f:
    w=lien.split(' ')[0]
    if w>word:
        print("没有找到该单词")
        break
    elif w==word:
        print(lien)
        break
else:
    print("没有找到该单词")

f.close()