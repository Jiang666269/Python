#Day 7 函数
#学生系统函数化重构
'''
def get_students():
    students = {}
    student_num = int(input("请输入学生人数："))
    for i in range(student_num):
        name,score = input("请输入学生姓名和分数并用空格隔开：").split()
        score = float(score)
        students[name] = score
    return students

def print_students(students):
    for name,score in students.items():
        print(f"{name}: {score}")

def get_top_students(students):
    top_score = 0
    top_students = []
    for score in students.values():
        if score >top_score:
            top_score = score
    for item in students.items():
        if item[1] == top_score:
            top_students.append(item[0])
    return top_students,top_score

def get_level_count(students):
    level = {
        "优秀":0,
        "良好":0,
        "及格":0,
        "不及格":0}
    for score in students.values():
        if score >=90:
            level["优秀"] +=1
        elif score >=80:
            level["良好"] +=1
        elif score >=60:
            level["及格"] +=1
        else:
            level["不及格"] +=1
    return level

def count_scores(students):
    count = {}
    for score in students.values():
        if score not in count:
            count[score] = 1
        else:
            count[score] += 1
    return count

def get_longest_name(students):
    longest_name = ""
    longest = 0
    for name in students.keys():
        if len(name) > longest:
            longest = len(name)
            longest_name = name
    return longest_name

def get_average_score(students):
    total_score = 0
    for score in students.values():
        total_score += score
    average_score = round(total_score/len(students),2)
    return average_score
'''


#Day 8 function进阶

#6 *args
def max_num(*nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

#8 递归
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#9 综合
def process_scores(*scores):
    max_value = 0
    total_score = 0
    average_score = 0
    exceed_average = []
    for score in scores:
        total_score +=score
        if score> max_value:
            max_value = score
    average_score = round(total_score/len(scores),2)
    for score in scores:
        if score > average_score:
            exceed_average.append(score)
    return (max_value,average_score,exceed_average)

#10 终极(不用全局变量)
def counter():
    count = 0
    def inner():
        nonlocal count #nonlocal 修改外层变量
        count += 1
        return count
    return inner
c = counter()
print(c())
print(c())
print(c())