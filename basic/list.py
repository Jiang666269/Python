#Day5 list

#1.找最大和次大值(不能用sort)
'''
nums = [3, 7, 2, 9, 5]
max = nums[0]
sec_max = nums[0]
for num in nums:
    if num > max:
        sec_max,max =max,num
    elif num > sec_max and num != max:
        sec_max = num
print("最大值为:",max)
print("次大值为:",sec_max)
'''

#2.列表去重(list+for,不能用set)
'''
nums = [1, 2, 2, 3, 4, 4, 5]
new_nums = []
for num in nums:
    if num not in new_nums:
        new_nums.append(num)
print(new_nums)
'''

#3.统计出现次数(不能用dict)
'''
nums = [1, 2, 2, 3, 3, 3, 4]
appeared = []
for n in nums:
    if n not in appeared:
        count = 0
        appeared.append(n)
        for m in nums:
            if m == n:
                count +=1
    else:
        continue
    print(f"{n}出现了{count}次")
'''

#4.列表反转(不能用reverse)
'''
nums = [1, 2, 3, 4, 5]
reversed_nums = []
for i in range(len(nums)):
    reversed_nums.append(nums[len(nums)-i-1]))
print(reversed_nums)
'''

#5.筛选+构造新列表
'''
nums = [1, 2, 3, 4, 5, 6]
new_nums=[i for i in nums if i%2==0]
print(new_nums)
'''

#6.找连续最大子列表长度
'''
nums = [1, 1, 2, 2, 2, 3, 3, 3, 3]
max_count = 1
current_count = 1
max_num = nums[0]
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
            max_num = nums[i]
    else:
        current_count = 1
print(f"最大连续相同数字是{max_num},出现了{max_count}次")
'''