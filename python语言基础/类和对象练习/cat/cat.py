# 1)✔	创建一个猫类（Cat），定义姓名、年龄、颜色三个属性。为私有的
# 2)✔	在猫类中写一个跑的方法，输出：name+跑步
# 3)✔	在猫类中写一个叫的方法，输出：name+在叫
# 4)✔	在猫类中写一个显示信息的show方法，输出：姓名：+name+年龄：+age+颜色+color
# 5)✔	在主函数中利用循环创建3只猫，并给猫的姓名、颜色、年龄赋值
# 6)✔	创建一个列表，将创建好的3只猫存储到列表中
# 7)✔	遍历列表，调用显示信息（show）方法、跑步、叫的方法
# 8)✔	定义一个求和变量求出3只猫的年龄总和并输出
# 9)✔	到此检查自己的代码有没有问题，是否和案例效果一致再往下做
# 10)✔	检测有没有这只猫：输出一个姓名，判断列表中有没有这只猫，有的话就调用show方法输出这只猫的信息并进行下一次输入检测，没有就结束程序。


# 1)✔	创建一个猫类（Cat），定义姓名、年龄、颜色三个属性。为私有的
class Cat:


    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

# 2)✔	在猫类中写一个跑的方法，输出：name+跑步
    def run(self):
        print("%s跑步" % self.__name)

# 3)✔	在猫类中写一个叫的方法，输出：name+在叫
    def miao(self):
        print("%s在叫" % self.__name)

# 4)✔	在猫类中写一个显示信息的show方法，输出：姓名：+name+年龄：+age+颜色+color
    def show(self):
        print("-------------猫的信息如下------------")
        print("姓名：%s    年龄：%d    颜色：%s" % (self.__name, self.__age, self.__color))