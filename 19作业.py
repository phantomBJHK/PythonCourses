class Grade():
    def __init__(self, grades):
        self.grades = str(grades)
        self.grades_name = '年级'

    def __str__(self):
        return self.grades


class Banji():
    def __init__(self, banji):
        self.banji = str(banji)
        self.banji_name = '班级'

    def __str__(self):
        return self.banji


class Teacher(Grade, Banji):
    def __init__(self, name, subject, grades_name, banji_name):
        Grade.__init__(self, grades_name)
        Banji.__init__(self, banji_name)
        self.name = name
        self.subject = subject

    def run(self):
        print('我是老师%s，%s年级,%d班的%s老师。' %
              (self.name, self.grades, int(self.banji), self.subject))


class Student(Grade, Banji):
    def __init__(self, name, age, grades_name, banji_name):
        Grade.__init__(self, grades_name)
        Banji.__init__(self, banji_name)
        self.name = name
        self.age = age

    def run(self):
        print('我是%s，%s年级%s班的学生，今年%s岁。' %
              (self.name, self.grades, self.banji, self.age))


grade = Grade('2')
print('年级', grade)
banji = Banji('3')
print('班级', banji)
tea = Teacher('name', 'sub', grade, banji)
tea.run()
stu = Student('小张', 19, grade, banji)
stu.run()
