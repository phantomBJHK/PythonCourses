class Maleguests:
    def __init__(self, name, age, city):
        print('各位女嘉宾好！')
        self.name = name
        self.age = age
        self.city = city
    def intro(self):
        print('我是%s，今年%s岁，来自%s' %(self.name, self.age, self.city))

guest1 = Maleguests('张三', 29, '南京')
guest1.intro()
