from utils import *
good = load_goods()
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
        try:
            name,price,count = input("请输入商品名称 价格 数量：").split()
            goods = add_good(goods,name,price,count)
            save_goods(goods)
            print("添加成功！")
        except:
            print("输入错误！")
    elif choice == "2":
        goods = load_goods()
        for name,price,count in goods:
            print(name,price,count)
    elif choice == "3":
        name = input("请输入要删除的商品名称：")
        good,success = delete_good(goods,name)
        if success:
            save_goods(good)
            print("删除成功")
        else:
            print("商品不存在")
    elif choice == "4":
        try:
            name,price,count = input("输入商品名称 新价格 新数量").split()
            goods,success = update_good(goods,name,price,count)
            if success:
                save_goods(goods)
                print("更新成功")
            else:
                print("商品不存在")
        except:
            print("输入错误")
    elif choice == "5":
        total = calculate_total(goods)
        print(f"总价为:{total}")
    elif choice == "6":
        result = get_max_price(goods)
        if result:
            name,price = result
            print(f"最贵商品{name}，价格{price}")
        else:
            print("没有商品")
    elif choice == "0":
        print("成功退出系统")
        break