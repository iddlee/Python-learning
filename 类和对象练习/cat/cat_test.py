from cat import Cat

def main():
    cat = []
    for i in range(3):
        newname = input("请输入姓名")
        newage = int(input("请输入年龄"))
        newcolor = input("请输入颜色")
        c = Cat(newname, newage, newcolor)
        cat.append(c)
    sum = 0
    for i in cat:  # 遍历猫这个列表
        i.show()
        i.run()
        i.miao()
        sum += i.getAge()
    print("三只猫的年龄之和为%d" % sum)

def find():
    global cat
    print("----检测有没有创建这只猫----")
    a = input("请输入猫的名字：")
    isA = False
    for i in cat:
        if i.getName() == a:
            print("找到了这只猫，猫的信息如下")
            i.show()
            isA = True
            break
        else:
            isA = False
    if isA == False:
        print("没有这只猫，程序结束")
    else:
        find()


if __name__ == "__main__":
    main()
    find()