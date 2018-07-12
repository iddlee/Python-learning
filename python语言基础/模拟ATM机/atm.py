'''
ATM：
    属性：用户列表（存储所有开卡人的信息）
    行为：开户，查询，存款，取款，转账，改密，锁定，解锁，销户，退出
'''
import random
import sys
from card import Card
from user import User
import time
class Atm:


    def  __init__(self):
        self.user_dic = {}

    def printOptionUI(self):
        print("*****************************************")
        print("*      开户（1）         查询（2）      *")
        print("*      存款（3）         取款（4）      *")
        print("*      转账（5）         改密（6）      *")
        print("*      锁定（7）         解锁（8）      *")
        print("*      销户（9）         退出（T）      *")
        print("*****************************************")

    def creatUser(self):  # 开户
        name = input("请输入姓名：")
        id = input("请输入身份证号：")
        phonenum = input("请输入手机号")
        passWord = input("请输入密码：")
        passWord2 = input("请再输入一遍密码：")
        if passWord != passWord2:
            print("两次输入密码不一致！开户失败")
            return False
        money = int(input("请输入存款金额，不得低于10："))
        if money < 10:
            print("存款不足10元，开户失败")
            return False
        # 证明前面输入的信息都没有问题，可以开户
        # 随机一个卡号（6）
        cardNum = random.randint(10000000, 99999999)
        # 创建卡对象
        card = Card(cardNum, passWord, money)
        # 创建用户对象
        user = User(name, phonenum, id, card)
        self.user_dic[cardNum] = user
        print("开户成功，卡号是：%d，余额为%d" % (cardNum, money))
        print(self.user_dic)

    def serach(self):  # 查询
        cardnum2 = int(input("请输入您要查询的卡号："))
        user = self.user_dic.get(cardnum2)
        if user == None:
            # if cardnum2 != user.card.cardNum:
            print("此卡未开户")
            return False
        if user.card.isLock == True:
            print("您的卡已被锁定，查询失败。。。请解锁")
            return False
        for i in range(3):
            passWord2 = input("请输入密码")
            if passWord2 != user.card.passWord:
                print("您的密码输入错误")
                print("剩余%d次机会" % (2 - i))
            else:
                break
        else:
            print("3次机会用尽，卡已被锁定")
            user.card.isLock = True
            return False
        print("您的账户余额为%.2f" % user.card.yu)

    def save(self):  # 存款
        cardnum2 = int(input("请输入您的卡号："))
        user = self.user_dic.get(cardnum2)
        if cardnum2 != user.card.cardNum:
        # if user == None
            print("此卡未开户")
            return False
        if user.card.isLock == True:
            print("您的卡已被锁定，存款失败。。。请解锁")
            return False
        for i in range(3):
            passWord2 = input("请输入密码")
            if passWord2 != user.card.passWord:
                print("您的密码输入错误")
                print("剩余%d次机会" % (2 - i))
            else:
                break
        else:
            print("3次机会用尽，卡已被锁定")
            user.card.isLock = True
            return False
        money = int(input("请输入你要存款的金额："))
        user.card.yu += money
        print("存款成功，您的余额为%.2f" % user.card.yu)
        return False

    def take(self):  # 取款
        cardnum2 = int(input("请输入您的卡号："))
        user = self.user_dic.get(cardnum2)
        if cardnum2 != user.card.cardNum:
            # if user == None
            print("此卡未开户")
            return False
        if user.card.isLock == True:
            print("您的卡已被锁定，取款失败。。。请解锁")
            return False
        for i in range(3):
            passWord2 = input("请输入密码")
            if passWord2 != user.card.passWord:
                print("您的密码输入错误")
                print("剩余%d次机会" % (2 - i))
            else:
                break
        else:
            print("3次机会用尽，卡已被锁定")
            user.card.isLock = True
            return False
        money = int(input("请输入你要取款的金额："))
        user.card.yu -= money
        if user.card.yu >= 0:
            print("取款成功，您的余额为%.2f" % user.card.yu)
        else:
            print("余额不足，取款失败")
            return False

    def transfer(self):  # 转账
        cardnum2 = int(input("请输入您的卡号："))
        user = self.user_dic.get(cardnum2)
        # if cardnum2 != user.card.cardNum:
        if user == None:
            print("此卡未开户")
            return False
        if user.card.isLock == True:
            print("您的卡已被锁定，转账失败。。。请解锁")
            return False
        for i in range(3):
            passWord2 = input("请输入密码")
            if passWord2 != user.card.passWord:
                print("您的密码输入错误")
                print("剩余%d次机会" % (2 - i))
            else:
                break
        else:
            print("3次机会用尽，卡已被锁定")
            user.card.isLock = True
            return False
        cardnum3 = int(input("请输入您要转账的卡号："))
        user1 = self.user_dic.get(cardnum3)
        if user == None:
            print("此卡未开户")
            return False
        money = int(input("请输入转账金额："))
        if user.card.yu >= 0:
            user.card.yu -= money
            user1.card.yu += money
            print("转账成功，您的余额为%.2f" % user.card.yu)
        else:
            print("余额不足，转账失败")
        return False

    def change(self):  # 改密
        cardnum2 = int(input("请输入您的卡号："))
        user = self.user_dic.get(cardnum2)
        if user == None:
            # if cardnum2 != user.card.cardNum:
            print("此卡未开户")
            return False
        if user.card.isLock == True:
            print("您的卡已被锁定，改密失败。。。请解锁")
            return False
        for i in range(3):
            passWord2 = input("请输入密码")
            if passWord2 != user.card.passWord:
                print("您的密码输入错误")
                print("剩余%d次机会" % (2 - i))
            else:
                break
        else:
            print("3次机会用尽，卡已被锁定")
            user.card.isLock = True
            return False
        newp = input("请输入您要修改的新密码：")
        newp1 = input("请再输入一遍新密码")
        user.card.passWord = newp
        print("密码修改成功")

    def lock(self):  # 锁卡
        cardnum2 = int(input("请输入您的卡号："))
        user = self.user_dic.get(cardnum2)
        if cardnum2 != user.card.cardNum:
            # if user == None
            print("此卡未开户")
            return False
        if user.card.isLock == True:
            print("您的卡已被锁定")
            return False
        for i in range(3):
            passWord2 = input("请输入密码")
            if passWord2 != user.card.passWord:
                print("您的密码输入错误")
                print("剩余%d次机会" % (2 - i))
            else:
                break
        else:
            print("3次机会用尽，卡已被锁定")
            user.card.isLock = True
            return False
        if user.card.isLock == False:
            user.card.isLock = True
            print("锁定成功")

    def unlock(self):  # 解锁
        cardnum2 = int(input("请输入您的卡号："))
        user = self.user_dic.get(cardnum2)
        if cardnum2 != user.card.cardNum:
            # if user == None
            print("此卡未开户")
            return False
        for i in range(3):
            passWord2 = input("请输入密码")
            if passWord2 != user.card.passWord:
                print("您的密码输入错误")
                print("剩余%d次机会" % (2 - i))
            else:
                break
        else:
            print("3次机会用尽,请明天再试")
            return False
        if user.card.isLock == False:
            print("您的卡未锁定")
            return False
        else:
            user.card.isLock = True
            print("恭喜你，解锁成功")

    def clear(self):  # 销户
        cardnum2 = int(input("请输入您的卡号："))
        user = self.user_dic.get(cardnum2)
        if user == None:
            # if cardnum2 != user.card.cardNum:
            print("此卡未开户")
            return False
        if user.card.isLock == True:
            print("您的卡已被锁定，查询失败。。。请解锁")
            return False
        for i in range(3):
            passWord2 = input("请输入密码")
            if passWord2 != user.card.passWord:
                print("您的密码输入错误")
                print("剩余%d次机会" % (2 - i))
            else:
                break
        else:
            print("3次机会用尽，卡已被锁定")
            user.card.isLock = True
            return False
        qingchu = input("销户后，所有信息将清除！确定销户请按y，否则请按n:")
        if qingchu == "y":
            self.user_dic.pop(cardnum2)
            print("销户成功")
        else:
            print("退出销户成功")
            return False

    def exit(self):
        sys.exit()