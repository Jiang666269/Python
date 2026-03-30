#Day6 list&&str

#1.统计字符出现次数
'''
text = "banana"
appeared = []
for letter in text:
    if letter not in appeared:
        count = 0
        for ch in text:
            if letter ==ch:
                count += 1
        print(f"{letter} 出现 {count}次")
        appeared.append(letter
'''
from ctypes.wintypes import PWORD

#2.找最长单词
'''
text = "I love artificial intelligence"
appeared = text.split(' ')
max = len(appeared[0])
m = 0
for i in range(4):
    if len(appeared[i]) >= max:
        max = len(appeared[i])
        m = i
print(f"最长单词是: {appeared[m]}")
'''

#3.字符串反转（不能用切片）
'''
text = "hello"
rev = []
for i in range(len(text)-1,-1,-1):
    rev.append(text[i])
result = "".join(rev)
print(result)
'''

#4.删除字符串中所有空格
'''
text = "a b c d e"
result =""
for i in range(len(text)):
    if text[i] != " ":
        result += text[i]
print(result)
'''

#5.列表中字符串统一格式化
'''
names = ["tom", "JACK", "aLiCe"] #要求首字母大写，其余小写
result = []
for name in names:
    first = name[0].upper()
    rest = ""
    for ch in name[1:]:
        rest += ch.lower()
    result.append(first + rest)
print(result)
'''

#6.模拟split
'''
text = "I-love-python"
result = []
word =""
for i in range(len(text)):
    if text[i] != "-":
        word +=text[i]
    else:
        result.append(word)
        word = ""
        pass
result.append(word)
print(result)
'''

#7.判断回文
'''
text =""
text +=input("请输入文字：")
is_rev = True
for i in range(len(text)//2):
    if text[i] != text[len(text)-i-1]:
        is_rev = False
        print(f"{text}不是回文")
        break
if is_rev:
    print(f"{text}是回文")
'''
