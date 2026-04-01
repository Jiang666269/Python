#Day6 dic

#1.统计单词出现次数
'''
word = {}
current = ""
text = "I love AI and AI love me "
for i in range(len(text)):
    if text[i] !=" ":
        current += text[i]
    else:
        if current not in word:
            word[current] = 1
            current = ""
        else:
            word[current] += 1
            current = ""
for item in word.items():
    print(f"{item[0]}: {item[1]}")
'''

#2.学生成绩
'''
student_score = {}
num = int(input("请输入学生数量:"))
highest_score = 0
for i in range(num):
    name = input("输入学生姓名:")
    score = float(input("输入学生分数:"))
    student_score[name] = score
    if score > highest_score:
        highest_score = score
        highest_name = name
print("最高分学生是:" + highest_name + "分数是:" + str(highest_score))
'''

#3.找重复元素
'''
nums = [1,2,2,3,3,3,4,1]
dict1 = {}
for num in nums:
    if num not in dict1:
        dict1[num] = 1
    else:
        dict1[num] += 1
for item in dict1.items():
    if item[1] > 1:
        print(f"{item[0]} 出现 {item[1]} 次")
'''

#4.反转字典
'''
d = {
    "a":1,
    "b":2,
    "c":3
}
new_d = {}
for k,v in d.items():
    new_d[v] = k
print(new_d)
'''

#5.统计字符频率
'''
text = "banana"
frequency = {}
for ch in text:
    if ch not in frequency:
        frequency[ch] = 1
    else:
        frequency[ch] += 1
print(frequency)
'''

#6.分组统计
'''
scores = [85, 90, 78, 92, 88, 76]
level = {"优秀":0,
         "良好":0,
         "及格":0}
for score in scores:
    if score >= 90:
        level["优秀"] +=1
    elif score >= 80:
        level["良好"] +=1
    else:
        level["及格"] +=1
print(level)
'''

#7.词频
'''
text = "I love AI and AI love AI"
word = {}
current = ""
most_fre = 0
for ch in text:
    if ch != " ":
        current +=ch
    else:
        if current not in word:
            word[current] = 1
            current = ""
        else:
            word[current] += 1
            current = ""
word[current] +=1
for item in word.items():
    if item[1] > most_fre:
        most_fre = item[1]
        most_word = item[0]
print(f"出现最多的单词是{most_word},出现了{most_fre}次")
'''