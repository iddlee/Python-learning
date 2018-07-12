'''
用户在注册账号的时候我们需要输入用户信息，
创建一个用户类，变量有：用户名、密码、性别。
要求：用户名必须以字母开头，密码必须是6位以上，性别只能是男和女。
写一个show方法打印用户名、密码、性别的信息。
在主函数中创建一个用户对象，给三个变量赋值，如果赋值不满足要求则重新输入。
否则调用show方法输出信息即可
'''

class User:
    def __init__(self, name, password, sex):
        self.name = name
        self.password = password
        self.sex = sex
    def show(self):
        print("输入的信息如下：")
        print("用户名：%s   密码：%s   性别：%s" % (self.name, self.password, self.sex))

