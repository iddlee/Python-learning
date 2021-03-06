'''
用户：User
    属性：姓名，手机号，身份证号，卡号
    行为：
卡：Card
    属性：卡号，密码，余额，是否锁定 （True锁定了False未锁定）
    行为：
ATM：
    属性：用户列表（存储所有开卡人的信息）
    行为：开户，查询，存款，取款，转账，改密，锁定，解锁，销户，退出
管理员：Admin
    属性：用户名，密码
    行为：登录
'''
from admin import Admin
from atm import Atm
def main():
    # 1.创建管理员对象
    ad = Admin("admin", "123")
    # 2. 管理员登录
    ad.landUI()
    # 3.创建atm对象
    atm = Atm()
    # 4.显示操作界面
    while True:
        atm.printOptionUI()  # 5.用户输入对应的编号，调用对应的函数
        bh = input("请输入编号")
        if bh == "1":
            atm.creatUser()
        elif bh == "2":
            atm.serach()
        elif bh == "3":
            atm.save()
        elif bh == "4":
            atm.take()
        elif bh == "5":
            atm.transfer()
        elif bh == "6":
            atm.change()
        elif bh == "7":
            atm.lock()
        elif bh == "8":
            atm.unlock()
        elif bh == "9":
            atm.clear()
        elif bh == "T":
            atm.exit()


if __name__ == '__main__':
    main()