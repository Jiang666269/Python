from utils import *
goods = []
n = int(input("请输入商品类别数："))
while n > 0:
    name,price,count = input("请输入商品名称 价格 数量：").split()
    if not is_number(price) or not is_number(count):
        print("价格/数量应为阿拉伯数字，请重新输入:")
    elif float(count) % 1 != 0.0:
        print("数量应为整数，请重新输入：")
    else:
        price = float(price)
        count = int(count)
        goods.append((name,price,count))
        n -= 1
save_goods(goods)
print(f"您的购物车信息为：{load_goods()}")
print(f"总价为：{calculate_total(goods)}元")
print(f"最贵单品及其价格为{get_max_price(goods)}")
