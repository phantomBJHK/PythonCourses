class Master:
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print('【古法】按照<%s>制作了一份煎饼果子...' % self.kongfu)

class School:
    def __init__(self):
        self.kongfu = '现代煎饼果子配方'

    def make_cake(self):
        print('【现代】按照<%s>制作了一份煎饼果子...' % self.kongfu)

class Apprentice(Master, School):
    def __init__(self):
        self.kongfu = '独创的煎饼果子配方'

    def make_cake(self):
        self.__init__()
        print('【独创】按照<%s>制作了一份煎饼果子...' % self.kongfu)

    def make_cake_old(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_cake_new(self):
        School.__init__(self)
        School.make_cake(self)

    

zhangsan = Apprentice()
zhangsan.make_cake()
zhangsan.make_cake_new()
zhangsan.make_cake_old()



    

