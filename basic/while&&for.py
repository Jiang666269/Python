#Day3 while && for

#1.猜数字
#固定数
'''
true_num = 36
while True:
    user_num = int(input("猜一个数:"))
    if user_num == true_num:
        print("Bingo!")
        break
    elif user_num > true_num:
        print("Bigger")
    else:
        print("Smaller")
'''
#随机数
'''
import random
true_num = random.randint(1,100)
while True:
    user_num = int(input("猜一个数:"))
    if user_num == true_num:
        print("Bingo!")
        break
    elif user_num > true_num:
        print("Bigger")
    else:
        print("Smaller")
'''

#2.求和
'''
total = 0
n = int(input("输入一个整数："))
for i in range(n+1):
    total += i
print(total)
'''

#3.打印九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {i*j}",end="  ")
    print("\t)
'''

#4.找第一个能被整除的数
'''
n = int(input("输入一个正整数:"))
for i in range(1,101):
    if i % n == 0:
        print(i)
        break
'''

#5.统计输入次数
'''
total = 0
count = 0
while True:
    n = int(input("输入一个数："))
    if n ==0:
        count +=1
        print(f"一共输入了{count}个数")
        print(f"总和为{total}")
        break
    else:
        count += 1
        total += n
'''
#6.打印图形
'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''