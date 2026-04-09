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
from typing import final

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

#学生成绩分析系统（综合)
'''
student = {}
level = {"优秀":0,
         "良好":0,
         "及格":0,
         "不及格":0 }
appeared_times = {}
max_students = []
max_score = 0
longest = 0
total_score = 0.0
student_num = int(input("请输入学生数量:"))
for i in range(student_num):
    name,score = input("请输入姓名和分数(空格隔开):").split()
    score = float(score)
    student[name] = score
print("所有学生信息：")
for item in student.items():
    print(f"{item[0]} {item[1]}")
    if item[1] > max_score:
        max_student = item[0]
        max_score = item[1]
max_students.append(max_student)
for item in student.items():
    if item[1] == max_score and item[0] not in max_students:
        max_students.append(item[0])
print("最高分学生:")
for i in range(len(max_students)):
    print(max_students[i] + " " + str(max_score) )

for item in student.items():
    if float(item[1]) >= 90:
        level["优秀"] += 1
    elif float(item[1]) >= 80:
        level["良好"] += 1
    elif float(item[1]) >= 60:
        level["及格"] += 1
    else:
        level["不及格"] += 1
print("成绩等级统计:")
for item in level.items():
    print(f"{item[0]}:{item[1]}")

for item in student.items():
    if item[1] not in appeared_times:
        appeared_times[item[1]] = 1
    else:
        appeared_times[item[1]] += 1
print("分数出现次数:")
for item in appeared_times.items():
    print(f"{item[0]} 出现了 {item[1]}次")

for item in student.items():
    if len(item[0]) > longest:
        longest = len(item[0])
        longest_student = item[0]
print(f"名字最长的学生： {longest_student}")

for score in student.items():
    total_score += score[1]
average_score = round(total_score / len(student.keys()),2)
print(f"平均分为 {average_score}")
'''

#电商订单计算器
#定义一个函数 用于根据传入的商品信息（名字，价格，数量），优惠，运费信息计算订单的总金额
#优惠卷规则：满3000才能用 且优惠卷总额不超过商品总价
#积分抵扣规则：满2000才能用 100积分=1元 只能整数抵扣 抵扣金额低于剩余金额
#会员折扣：会员9折（最后计算）
#运费规则：满5000 免运费 否则运费15
#返回值格式：（原始总价，优惠后价格，最终支付价格）
'''
def calculate_order(goods,coupon=0,points=0,is_vip=False):
    original_total = 0
    current_total = 0
    for name,price,count in goods:
        original_total += price * count
        current_total += price * count

    if coupon<=current_total and original_total>=3000:
        current_total -= coupon

    points_amount = points // 100
    if points_amount<=current_total and original_total>=2000:
        current_total -= points_amount
    final_total = current_total

    if is_vip:
        final_total = final_total * 0.9

    if final_total<5000:
        final_total = final_total+15
    price = (original_total,current_total,final_total)
    return price

goods = []
n = int(input("输入商品数量："))
for i in range(n):
    name,price,count = input("请输入商品名 价格 数量:").split()
    price = float(price)
    count = int(count)
    goods.append((name,price,count))
coupon = float(input("请输入优惠卷金额："))
points = int(input("请输入积分数量（整百）："))
is_vip = input("是否是vip，是的话请输入True：").lower()
if is_vip == "true":
    is_vip = True
price = calculate_order(goods,coupon,points,is_vip)
print(f"原价：{price[0]}")
print(f"优惠后：{price[1]}")
print(f"实际支付：{price[2]}")
'''
