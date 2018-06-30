# 登录界面
def landUI():
    bh = int(input("请输入编号："))
    if bh == 1:
        i = 0
        while i < 3:
            name = input("请输入用户名：")
            password = input("请输入密码：")
            if name == "ldd" and password == "uuu":
                print("登陆成功")
                startUI()
                break
            else:
                print("登录失败，请重新输入")
                print("你还有%d次机会" % (2-i))
            i += 1

def startUI():
    welcome = "******欢迎进入手机购物******"
    print(welcome.center(50))
    print("******1.今日特卖******")
    print("******2.女士服装******")
    print("******3.男士服装******")
    print("******4.美食茶酒******")
    print("******5.结算******")
    bh = int(input("请输入编号："))
    if bh == 1:
        todayUI()
    elif bh == 2:
        woman()
    elif bh == 3:
        man()
    elif bh == 4:
        food()
    elif bh == 5:
        checkout()

def todayUI():
    print("******1  毛衫连衣裙  59元******")
    print("******2  运动鞋  69元******")
    print("******3  风衣  99元******")
    bh = int(input("请输入要购买的商品编号："))
    if bh == 1:
        # 将商品信息存入到购物车（字典）中
        gwc["毛衫连衣裙"] = 59
    elif bh == 2:
        gwc["运动鞋"] = 69
    elif bh == 3:
        gwc["风衣"] = 99
    print("购买成功，是否继续y/n")
    isY = input()
    if isY == "y":
        todayUI()
    else:
        print("当前购物车商品信息有：")
        for k, v in gwc.items():
            print(k, v)
        startUI()

def man():
    print("******1  polo衬衫  59元******")
    print("******2  运动鞋  99元******")
    print("******3  牛仔裤  109元******")
    bh = int(input("请输入要购买的商品编号："))
    if bh == 1:
        # 将商品信息存入到购物车（字典）中
        gwc["polo衬衫"] = 59
    elif bh == 2:
        gwc["运动鞋"] = 99
    elif bh == 3:
        gwc["牛仔裤"] = 109
    print("购买成功，是否继续y/n")
    isY = input()
    if isY == "y":
        man()
    else:
        print("当前购物车商品信息有：")
        for k, v in gwc.items():
            print(k, v)
        startUI()

def woman():
    print("******1  毛衫连衣裙  59元******")
    print("******2  高跟鞋  199元******")
    print("******3  风衣  99元******")
    bh = int(input("请输入要购买的商品编号："))
    if bh == 1:
        # 将商品信息存入到购物车（字典）中
        gwc["毛衫连衣裙"] = 59
    elif bh == 2:
        gwc["高跟鞋"] = 199
    elif bh == 3:
        gwc["风衣"] = 99
    print("购买成功，是否继续y/n")
    isY = input()
    if isY == "y":
        woman()
    else:
        print("当前购物车商品信息有：")
        for k, v in gwc.items():
            print(k, v)
        startUI()

def food():
    print("******1  咖啡  50元******")
    print("******2  零食大礼包  49元******")
    print("******3  柠檬  30元******")
    bh = int(input("请输入要购买的商品编号："))
    if bh == 1:
        # 将商品信息存入到购物车（字典）中
        gwc["咖啡"] = 50
    elif bh == 2:
        gwc["零食大礼包"] = 49
    elif bh == 3:
        gwc["柠檬"] = 30
    print("购买成功，是否继续y/n")
    isY = input()
    if isY == "y":
        food()
    else:
        print("当前购物车商品信息有：")
        for k, v in gwc.items():
            print(k, v)
        startUI()

def checkout():
    welcome = "******欢迎进入手机购物******"
    print(welcome.center(50))
    print("您本次购买的商品列表如下：")
    for k, v in gwc.items():
        print(k, v)
    sum = 0
    for v in gwc.values():
        sum += v
    print("本次总共消费：%d" % sum)
    gwc.clear()
    print("谢谢您使用手机购物，继续购物请按w，退出请按0")
    isW = input()
    if isW == "w":
        startUI()
    else:
        print("退出成功")

gwc = {}  # 空的购物车
welcome = "******欢迎进入手机购物******"
print(welcome.center(50))
print("1：登录")
print("2：退出")
landUI()