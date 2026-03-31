#前三天学习成果检验
'''
import random
true_num=random.randint(1,100)
while True:
    n = int(input("输入一个正整数n(输入0退出):"))
    if n==0:
        break
    if n%2==0:
        print(f"{n}是偶数")
    else:
        print(f"{n}是奇数")
    print(f"{n}的因子有：", end="")
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ")
    print()
    is_prime = True
    if n > 1 :
        for j in range(2,n):
            if n % j ==0:
                is_prime=False
                print(f"{n}不是质数")
                break
            if is_prime:
                print(f"{n}是质数")
                break
    else:
        print(f"{n}不是质数")
    while True:
         m = int(input("猜一个数(0~100)："))
         if m==true_num:
             print("Bingo!")
             break
         elif m <true_num:
             print("smaller")
         else:
             print("bigger")
'''

#文本分析系统实现功能：1.去除多余空格 2.统计单词数量 3.找最长单词 4.统计每个单词出现的次数
'''
sentence = ""
word = ""
correct = []
appeared = []
max_num = 0
sentence += input("请输入一段英文句子（空格隔开）:")
for i in range(len(sentence)):
    if sentence[i] !=" ":
        word += sentence[i]
        pass
    else:
        if word !="":
            correct.append(word)
            word =""
correct.append(word)
for j in range(len(correct)):
    print(correct[j],end=" ")
print()
print(f"单词数量：{len(correct)}")
for j in range(len(correct)):
    count = len(correct[j])
    if count > max_num:
        max_word = correct[j]
        max_num = count
    current_word =""
print("最长的单词是：",max_word)
for m in range(len(correct)):
    if correct[m] not in appeared:
        appeared.append(correct[m])
        times = 0
        for n in range(len(correct)):
            if correct[m] == correct[n]:
                times +=1
        print(correct[m] + "出现了" + str(times))
'''

#文本压缩+分析系统 功能1.压缩字符串 2.找出现次数最多的字符 3.解压字符串 4.判断压缩是否有效、
'''
text = input("输入一句英文(不用隔开): ")
compressed = ""
max_char = ""
max_count = 0
i = 0
while i < len(text):
    current_char = text[i]
    count = 1
    while i + 1 < len(text) and text[i + 1] == current_char:
        count += 1
        i += 1
    compressed += current_char + str(count)
    if count > max_count:
        max_count = count
        max_char = current_char
    i += 1
print("压缩后：", compressed)
print(f"出现最多的字符是: {max_char}, 次数为: {max_count}")
decompressed = ""
i = 0
while i < len(compressed):
    ch = compressed[i]
    i += 1
    num_str = ""
    while i < len(compressed) and compressed[i].isdigit():
        num_str += compressed[i]
        i += 1
    decompressed += ch * int(num_str)
print("解压后：", decompressed)
if len(compressed) >= len(text):
    print("不值得压缩")
else:
    print("压缩有效")
'''