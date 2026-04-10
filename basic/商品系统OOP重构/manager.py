from good import Goods
class Goodsmanager:
    def __init__(self):
        self.goods_list = []

    def add_good(self,name,price,count):
        good = Goods(name,price,count)
        self.goods_list.append(good)
        return self.goods_list

    def delete_good(self,name):
        for good in self.goods_list:
            if good.name == name:
                self.goods_list.remove(good)
                return self.goods_list,True
            else:
                return self.goods_list,False
    def update_good(self,name,new_price,new_count):
        for good in self.goods_list:
            if good.name == name:
                good.price = float(new_price)
                good.count = int(new_count)
                return self.goods_list,True
            else:
                return self.goods_list,False
    def show_all(self):
        return self.goods_list

    def total_price(self):
        total = 0
        for good in self.goods_list:
            total += good.total()
        return total

    def get_max_good(self):
        max_price = 0
        for good in self.goods_list:
            if good.price > max_price:
                max_price = good.price
                max_good = good
        return max_good,max_good.price

