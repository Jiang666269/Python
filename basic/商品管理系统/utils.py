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

#添加商品
def add_good(goods,name,price,count):
    price = float(price)
    count = int(count)
    goods.append((name,price,count))
    return goods

#删除商品
def delete_good(goods,target_name):
    for i in range(len(goods)):
        name,price,count = goods[i]
        if name == target_name:
            goods.pop(i)
            return goods,True
    return goods,False

#更新商品
def update_good(goods,target_name,new_price,new_count):
    new_price = float(new_price)
    new_count = int(new_count)
    for i in range(len(goods)):
        name,price,count = goods[i]
        if name == target_name:
            goods[i] = (name,price,count)
            return goods,True
    return goods,False