class Info:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_name(self):
        print('姓名：%s' % (self.name))
    
    def print_age(self):
        print('年龄：%s' % (self.age))
    

me = Info('张三丰',46)
me.print_name()
me.print_age()