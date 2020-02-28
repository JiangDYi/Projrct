

import re

pattern=r"(ab)cd(?P<dog>ef)"

regex=re.compile(pattern)

obj=regex.search("abcdefjhi")

print(obj.span()) #匹配到的内容在目标字符串中的位置s[o:6]z
print(obj.groupdict())

print(obj.group())
print(obj.group(1))
print(obj.group('dog'))