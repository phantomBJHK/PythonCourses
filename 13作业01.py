class Info:
    name = 'James'
    def __init__(self,star,age):
        self.star = star
        self.age = age
    def run(self):
        print('我是%s星座，我%s岁。' % (self.star,self.age))

me = Info('狮子',46)
print(me.name)
me.run()