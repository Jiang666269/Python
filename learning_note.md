# **python学习笔记**
##  *Day3:for && while*
* 随机数:
导入random模块，random.randint(a,b),即返回a,b之间(包括a,b)的一个整数
```python
import random
num = random.randint(1,100)
print(num)
```
* print函数输出默认以"\n"结尾，可以通过end来更改
```python
print("Hello python",end=" ")
```
* while True 无限循环
* 判断质数 is_prime:引入布尔变量
```python
n = 7
is_prime=True
for i in range(1,10):
    if n % i ==0:
         is_prime=False
```
---
## *Day4:list*
* > 定义：列表名称[元素1,···,元素n]
* >切片：列表名称[start:end:step],***不包含end***
* >列表的常见方法：
1.增加append `s.append()` 2.指定索引之前插入insort `s.insort(a,b)` 3.移除第一个匹配值remove `s.remove()` 4.删除指定索引元素pop（未指定则为最后一个）`s.pop()` 5.排序sort（小->大） `s.sort()` 6.反转reverse `s.reverse()`
* >解包/组包：将容器解开成多个独立元素/将多个独立元素合并到一个容器
```python
a = [*b,*c] #a,b,c为列表,可用于合并列表
```
* 列表推导式：一定规则，快速形成
```python
#格式1[插入值 for i in 列表]
num = [i**2 for i in range(1,21)]
#格式2[插入值 for i in 列表 if 条件]
num =[i**2 for i in range(1,21) if i%2==0]
```
---
## *Day5:list&&str*
* > 特点：1.不可变性。 2.有序性。 3.可迭代性。
* > 常用方法：1.uper/lower()--将字符串中所有字母转为大/小写。2.split()--将字符串按指定分隔符分割成列表。