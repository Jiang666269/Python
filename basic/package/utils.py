#判断是否是数字
def is_number(price):
    try:
        float(price)
        return True
    except ValueError:
        return False
#写
def save_goods(goods):
    with open("data.txt","w") as f:
        for name,price,count in goods:
            f.write(f"{name} {price} {count}\n")

#读
def load_goods():
    with open("data.txt","r") as f:
        goods = []
        for line in f:
            name,price,count = line.strip().split()
            goods.append((name,float(price),int(count)))
    return goods

#计算总价
def calculate_total(goods):
    total = 0
    for name,price,count in goods:
        total += price * count
    return total

#找最贵商品
def get_max_price(goods):
    max_price = 0
    for name,price,count in goods:
        if price > max_price:
            max_price = price
            max_good = name
    return max_good,max_price