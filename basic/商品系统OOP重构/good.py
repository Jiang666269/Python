class Goods:
    def __init__(self,name,price,count):
        self.name = name
        self.price = float(price)
        self.count = int(count)
    def total(self):
        return self.price * self.count
