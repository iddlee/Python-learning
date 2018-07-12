'''
管理员：Admin
    属性：用户名，密码
    行为：登录
'''
import time
import sys
class Admin:


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def landUI(self):
        print("--------------------欢迎来到XX银行--------------------")
        username = input("请输入管理员账号")
        password = input("请输入管理员密码")
        if username == self.username and password == self.password:
            print("登陆成功，请稍后。。。")
            time.sleep(1)
        else:
            print("账号或密码错误，登录失败")
            sys.exit()