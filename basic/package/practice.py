#practice
goods = []
with open("goods.txt","r") as f:
    for line in f:
        name,price,count = line.strip().split()
        price = float(price)
        count = int(count)
        goods.append((name,price,count))
print(goods)