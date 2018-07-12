from 父类 import Person

class Student(Person):


    def __init__(self, name, age, sex, item, id):
        Person.__init__(self, name, age, sex, item)
        self.id = id

    def study(self):
        print("我承诺，我会好好学习")

    def show(self):
        print("姓名：%s  年龄：%d  性别：%s  学号：%s" % (self.name, self.age, self.sex, self.id))