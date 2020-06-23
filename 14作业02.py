class Computer:
    def __init__(self, color, price):
        self.color = color
        self.price = price

class Notebook(Computer):
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        self.color = 'Red'
        self.price = 5000
        return '%s牌笔记本电脑，%s色，价格：%s元。' %(self.brand, self.color, self.price)

pc = Computer('Blue',7500)
pc1 = Notebook('联想')
print(pc1)
        