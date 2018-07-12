class Person:


    def __init__(self, name, age, sex, item):
        self.name = name
        self.age = age
        self.sex = sex
        self.item = item

    def play(self):
        print("%s爱玩%s" % (self.name, self.item))

    def show(self):
        print("姓名：%s  年龄：%s  性别：%s" % (self.name, self.age, self.sex))