from manager import *
manager = Goodsmanager()
while True:
    print("\n==== 商品管理系统 ====")
    print("1.添加商品")
    print("2.查看商品")
    print("3.删除商品")
    print("4.修改商品")
    print("5.计算总价")
    print("6.最贵商品")
    print("0.退出")

    choice = input("请选择功能：")
    if choice == "1":
        n = int(input("要添加的商品数量："))
        for i in range(n):
            name,price,count = input("请输入商品名称 价格 数量：").split()
            manager.add_good(name,price,count)

    elif choice == "2":
        goods = manager.show_all()
        if len(goods) == 0:
            print("暂无商品")
        else:
            for good in goods:
                print(f"{good.name} {good.price} {good.count}")

    elif choice == "3":
        name = input("请输入要删除的商品名称：")
        good,success = manager.delete_good(name)
        if success:
            print("删除成功")
        else:
            print("商品不存在")
    elif choice == "4":
        try:
            name,price,count = input("输入商品名称 新价格 新数量：").split()
            new_price = float(price)
            new_count = int(count)
            goods,success = manager.update_good(name,new_price,new_count)
            if success:
                print("更新成功")
            else:
                print("商品不存在")
        except:
            print("输入错误")
    elif choice == "5":
        total = manager.total_price()
        print(f"总价为：{total}")
    elif choice == "6":
        result = manager.get_max_good()
        if result:
            good,price = result
            print(f"最贵商品：{good.name}，价格：{good.price}")
        else:
            print("暂无商品")
    elif choice == "0":
        print("成功退出系统")
        break
    else:
        print("无效操作，请重新输入：")
