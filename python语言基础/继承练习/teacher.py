from 父类 import Person
class Teacher(Person):


    def __init__(self, name, age, sex, item, workage):
        Person.__init__(self, name, age, sex, item)
        self.workage = workage

    def teach(self):
        print("我承诺，我会认真教课")

    def show(self):
        print("姓名：%s  年龄：%d  性别：%s  工龄：%d" % (self.name, self.age, self.sex, self.workage))