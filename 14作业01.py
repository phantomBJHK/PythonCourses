class Amateur:
    def __init__(self, name, major, age, sex):
        self.name = name
        self.major = major #专业
        self.age = 年龄
        self.sex = sex

class CN_Amateur(Amateur):
    country = '中国'
    def __init__(self, name, major, age, sex, hometown):
        self.name = name
        self.major = major #专业
        self.age = age
        self.sex = sex
        self.hometown = hometown
    def info(self):
        print('姓名：%s，%s运动员, 年龄：%s, 性别：%s，来自：%s%s' %(self.name,self.major,self.age,self.sex,self.country,self.hometown))
sportsman = CN_Amateur('张三','乒乓球',23,'男','河北')
sportsman.info()