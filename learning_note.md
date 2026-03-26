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
