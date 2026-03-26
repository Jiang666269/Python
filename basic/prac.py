#前三天学习成果检验
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

