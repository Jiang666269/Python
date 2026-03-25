#Day 1
# name = "Knife"
# age = "18"
# print(f"My name is {name},I am {age} years old.")
# print("My name is %s ,I am %s years old"%(name,age))
#
# a = 10
# b = 3.14
# c = "hello"
# print(type(a),type(b),type(c))
#
# a = "hello"
# b = "world"
# print(a + " " + b)
#
# a,b = input("Enter two numbers separated by a comma").split()
# a = int(a)
# b = int(b)
# print(a+b)
# print(a*b)
#
# a = 20
# b = 10
# c = a
# a = b
# b = c
# print(a,b)
#
# a = input("姓名：")
# b = input("年龄：")
# c = input("身高：")
# print(f"====个人信息====\n姓名:{a}\n年龄:{b}\n身高：{c}")
#
# a = "10"
# b = 5
# print(a + str(b))
# print(int(a) + b)

#Day 2
# # a,b=input("Enter two numbers separeted by a comma:").split()
# # a,b=int(a),int(b)
# # if a>0 and b>0 :
# #     print("两个数都是正数")
# # elif a>0 or b>0:
# #     print("至少一个是正数")
# # else:
# #     print("都不是正数")
#
# # score=int(input("输入一个分数："))
# # if score>=60:
# #     if score>=90:
# #         print("优秀")
# #     else:
# #         print("及格")
# # else:
# #     print("不及格")
#
# # month = int(input("输入一个月份:"))
# # if month in [12,1,2]:
# #     print("冬")
# # elif month in [3,4,5]:
# #     print("春")
# # elif month in [6,7,8]:
# #     print("夏")
# # else:
# #     print("秋")
#
# # age = int(input("输入年龄："))
# # if 0< age <=12:
# #     print("儿童")
# # elif 13<= age <=19:
# #     print("青少年")
# # elif 20<= age <=59:
# #     print("成人")
# # else:
# #     print("老年")
#
# a,b,c = input("输入三个数 用空格间隔：").split()
# a,b,c=int(a),int(b),int(c)
# if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a :
#     print("输入错误")
# elif a==b or a==c or b==c:
#     if a==b and b==c:
#         print("等边")
#     else:
#         print("等腰")
# else:
#     print("普通")