import re

s="""Hello
重庆
"""
#只匹配ascii
# regex=re.compile(r"\w+",flags=re.A)

#让.匹配换行
# regex=re.compile(r".+",flags=re.S)

#忽略字母大小写
regex=re.compile(r"[a-z]+",flags=re.I)

l=regex.findall(s)
print(l)